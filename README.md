# Hệ thống Quản lý Thư viện

## Yêu cầu hệ thống

- Python 3.8 trở lên
- pip (Python package manager)
- Git
- Trình duyệt web hiện đại (Chrome, Firefox, Edge...)

## Cài đặt

1. Clone dự án:
```bash
git clone <repository-url>
cd library_project
```

2. Tạo môi trường ảo và cài đặt dependencies:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
pip install -r requirements.txt
```

3. Chạy migrations:
```bash
python manage.py migrate
```

4. Tạo tài khoản admin mặc định:
```bash
python manage.py create_default_admin
```

Thông tin đăng nhập mặc định:
- Tên đăng nhập: admin
- Mật khẩu: admin123
- Email: admin@library.com

**Lưu ý quan trọng**: 
- Vui lòng đổi mật khẩu sau khi đăng nhập lần đầu!
- Không sử dụng mật khẩu mặc định trong môi trường production

5. Chạy server:
```bash
python manage.py runserver
```

Truy cập:
- Trang chủ: http://127.0.0.1:8000
- Trang quản trị: http://127.0.0.1:8000/admin

## Tính năng chi tiết

### Quản lý người dùng
- Đăng ký tài khoản mới
- Đăng nhập/Đăng xuất
- Quản lý thông tin cá nhân
- Đổi mật khẩu
- Xem lịch sử mượn sách

### Quản lý sách
- Thêm sách mới
- Cập nhật thông tin sách
- Xóa sách
- Tìm kiếm sách
- Phân loại sách theo thể loại

### Quản lý mượn trả
- Mượn sách
- Trả sách
- Gia hạn thời gian mượn
- Xem lịch sử mượn trả
- Thông báo quá hạn

### Tính năng khác
- Giao diện tiếng Việt
- Responsive design
- Thống kê và báo cáo
- Tìm kiếm nâng cao

## Phân quyền người dùng

### Admin
- Quản lý tất cả người dùng
- Quản lý toàn bộ sách
- Xem thống kê và báo cáo
- Quản lý mượn trả sách
- Cấu hình hệ thống

### Người dùng thường
- Xem thông tin cá nhân
- Mượn và trả sách
- Xem lịch sử mượn
- Tìm kiếm sách

## Xử lý lỗi thường gặp

1. Lỗi "ModuleNotFoundError":
```bash
pip install -r requirements.txt
```

2. Lỗi database:
```bash
python manage.py migrate --run-syncdb
```

3. Lỗi static files:
```bash
python manage.py collectstatic
```

4. Lỗi port đang sử dụng:
```bash
python manage.py runserver 8001  # Thay đổi port
```

## Công nghệ sử dụng

- Backend: Django 5.2.2 (Python 3.x)
- Database: SQLite (mặc định trong Django)
- Frontend: Template Django (HTML + CSS cơ bản)
- Authentication: Django built-in auth system
- Forms: Django Forms
- Admin Interface: Django Admin

## Cấu trúc dự án
```
library_project/
├── library_project/    # Thư mục cấu hình dự án
├── users/             # Quản lý người dùng
├── books/             # Quản lý sách
├── borrow/            # Quản lý mượn trả
├── statistics/        # Thống kê và báo cáo
├── templates/         # Templates chung
├── static/           # Static files (CSS, JS, images)
├── media/            # User uploaded files
├── requirements.txt  # Dependencies
└── manage.py         # Django management script
```

## Đóng góp

Mọi đóng góp đều được hoan nghênh! Vui lòng:
1. Fork dự án
2. Tạo branch mới
3. Commit thay đổi
4. Push lên branch
5. Tạo Pull Request

## Giấy phép

Dự án này được phát hành dưới giấy phép MIT.

## Mô tả dự án

Dự án **Quản lý Thư viện** là một ứng dụng web xây dựng bằng Django, phục vụ quản lý các chức năng cơ bản của thư viện như:

- Đăng nhập / Đăng ký người dùng
- Quản lý sách: thêm, sửa, xóa, tìm kiếm
- Quản lý mượn và trả sách
- Quản lý người dùng
- Xem lịch sử mượn trả sách
- Thống kê số lượng sách và người mượn

---

## Công nghệ sử dụng

- Backend: Django 5.2.2 (Python 3.x)
- Database: SQLite (mặc định trong Django)
- Frontend: Template Django (HTML + CSS cơ bản)

---

## Cài đặt và chạy dự án

1. Clone dự án về máy:
   ```bash
   git clone <đường dẫn repo>
   cd library_project
2. Chạy migration để tạo database và bảng:

    python manage.py makemigrations
    python manage.py migrate
3. Tạo user admin (quản trị viên):
    
    python manage.py createsuperuser

4. Chạy server:

    python manage.py runserver

5. Truy cập ứng dụng tại: http://127.0.0.1:8000

## Cấu trúc dự án
- library_project/ - Thư mục chính dự án Django

- users/ - Quản lý đăng nhập, đăng ký, người dùng

- books/ - Quản lý sách

- borrow/ - Quản lý mượn và trả sách

- statistics/ - Thống kê và báo cáo

- templates/ - File HTML (nếu có dùng ngoài app)

- db.sqlite3 - File database SQLite

