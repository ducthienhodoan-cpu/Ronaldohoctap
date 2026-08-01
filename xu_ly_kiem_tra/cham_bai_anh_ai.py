# Thu muc: xu_ly_kiem_tra
# File: cham_bai_anh_ai.py
# Mo ta: Bo phan tich cham bai thu cong qua anh quet AI (OCR & phan tich loi sai) sang Tieng Viet co dau

def phan_tich_anh_bai_lam(duong_dan_anh):
    """Giả lập quét ảnh bài làm, nhận diện chữ viết và AI chấm bài chi tiết chuẩn Tiếng Việt có dấu."""
    if not duong_dan_anh:
        return {
            "trang_thai": False,
            "thong_bao": "Chưa chọn đường dẫn hình ảnh bài làm."
        }

    return {
        "trang_thai": True,
        "ten_file": duong_dan_anh,
        "van_ban_nhan_dien": "Kết quả bài làm quét từ hình ảnh:\nCâu 1: 15 + 25 = 40 (Đúng)\nCâu 2: 12 x 4 = 46 (Sai, kết quả đúng là 48)\nCâu 3: Điền từ: 'EduVerse AI' (Đúng)",
        "diem_so": 6.7,
        "so_cau_dung": 2,
        "so_cau_sai": 1,
        "danh_sach_loi_sai": [
            {
                "cau_so": 2,
                "loi": "Phép tính nhân 12 x 4 bị tính nhầm thành 46.",
                "goi_y_dung": "Thực hiện phép tính nhân theo cột dọc: 2 x 4 = 8, 1 x 4 = 4 -> Kết quả đúng là 48."
            }
        ],
        "danh_gia_chung": "Học sinh làm tốt các phép cộng và điền từ, cần chú ý kỹ hơn khi tính phép nhân."
    }
