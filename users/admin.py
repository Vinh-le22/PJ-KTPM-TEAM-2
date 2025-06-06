from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.contrib import messages

class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Thông tin cá nhân'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Quyền hạn'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Thông tin quan trọng'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2'),
        }),
    )
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('username', 'first_name', 'last_name', 'email')
    ordering = ('username',)

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        if obj and obj.is_superuser:
            messages.warning(request, _('Vui lòng đổi mật khẩu mặc định của tài khoản admin để bảo mật hệ thống.'))
        return form

# Đăng ký lại UserAdmin với cấu hình mới
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

# Thay đổi tiêu đề trang admin
admin.site.site_header = _('Quản trị Hệ thống Thư viện')
admin.site.site_title = _('Quản trị Thư viện')
admin.site.index_title = _('Quản lý Hệ thống Thư viện')

# Thêm thông báo yêu cầu đổi mật khẩu
def get_admin_site(request):
    if request.user.is_superuser and request.user.check_password('admin123'):
        messages.warning(request, _('Vui lòng đổi mật khẩu mặc định của tài khoản admin để bảo mật hệ thống.'))
