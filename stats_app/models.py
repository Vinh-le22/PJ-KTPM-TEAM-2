from django.db import models
from django.contrib.auth.models import User
from books.models import Book, Category
from borrow.models import BorrowRecord

class Statistic(models.Model):
    STAT_TYPE_CHOICES = (
        ('daily', 'Hàng ngày'),
        ('weekly', 'Hàng tuần'),
        ('monthly', 'Hàng tháng'),
        ('yearly', 'Hàng năm'),
    )

    stat_type = models.CharField(max_length=20, choices=STAT_TYPE_CHOICES)
    start_date = models.DateField()
    end_date = models.DateField()
    
    # Book statistics
    total_books = models.PositiveIntegerField(default=0)
    total_borrowed_books = models.PositiveIntegerField(default=0)
    total_available_books = models.PositiveIntegerField(default=0)
    
    # User statistics
    total_users = models.PositiveIntegerField(default=0)
    
    # Borrow statistics
    total_borrows = models.PositiveIntegerField(default=0)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.get_stat_type_display()} - {self.start_date} to {self.end_date}"

    class Meta:
        ordering = ['-end_date']
        unique_together = ['stat_type', 'start_date', 'end_date']
