# Thu muc: xu_ly_tro_choi
# File: quan_ly_dua_xe.py
# Mo ta: Xu ly logic Game Giai Dua Xe Sieu Cap Roblox 3 Muc do voi ty le chinh xac 70/30, 50/50, 30/70 sang Tieng Viet co dau

import random
from xu_ly_kiem_tra.dong_co_javascript import chay_javascript_sinh_de

def khoi_tao_duong_dua_xe(muc_do="Bình thường"):
    """Khởi tạo các tham số mặc định cho giải đua xe siêu cấp theo Mức độ chơi."""
    return {
        "muc_do": muc_do,
        "vi_tri_lan": 1,        # 0: Trái, 1: Giữa, 2: Phải
        "trang_thai_y": 0,       # 0: Bình thường, 1: Đang nhảy (W), 2: Đang chổm/núp (S)
        "so_mang": 3,           # 3 lượt mạng sống
        "quang_duong": 0,       # Tối đa 1000m tới Vạch Đích
        "dich_den": 1000,
        "diem_so": 0,
        "so_hop_qua": 0,
        "tro_choi_ket_thuc": False,
        "tro_choi_thang": False
    }

def sinh_vat_the_duong_dua(mon_hoc="Toán", lop="Lớp 6", muc_do="Bình thường"):
    """Sinh ngẫu nhiên chướng ngại vật hoặc Hộp quà may mắn dựa trên 3 Mức độ với tỷ lệ chính xác:
    - Dễ: 70% Hộp Quà, 30% Chướng Ngại Vật
    - Bình thường: 50% Hộp Quà, 50% Chướng Ngại Vật (50/50)
    - Khó: 30% Hộp Quà, 70% Chướng Ngại Vật
    """
    lan = random.randint(0, 2)
    
    if "Dễ" in muc_do:
        la_hop_qua = random.random() < 0.70
    elif "Khó" in muc_do:
        la_hop_qua = random.random() < 0.30
    else:
        la_hop_qua = random.random() < 0.50

    if la_hop_qua:
        kieu = "hop_qua_may_man"
    else:
        kieu = random.choice(["chong_ngai_thap", "chong_ngai_cao", "chong_ngai_thuong"])

    cau_hoi = None
    if kieu == "hop_qua_may_man":
        ds = chay_javascript_sinh_de(lop, mon_hoc, "Đường Đua Siêu Cấp", 1)
        if ds:
            cau_hoi = ds[0]
            
    return {
        "lan": lan,
        "kieu": kieu,
        "y": -100,
        "cau_hoi": cau_hoi
    }
