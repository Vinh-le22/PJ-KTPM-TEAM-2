# Hệ thống Quản lý Thư viện

## Yêu cầu hệ thống

- Python 3.8 trở lên
- pip (Python package manager)
- Git
- Trình duyệt web hiện đại (Chrome, Firefox, Edge...)
- Pillow (thư viện xử lý ảnh)

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
pip install Pillow  # Cài đặt Pillow để xử lý ảnh
```

3. Chạy migrations:
```bash
python manage.py makemigrations
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
- Thêm ảnh bìa sách
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


