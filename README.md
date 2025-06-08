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
python manage.py createsuperuser
```

5. Chạy server:
```bash
python manage.py runserver
```

Truy cập:
- Trang chủ: http://127.0.0.1:8000
- Trang quản trị: http://127.0.0.1:8000/admin

## Cấu trúc dự án và Model

### Apps và Models

1. **users app**
   - Model: `UserProfile`
     - Liên kết với User model của Django
     - Phân quyền: admin/reader
     - Thông tin: số điện thoại, địa chỉ

2. **books app**
   - Models:
     - `Category`: Danh mục sách
     - `Author`: Thông tin tác giả
     - `Book`: Thông tin sách (tên, tác giả, số lượng, mô tả)

3. **borrow app**
   - Models:
     - `BorrowRecord`: Ghi nhận mượn sách
     - `ReturnRecord`: Ghi nhận trả sách

4. **stats_app**
   - Model: `Statistic`
     - Thống kê theo thời gian
     - Số lượng sách, người dùng, lượt mượn

### Cấu trúc thư mục
```
library_project/
├── library_project/    # Thư mục cấu hình dự án
├── users/             # Quản lý người dùng
├── books/             # Quản lý sách
├── borrow/            # Quản lý mượn trả
├── stats_app/         # Thống kê và báo cáo
├── templates/         # Templates chung
├── static/           # Static files (CSS, JS, images)
├── media/            # User uploaded files
├── requirements.txt  # Dependencies
└── manage.py         # Django management script
```

## Tính năng chi tiết

### Quản lý người dùng (users app)
- Đăng ký tài khoản mới
- Đăng nhập/Đăng xuất
- Quản lý thông tin cá nhân
- Phân quyền người dùng (admin/reader)

### Quản lý sách (books app)
- Thêm/sửa/xóa sách
- Tìm kiếm sách theo tên, tác giả
- Phân loại sách theo thể loại

### Quản lý mượn trả (borrow app)
- Mượn sách
- Trả sách
- Xem lịch sử mượn trả

### Thống kê (stats_app)
- Thống kê số lượng sách
- Thống kê người mượn
- Thống kê lượt mượn

## Phân quyền người dùng

### Admin
- Quản lý tất cả người dùng
- Quản lý toàn bộ sách
- Xem thống kê và báo cáo
- Quản lý mượn trả sách

### Người dùng thường
- Xem thông tin cá nhân
- Mượn và trả sách
- Xem lịch sử mượn
- Tìm kiếm sách

## Công nghệ sử dụng

- Backend: Django 5.2.2 (Python 3.x)
- Database: SQLite (mặc định trong Django)
- Frontend: Template Django (HTML + CSS cơ bản)
- Authentication: Django built-in auth system
- Forms: Django Forms
- Admin Interface: Django Admin

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

- stats_app/ - Thống kê và báo cáo

- templates/ - File HTML (nếu có dùng ngoài app)

- db.sqlite3 - File database SQLite

