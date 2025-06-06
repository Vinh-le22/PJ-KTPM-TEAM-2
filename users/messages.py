from django.utils.translation import gettext_lazy as _

# Thông báo đăng nhập
LOGIN_SUCCESS = _('Đăng nhập thành công!')
LOGIN_ERROR = _('Tên đăng nhập hoặc mật khẩu không chính xác.')
LOGIN_REQUIRED = _('Vui lòng đăng nhập để tiếp tục.')

# Thông báo đăng xuất
LOGOUT_SUCCESS = _('Đăng xuất thành công!')

# Thông báo đăng ký
REGISTER_SUCCESS = _('Đăng ký tài khoản thành công!')
REGISTER_ERROR = _('Có lỗi xảy ra trong quá trình đăng ký.')

# Thông báo thay đổi mật khẩu
PASSWORD_CHANGE_SUCCESS = _('Mật khẩu đã được thay đổi thành công!')
PASSWORD_CHANGE_ERROR = _('Mật khẩu cũ không chính xác.')
PASSWORD_MISMATCH = _('Mật khẩu mới không khớp.')
PASSWORD_TOO_SHORT = _('Mật khẩu phải có ít nhất 8 ký tự.')
PASSWORD_TOO_COMMON = _('Mật khẩu quá đơn giản.')
PASSWORD_ENTIRELY_NUMERIC = _('Mật khẩu không được chỉ chứa số.')

# Thông báo cập nhật thông tin
PROFILE_UPDATE_SUCCESS = _('Thông tin cá nhân đã được cập nhật!')
PROFILE_UPDATE_ERROR = _('Có lỗi xảy ra khi cập nhật thông tin.') 