# Thu muc: xu_ly_tro_choi
# File: minigame_giua_gio.py
# Mo ta: Bo thuat toan quan ly 3 minigame thu gian giua gio (Lat the ghi nho, Vong quay may man, Sut phat penalty 5 goc) sang Tieng Viet co dau

import random
from xu_ly_hoc_tap.he_thong_thuong import cong_phan_thuong

def tao_danh_sach_the_lat_tri_nho():
    """Tạo 6 cặp thẻ ghi nhớ tri thức và toán học ngẫu nhiên (tổng 12 thẻ)."""
    cac_cap = [
        ("Căn bậc hai của 16", "4"),
        ("Công thức diện tích hình tròn", "S = Pi x R^2"),
        ("Số nguyên tố nhỏ nhất", "2"),
        ("Ngôn ngữ lập trình Python", ".py"),
        ("Đơn vị đo chuẩn của lực", "Newton (N)"),
        ("Chu vi hình chữ nhật", "P = (a + b) x 2")
    ]
    
    the_list = []
    for pair_id, (mat_a, mat_b) in enumerate(cac_cap):
        the_list.append({"pair_id": pair_id, "text": mat_a})
        the_list.append({"pair_id": pair_id, "text": mat_b})

    random.shuffle(the_list)
    return the_list

def quay_vong_quay_may_man():
    """Quay thưởng vòng quay may mắn nhận ngẫu nhiên XP phần thưởng."""
    cac_phan_thuong = [
        {"ten": "Cộng 50 XP Kinh Nghiệm", "xp": 50},
        {"ten": "Cộng 100 XP Kinh Nghiệm", "xp": 100},
        {"ten": "Cộng 150 XP Kinh Nghiệm", "xp": 150},
        {"ten": "Cộng 200 XP Siêu Phần Thưởng", "xp": 200},
        {"ten": "Huy Hiệu Chăm Chỉ + 80 XP", "xp": 80},
        {"ten": "Ngôi Sao May Mắn + 120 XP", "xp": 120}
    ]
    thuong = random.choice(cac_phan_thuong)
    cong_phan_thuong(thuong["xp"])
    return thuong

def xu_ly_sut_phat_penalty(huong_sut):
    """Xử lý minigame sút phạt penalty 5 góc giải trí chuẩn đồng bộ tên hướng."""
    cac_huong_goc = ["Góc Cao Trái", "Góc Thấp Trái", "Chính Giữa", "Góc Cao Phải", "Góc Thấp Phải"]
    
    # Chuan hoa ten huong neu tu ban cu truyen sang
    mapping_ten = {
        "Trái": "Góc Thấp Trái", "Giữa": "Chính Giữa", "Phải": "Góc Thấp Phải",
        "Trái Trên": "Góc Cao Trái", "Trái Dưới": "Góc Thấp Trái",
        "Phải Trên": "Góc Cao Phải", "Phải Dưới": "Góc Thấp Phải"
    }
    huong_sut_chuan = mapping_ten.get(huong_sut, huong_sut)
    huong_thu_mon_bay = random.choice(cac_huong_goc)
    
    if huong_sut_chuan != huong_thu_mon_bay:
        xp_thuong = 60
        cong_phan_thuong(xp_thuong)
        return {
            "vao": True,
            "huong_thu_mon": huong_thu_mon_bay,
            "thong_bao": f"VÀO OOO! Bạn sút góc '{huong_sut_chuan}', thủ môn bay góc '{huong_thu_mon_bay}'. Nhận ngay +{xp_thuong} XP!"
        }
    else:
        return {
            "vao": False,
            "huong_thu_mon": huong_thu_mon_bay,
            "thong_bao": f"Thủ môn đã đoán đúng góc '{huong_sut_chuan}' và cản phá xuất sắc!"
        }
