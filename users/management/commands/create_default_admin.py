from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

class Command(BaseCommand):
    help = 'Tạo tài khoản admin mặc định nếu chưa tồn tại'

    def handle(self, *args, **options):
        if not User.objects.filter(username='admin').exists():
            User.objects.create(
                username='admin',
                email='admin@library.com',
                password=make_password('admin123'),
                is_superuser=True,
                is_staff=True,
                first_name='Admin',
                last_name='System'
            )
            self.stdout.write(self.style.SUCCESS('Đã tạo tài khoản admin mặc định thành công!'))
            self.stdout.write(self.style.WARNING('Tên đăng nhập: admin'))
            self.stdout.write(self.style.WARNING('Mật khẩu: admin123'))
            self.stdout.write(self.style.WARNING('Vui lòng đổi mật khẩu sau khi đăng nhập!'))
        else:
            self.stdout.write(self.style.WARNING('Tài khoản admin đã tồn tại!')) 