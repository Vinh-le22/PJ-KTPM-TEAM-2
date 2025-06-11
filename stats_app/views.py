from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db.models import Count, Sum
from django.utils import timezone
from datetime import timedelta
from books.models import Book
from borrow.models import BorrowRecord
from django.contrib.auth.models import User

def is_admin(user):
    return user.is_staff

@user_passes_test(is_admin)
def dashboard(request):
    # Thống kê sách
    total_books = Book.objects.count()
    available_books = Book.objects.filter(status='available').count()
    borrowed_books = Book.objects.filter(status='borrowed').count()
    
    # Thống kê người dùng
    total_users = User.objects.count()
    active_users = BorrowRecord.objects.values('user').distinct().count()
    
    # Thống kê mượn trả
    total_borrows = BorrowRecord.objects.count()
    current_borrows = BorrowRecord.objects.filter(status='approved').count()
    overdue_borrows = BorrowRecord.objects.filter(
        status='approved',
        due_date__lt=timezone.now().date()
    ).count()
    
    # Thống kê theo thể loại
    category_stats = Book.objects.values('category__name').annotate(
        total=Count('id')
    ).order_by('-total')
    
    # Thống kê theo thời gian
    today = timezone.now().date()
    last_week = today - timedelta(days=7)
    last_month = today - timedelta(days=30)
    
    weekly_borrows = BorrowRecord.objects.filter(
        created_at__date__gte=last_week
    ).count()
    
    monthly_borrows = BorrowRecord.objects.filter(
        created_at__date__gte=last_month
    ).count()
    
    context = {
        'total_books': total_books,
        'available_books': available_books,
        'borrowed_books': borrowed_books,
        'total_users': total_users,
        'active_users': active_users,
        'total_borrows': total_borrows,
        'current_borrows': current_borrows,
        'overdue_borrows': overdue_borrows,
        'category_stats': category_stats,
        'weekly_borrows': weekly_borrows,
        'monthly_borrows': monthly_borrows,
    }
    
    return render(request, 'stats_app/dashboard.html', context)
