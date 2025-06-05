# Library Management System

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
   git clone https://github.com/Vinh-le22/PJ-KTPM-TEAM-2.git
   cd library_project
2. Chạy migration để tạo database và bảng:
   ```bash
    python manage.py makemigrations
    python manage.py migrate
3. Tạo user admin (quản trị viên):
    ```bash
    python manage.py createsuperuser

4. Chạy server:
   ```bash
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

