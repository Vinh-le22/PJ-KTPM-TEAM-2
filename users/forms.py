from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Nhập email của bạn'})
    )
    username = forms.CharField(
        label='Tên đăng nhập',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nhập tên đăng nhập'})
    )
    password1 = forms.CharField(
        label='Mật khẩu',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Nhập mật khẩu'})
    )
    password2 = forms.CharField(
        label='Xác nhận mật khẩu',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Nhập lại mật khẩu'})
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Cập nhật các thông báo lỗi
        self.fields['username'].error_messages = {
            'required': 'Vui lòng nhập tên đăng nhập.',
            'unique': 'Tên đăng nhập này đã tồn tại.',
            'invalid': 'Tên đăng nhập không hợp lệ. Chỉ được chứa chữ cái, số và ký tự @/./+/-/_',
            'max_length': 'Tên đăng nhập không được vượt quá 150 ký tự.'
        }
        self.fields['email'].error_messages = {
            'required': 'Vui lòng nhập email.',
            'invalid': 'Email không hợp lệ.',
            'unique': 'Email này đã được sử dụng.'
        }
        self.fields['password1'].error_messages = {
            'required': 'Vui lòng nhập mật khẩu.',
            'password_too_short': 'Mật khẩu phải có ít nhất 8 ký tự.',
            'password_too_common': 'Mật khẩu quá đơn giản.',
            'password_entirely_numeric': 'Mật khẩu không được chỉ chứa số.'
        }
        self.fields['password2'].error_messages = {
            'required': 'Vui lòng xác nhận mật khẩu.',
            'password_mismatch': 'Mật khẩu xác nhận không khớp.'
        }

class UserLoginForm(forms.Form):
    username = forms.CharField(
        label='Tên đăng nhập',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nhập tên đăng nhập'})
    )
    password = forms.CharField(
        label='Mật khẩu',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Nhập mật khẩu'})
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].error_messages = {
            'required': 'Vui lòng nhập tên đăng nhập.'
        }
        self.fields['password'].error_messages = {
            'required': 'Vui lòng nhập mật khẩu.'
        }

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        labels = {
            'first_name': 'Tên',
            'last_name': 'Họ',
            'email': 'Email'
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nhập tên của bạn'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nhập họ của bạn'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Nhập email của bạn'})
        } 