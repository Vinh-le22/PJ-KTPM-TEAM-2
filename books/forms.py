from django import forms
from .models import Book, Category, Author

class BookForm(forms.ModelForm):
    author_name = forms.CharField(
        label='Tên tác giả',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Nhập tên tác giả'
        })
    )

    class Meta:
        model = Book
        fields = ['title', 'category', 'description', 'publication_year', 'total_copies']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nhập tên sách'
            }),
            'category': forms.Select(attrs={
                'class': 'form-select',
                'placeholder': 'Chọn thể loại'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Nhập mô tả ngắn về nội dung sách',
                'rows': 4
            }),
            'publication_year': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nhập năm xuất bản',
                'min': 1
            }),
            'total_copies': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nhập số lượng sách',
                'min': 1
            })
        }
        labels = {
            'title': 'Tên sách',
            'category': 'Thể loại',
            'description': 'Mô tả',
            'publication_year': 'Năm xuất bản',
            'total_copies': 'Số lượng'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Lấy danh sách các thể loại sách
        self.fields['category'].queryset = Category.objects.all().order_by('name')
        # Thêm placeholder cho dropdown
        self.fields['category'].empty_label = "Chọn thể loại sách"

        if kwargs.get('instance'):
            self.fields['author_name'].initial = kwargs['instance'].author.name

    def save(self, commit=True):
        book = super().save(commit=False)
        author_name = self.cleaned_data.get('author_name')
        author, created = Author.objects.get_or_create(name=author_name)
        book.author = author
        book.available_copies = book.total_copies
        if commit:
            book.save()
        return book

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name']

class BookSearchForm(forms.Form):
    search_query = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Tìm kiếm theo tên sách hoặc tác giả...'})
    )
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        required=False,
        empty_label="Tất cả thể loại"
    ) 