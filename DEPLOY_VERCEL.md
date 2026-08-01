# HƯỚNG DẪN TRIỂN KHAI DỰ ÁN LÊN VERCEL (1-CLICK DEPLOYMENT GUIDE)

Tài liệu này hướng dẫn chi tiết từng bước triển khai toàn bộ ứng dụng **Siêu Club Học Tập & Tập Thi IELTS** lên nền tảng **Vercel Platform Cloud**.

---

## 1. Cấu Trúc Các Tệp Đã Chuẩn Bị Ready Cho Vercel

Dự án đã được tích hợp sẵn 100% bộ tệp triển khai Vercel:
- **`vercel.json`**: Điều hướng Router cho Python Serverless API và Static Assets Frontend.
- **`api/index.py`**: Động cơ Backend Serverless Python (Flask REST API) xử lý cấp phát câu hỏi, chấm điểm tự động và lưu cài đặt mục tiêu.
- **`requirements.txt`**: Khai báo thư viện Python hỗ trợ Serverless Vercel Build.
- **`public/index.html`**: Giao diện Web Application Dashboard trực tuyến đầy đủ tính năng.

---

## 2. Các Bước Triển Khai Lên Vercel (2 Cách Nhanh Nhất)

### Cách 1: Triển Khai Qua GitHub (Khuyên Dùng)

1. **Đẩy mã nguồn dự án lên GitHub**:
   - Mở Terminal tại thư mục dự án và chạy các lệnh:
     ```bash
     git init
     git add .
     git commit -m "Deploy Sieu Club Hoc Tap & Tap Thi IELTS len Vercel"
     git branch -M main
     git remote add origin <URL_REPOSITORY_GITHUB_CỦA_BẠN>
     git push -u origin main
     ```

2. **Đăng nhập Vercel & Import Repository**:
   - Truy cập [https://vercel.com](https://vercel.com) và đăng nhập tài khoản (hoặc chọn Login with GitHub).
   - Bấm nút **"Add New..."** -> chọn **"Project"**.
   - Chọn kho chứa GitHub vừa tạo và bấm **"Import"**.

3. **Deploy 1-Click**:
   - Giữ nguyên các thiết lập mặc định (Framework Preset: Other / None).
   - Bấm nút **"Deploy"**.
   - Vercel sẽ tự động build ứng dụng và cung cấp đường link tên miền chính thức (Ví dụ: `https://sieu-club-hoc-tap.vercel.app`).

---

### Cách 2: Triển Khai Trực Tiếp Qua Vercel CLI (Dành cho Lập trình viên)

1. Cài đặt Vercel CLI toàn cục (nếu chưa có):
   ```bash
   npm install -g vercel
   ```

2. Mở Terminal tại thư mục dự án và gõ lệnh:
   ```bash
   vercel
   ```

3. Đăng nhập và xác nhận thông số cấu hình mặc định (bấm Enter liên tục).
4. Vercel CLI sẽ tự động tải lên và trả về đường link trang web dự án trực tuyến ngay lập tức!
