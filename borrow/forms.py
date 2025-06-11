from django import forms
from .models import BorrowRecord, ReturnRecord
from books.models import Book
from django.utils import timezone

class BorrowForm(forms.ModelForm):
    class Meta:
        model = BorrowRecord
        fields = ['notes', 'due_date']
        widgets = {
            'notes': forms.Textarea(attrs={'rows': 3}),
            'due_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }
        labels = {
            'notes': 'Ghi chú',
            'due_date': 'Ngày trả',
        }

    def __init__(self, *args, **kwargs):
        self.book = kwargs.pop('book', None) # Lấy đối tượng sách ra khỏi kwargs
        super().__init__(*args, **kwargs)
        # Loại bỏ các trường không cần thiết
        if 'book' in self.fields:
            del self.fields['book']
        if 'borrow_date' in self.fields:
            del self.fields['borrow_date']

    def clean(self):
        cleaned_data = super().clean()
        if self.book and self.book.available_copies <= 0:
            raise forms.ValidationError("Sách này hiện đã hết hoặc không có sẵn.")
        return cleaned_data

    def clean_due_date(self):
        due_date = self.cleaned_data.get('due_date')
        if due_date:
            today = timezone.now().date()
            if due_date < today:
                raise forms.ValidationError("Ngày phải trả không thể là ngày trong quá khứ.")
            if (due_date - today).days > 30:
                raise forms.ValidationError("Ngày phải trả không được quá 30 ngày kể từ ngày hôm nay.")
        return due_date

class ReturnForm(forms.ModelForm):
    class Meta:
        model = ReturnRecord
        fields = ['return_date', 'notes']
        widgets = {
            'return_date': forms.DateInput(attrs={'type': 'date'}),
            'notes': forms.Textarea(attrs={'rows': 3}),
        }
        labels = {
            'return_date': 'Ngày trả',
            'notes': 'Ghi chú',
        } 