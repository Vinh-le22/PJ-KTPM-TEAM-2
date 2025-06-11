from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.db.models import Q
from .models import Book, Category, Author
from .forms import BookForm, CategoryForm, AuthorForm, BookSearchForm

def is_admin(user):
    return user.is_staff

# Create your views here.

@login_required
def book_list(request):
    search_form = BookSearchForm(request.GET)
    books = Book.objects.all()
    
    if search_form.is_valid():
        search_query = search_form.cleaned_data.get('search_query')
        category = search_form.cleaned_data.get('category')
        
        if search_query:
            books = books.filter(
                Q(title__icontains=search_query) |
                Q(author__name__icontains=search_query)
            )
        
        if category:
            books = books.filter(category=category)
    
    categories = Category.objects.all()
    context = {
        'books': books,
        'search_form': search_form,
        'categories': categories,
        'is_admin': request.user.is_staff,
    }
    return render(request, 'books/book_list.html', context)

@login_required
def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'books/book_detail.html', {
        'book': book,
        'is_admin': request.user.is_staff
    })

@user_passes_test(is_admin)
def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save()
            messages.success(request, 'Sách đã được thêm thành công!')
            return redirect('book_detail', pk=book.pk)
    else:
        form = BookForm()
    return render(request, 'books/book_form.html', {'form': form, 'action': 'Thêm'})

@user_passes_test(is_admin)
def book_edit(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            book = form.save()
            messages.success(request, 'Sách đã được cập nhật thành công!')
            return redirect('book_detail', pk=book.pk)
    else:
        form = BookForm(instance=book)
    return render(request, 'books/book_form.html', {'form': form, 'action': 'Sửa'})

@user_passes_test(is_admin)
def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        messages.success(request, 'Sách đã được xóa thành công!')
        return redirect('book_list')
    return render(request, 'books/book_confirm_delete.html', {'book': book})

@user_passes_test(is_admin)
def category_list(request):
    categories = Category.objects.all()
    return render(request, 'books/category_list.html', {'categories': categories})

@user_passes_test(is_admin)
def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save()
            messages.success(request, 'Thể loại đã được thêm thành công!')
            return redirect('category_list')
    else:
        form = CategoryForm()
    return render(request, 'books/category_form.html', {'form': form, 'action': 'Thêm'})

@user_passes_test(is_admin)
def author_list(request):
    authors = Author.objects.all()
    return render(request, 'books/author_list.html', {'authors': authors})

@user_passes_test(is_admin)
def author_create(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            author = form.save()
            messages.success(request, 'Tác giả đã được thêm thành công!')
            return redirect('author_list')
    else:
        form = AuthorForm()
    return render(request, 'books/author_form.html', {'form': form, 'action': 'Thêm'})
