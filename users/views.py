from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout, update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from .forms import UserRegisterForm, UserLoginForm, UserProfileForm, CustomPasswordChangeForm
from .messages import (
    LOGIN_SUCCESS, LOGIN_ERROR, LOGOUT_SUCCESS,
    REGISTER_SUCCESS, REGISTER_ERROR,
    PASSWORD_CHANGE_SUCCESS, PASSWORD_CHANGE_ERROR
)

def register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, REGISTER_SUCCESS)
            return redirect('login')
        else:
            messages.error(request, REGISTER_ERROR)
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
        
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, LOGIN_SUCCESS)
            
            # Kiểm tra nếu là superuser và mật khẩu mặc định
            if user.is_superuser and user.check_password('admin123'):
                messages.warning(request, 'Vui lòng đổi mật khẩu mặc định của tài khoản admin để bảo mật hệ thống.')

            next_url = request.GET.get('next', 'home')
            return redirect(next_url)
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, error)
    else:
        form = UserLoginForm()
    return render(request, 'users/login.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    messages.success(request, LOGOUT_SUCCESS)
    return redirect('home')

@login_required
def profile_view(request):
    return render(request, 'users/profile.html', {'user': request.user})

@login_required
def edit_profile_view(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thông tin cá nhân đã được cập nhật thành công!')
            return redirect('profile')
    else:
        form = UserProfileForm(instance=request.user)
    return render(request, 'users/edit_profile.html', {'form': form})

@login_required
def change_password(request):
    if request.method == 'POST':
        form = CustomPasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, PASSWORD_CHANGE_SUCCESS)
            return redirect('profile')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{form.fields[field].label}: {error}")
    else:
        form = CustomPasswordChangeForm(request.user)
    return render(request, 'users/change_password.html', {'form': form})
