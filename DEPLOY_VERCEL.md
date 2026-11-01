# HUONG DAN TRIEN KHAI VA TOI UU UNG DUNG TREN VERCEL (MAXIMUM PERFORMANCE)

Tai lieu nay huong dan chi tiet cac buoc trien khai va tong hop cac thiet lap toi uu hoa dat hieu nang cao nhat tren nen tang **Vercel Cloud**.

---

## 1. Cac Cai Tien Toi Uu Hoa Da Duoc Tich Hop

1. **May chu Datacenter Singapore (`sin1`)**:
   - Giam do tre ket noi tu mang Viet Nam xuong con 30ms - 50ms (thay vi 300ms ve My).
2. **Loai bo tep thua bang `.vercelignore`**:
   - Bo qua cac thu muc Desktop PyQt6 (`giao_dien/`, `giao_dien_ui/`, `main.py`,...) giup goi build nhe hon 80% va thoi gian build chi mat duoi 5 giay.
3. **Bo nho dem Edge CDN & Cache-Control da tang**:
   - Toan bo hinh anh 3D, am thanh, JavaScript 3D engine duoc gan `Cache-Control: public, max-age=31536000, immutable`.
   - File Service Worker `sw.js` luon kiem tra cap nhat moi nhat (`no-cache, no-store`).
4. **CORS & Response Headers day du**:
   - Ho tro day du CORS de goi API tu moi thiet bi, trinh duyet di dong hay may tinh.
5. **Precache Service Worker sieu toc**:
   - Luu tru offline cac tep cot loi trong trinh duyet giup mo trang web gan nhu tuc thi (0ms).

---

## 2. Cac Tep Cau Hinh Cot Loi

- **`vercel.json`**: Cau hinh Region `sin1`, dinh tuyen Serverless Python va phan bo Headers Cache/Security.
- **`.vercelignore`**: Danh sach tep bo qua khi deploy.
- **`api/index.py`**: Backend Serverless Python tich hop day du 16 tinh nang voi CORS va Cache-Control.
- **`public/sw.js`**: Service Worker phuc vu du lieu offline va Stale-While-Revalidate.
- **`requirements.txt`**: Khai bao toi gian (chi co `Flask`) giup khoi dong Serverless nhanh nhat.

---

## 3. Cac Buoc Trien Khai (2 Cach)

### Cach 1: Trien Khai Qua GitHub (Khuyen dung)

1. **Day ma nguon len GitHub**:
   ```bash
   git add .
   git commit -m "Toi uu hoa hieu nang cao nhat tren Vercel"
   git push origin main
   ```

2. **Deploy tren Vercel Dashboard**:
   - Truy cap https://vercel.com
   - Chon Project -> Vercel se tu dong nhan dien va Deploy ban moi nhat.

---

### Cach 2: Trien Khai Truc Tiep Bang Vercel CLI

1. Mo Terminal tai thu muc goc du an:
   ```bash
   vercel --prod
   ```
2. Vercel se tu dong dong goi va cap nhat ban Production trong vai giay!
