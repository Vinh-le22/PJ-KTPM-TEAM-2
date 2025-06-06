from django.contrib import messages
from django.utils.translation import gettext_lazy as _

class AdminPasswordChangeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated and request.user.is_superuser:
            if request.user.check_password('admin123'):
                messages.warning(request, _('Vui lòng đổi mật khẩu mặc định của tài khoản admin để bảo mật hệ thống.'))
        
        response = self.get_response(request)
        return response 