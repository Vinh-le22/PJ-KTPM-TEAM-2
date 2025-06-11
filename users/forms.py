from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import authenticate

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

class UserLoginForm(AuthenticationForm):
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

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if user is None:
                raise forms.ValidationError('Tên đăng nhập hoặc mật khẩu không chính xác.')
            elif not user.is_active:
                raise forms.ValidationError('Tài khoản của bạn đã bị khóa.')
        return cleaned_data

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

class CustomPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        label=_('Mật khẩu hiện tại'),
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Nhập mật khẩu hiện tại'
        })
    )
    new_password1 = forms.CharField(
        label=_('Mật khẩu mới'),
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Nhập mật khẩu mới'
        }),
        help_text=_('Mật khẩu phải có ít nhất 8 ký tự và không được quá đơn giản.')
    )
    new_password2 = forms.CharField(
        label=_('Xác nhận mật khẩu mới'),
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Nhập lại mật khẩu mới'
        })
    )

    def clean_old_password(self):
        old_password = self.cleaned_data.get('old_password')
        if not self.user.check_password(old_password):
            raise forms.ValidationError(_('Mật khẩu hiện tại không chính xác.'))
        return old_password

    def clean_new_password2(self):
        password1 = self.cleaned_data.get('new_password1')
        password2 = self.cleaned_data.get('new_password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(_('Mật khẩu mới không khớp.'))
        return password2 