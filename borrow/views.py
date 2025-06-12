from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.utils import timezone
from .models import BorrowRecord, ReturnRecord, Book
from .forms import BorrowForm, ReturnForm

@login_required
def borrow_list(request):
    if request.user.is_staff:
        borrows = BorrowRecord.objects.all().order_by('-created_at')
    else:
        borrows = BorrowRecord.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'borrow/borrow_list.html', {'borrows': borrows, 'is_admin': request.user.is_staff})

@login_required
def borrow_create(request, book_pk=None):
    book = None
    if book_pk:
        book = get_object_or_404(Book, pk=book_pk)

    if request.method == 'POST':
        form = BorrowForm(request.POST, book=book)
        if form.is_valid():
            borrow = form.save(commit=False)
            borrow.user = request.user
            borrow.book = book
            borrow.borrow_date = timezone.now().date()
            borrow.status = 'pending'
            borrow.save()
            
            messages.success(request, 'Yêu cầu mượn sách đã được gửi!')
            return redirect('borrow_list')
    else:
        form = BorrowForm(book=book)

    context = {
        'form': form,
        'book': book,
        'current_date': timezone.now().date(),
    }
    return render(request, 'borrow/borrow_form.html', context)

@login_required
def borrow_detail(request, pk):
    borrow = get_object_or_404(BorrowRecord, pk=pk, user=request.user)
    return render(request, 'borrow/borrow_detail.html', {'borrow': borrow})

@login_required
def return_book(request, pk):
    borrow = get_object_or_404(BorrowRecord, pk=pk, user=request.user)
    
    if borrow.status != 'approved':
        messages.error(request, 'Không thể trả sách này!')
        return redirect('borrow_list')
    
    if request.method == 'POST':
        form = ReturnForm(request.POST)
        if form.is_valid():
            return_record = form.save(commit=False)
            return_record.borrow_record = borrow
            return_record.save()
            
            # Cập nhật trạng thái mượn dựa trên ngày trả
            if return_record.return_date and return_record.return_date > borrow.due_date:
                borrow.status = 'overdue'
            else:
                borrow.status = 'returned'
            borrow.return_date = return_record.return_date
            borrow.save()
            
            # Cập nhật số lượng sách
            book = borrow.book
            book.available_copies += 1
            if book.status == 'borrowed':
                book.status = 'available'
            book.save()
            
            messages.success(request, 'Sách đã được trả thành công!')
            return redirect('borrow_list')
    else:
        form = ReturnForm()
    
    return render(request, 'borrow/return_form.html', {
        'form': form,
        'borrow': borrow
    })

def is_admin(user):
    return user.is_staff

@login_required
@user_passes_test(is_admin)
def borrow_approve(request, pk):
    borrow = get_object_or_404(BorrowRecord, pk=pk)
    if borrow.status == 'pending':
        borrow.status = 'approved'
        borrow.borrow_date = timezone.now().date()
        # Set due_date 14 days from borrow_date (example)
        borrow.due_date = borrow.borrow_date + timezone.timedelta(days=14)
        borrow.save()
        
        # Cập nhật số lượng sách
        book = borrow.book
        book.available_copies -= 1
        if book.available_copies == 0:
            book.status = 'borrowed'
        book.save()

        messages.success(request, 'Yêu cầu mượn sách đã được duyệt!')
    else:
        messages.error(request, 'Không thể duyệt yêu cầu mượn này.')
    return redirect('borrow_list')

@login_required
@user_passes_test(is_admin)
def borrow_reject(request, pk):
    borrow = get_object_or_404(BorrowRecord, pk=pk)
    if borrow.status == 'pending':
        borrow.status = 'rejected'
        borrow.save()
        
        messages.warning(request, 'Yêu cầu mượn sách đã bị từ chối!')
    else:
        messages.error(request, 'Không thể từ chối yêu cầu mượn này.')
    return redirect('borrow_list')
