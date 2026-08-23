# File: xu_ly_tro_choi/quan_ly_vong_quay.py
# Mo ta: Xu ly thuat toan Vong Quay May Man Super Lucky Wheel 10 o voi Lucky Meter, Super Spin, Golden Spin va Jackpot

import os
import json
import random
import datetime
from xu_ly_hoc_tap.he_thong_thuong import cong_phan_thuong

DUONG_DAN_VONG_QUAY = os.path.join("du_lieu", "he_thong_vong_quay.json")

# Danh sach 10 o phan thuong mac dinh (Che do Thuong)
DANH_SACH_10_O_THUONG = [
    {"index": 0, "ten": "100 Xu", "loai": "xu", "gia_tri": 100, "rarity": "thuong"},
    {"index": 1, "ten": "250 Xu", "loai": "xu", "gia_tri": 250, "rarity": "thuong"},
    {"index": 2, "ten": "+1 Vé Gắp Thú", "loai": "ve_gap", "gia_tri": 1, "rarity": "thuong"},
    {"index": 3, "ten": "+100 XP", "loai": "xp", "gia_tri": 100, "rarity": "thuong"},
    {"index": 4, "ten": "Mystery Box", "loai": "mystery_box", "gia_tri": 1, "rarity": "hiem"},
    {"index": 5, "ten": "10 Kim Cương", "loai": "kim_cuong", "gia_tri": 10, "rarity": "hiem"},
    {"index": 6, "ten": "Thú Ngẫu Nhiên", "loai": "thu_bong", "gia_tri": 1, "rarity": "hiem"},
    {"index": 7, "ten": "Golden Ticket", "loai": "ve_vang", "gia_tri": 1, "rarity": "sieu_hiem"},
    {"index": 8, "ten": "Skin Đặc Biệt", "loai": "skin", "gia_tri": 1, "rarity": "sieu_hiem"},
    {"index": 9, "ten": "JACKPOT", "loai": "jackpot", "gia_tri": 1, "rarity": "huyen_thoai"}
]

# Danh sach 10 o phan thuong nang cap (Che do SUPER SPIN - Lucky Meter 100%)
DANH_SACH_10_O_SUPER_SPIN = [
    {"index": 0, "ten": "500 Xu (Super)", "loai": "xu", "gia_tri": 500, "rarity": "thuong"},
    {"index": 1, "ten": "1.000 Xu (Super)", "loai": "xu", "gia_tri": 1000, "rarity": "thuong"},
    {"index": 2, "ten": "+3 Vé Gắp Thú (Super)", "loai": "ve_gap", "gia_tri": 3, "rarity": "thuong"},
    {"index": 3, "ten": "+300 XP (Super)", "loai": "xp", "gia_tri": 300, "rarity": "thuong"},
    {"index": 4, "ten": "Super Mystery Box", "loai": "super_mystery_box", "gia_tri": 1, "rarity": "hiem"},
    {"index": 5, "ten": "30 Kim Cương", "loai": "kim_cuong", "gia_tri": 30, "rarity": "hiem"},
    {"index": 6, "ten": "Thú Hiếm Đặc Biệt", "loai": "thu_bong", "gia_tri": 1, "rarity": "hiem"},
    {"index": 7, "ten": "2 Golden Tickets", "loai": "ve_vang", "gia_tri": 2, "rarity": "sieu_hiem"},
    {"index": 8, "ten": "Skin Siêu Cấp", "loai": "skin", "gia_tri": 1, "rarity": "sieu_hiem"},
    {"index": 9, "ten": "JACKPOT SIÊU CẤP", "loai": "jackpot", "gia_tri": 1, "rarity": "huyen_thoai"}
]

# Danh sach 10 o phan thuong Hoàng Gia (Che do GOLDEN SPIN - dung 1 Ve Vang)
DANH_SACH_10_O_GOLDEN_SPIN = [
    {"index": 0, "ten": "50 Kim Cương", "loai": "kim_cuong", "gia_tri": 50, "rarity": "hiem"},
    {"index": 1, "ten": "Super Box Hoàng Gia", "loai": "super_mystery_box", "gia_tri": 1, "rarity": "hiem"},
    {"index": 2, "ten": "Thú Bông Hiếm Hoàng Gia", "loai": "thu_bong", "gia_tri": 1, "rarity": "hiem"},
    {"index": 3, "ten": "+500 XP Hoàng Gia", "loai": "xp", "gia_tri": 500, "rarity": "hiem"},
    {"index": 4, "ten": "Skin Hoàng Gia Thần Thoại", "loai": "skin", "gia_tri": 1, "rarity": "sieu_hiem"},
    {"index": 5, "ten": "100 Kim Cương", "loai": "kim_cuong", "gia_tri": 100, "rarity": "sieu_hiem"},
    {"index": 6, "ten": "Mascot Huyền Thoại Golden Cat", "loai": "thu_bong", "gia_tri": 1, "rarity": "sieu_hiem"},
    {"index": 7, "ten": "3 Golden Tickets", "loai": "ve_vang", "gia_tri": 3, "rarity": "sieu_hiem"},
    {"index": 8, "ten": "Secret Mascot Roblox", "loai": "secret", "gia_tri": 1, "rarity": "sieu_hiem"},
    {"index": 9, "ten": "JACKPOT HOÀNG GIA", "loai": "jackpot", "gia_tri": 1, "rarity": "huyen_thoai"}
]

def lay_tuan_hien_tai():
    today = datetime.date.today()
    return f"{today.year}-W{today.isocalendar()[1]}"

def lay_du_lieu_vong_quay():
    """Tải dữ liệu số dư vé quay, Lucky Meter và kho đồ kèm quà tặng 5 vé vàng mỗi tuần."""
    today_str = datetime.date.today().isoformat()
    current_week = lay_tuan_hien_tai()
    if not os.path.exists(DUONG_DAN_VONG_QUAY):
        data_default = {
            "ve_quay": 5,
            "ve_vang": 5,
            "chuoi_quay": 0,
            "lucky_meter_percent": 0,
            "ngay_nhan_ve": today_str,
            "tuan_nhan_ve_vang": current_week,
            "kho_do": []
        }
        luu_du_lieu_vong_quay(data_default)
        return data_default
    try:
        with open(DUONG_DAN_VONG_QUAY, "r", encoding="utf-8") as f:
            data = json.load(f)
            # Quà tặng tuần mới: +5 Vé Vàng miễn phí mỗi tuần
            if data.get("tuan_nhan_ve_vang") != current_week:
                data["ve_vang"] = data.get("ve_vang", 0) + 5
                data["tuan_nhan_ve_vang"] = current_week
                luu_du_lieu_vong_quay(data)
            return data
    except Exception:
        return {
            "ve_quay": 5, "ve_vang": 5, "chuoi_quay": 0,
            "lucky_meter_percent": 0, "ngay_nhan_ve": "", "kho_do": []
        }

def luu_du_lieu_vong_quay(data):
    """Lưu dữ liệu vòng quay vào JSON."""
    try:
        thu_muc = os.path.dirname(DUONG_DAN_VONG_QUAY)
        if not os.path.exists(thu_muc):
            os.makedirs(thu_muc)
        with open(DUONG_DAN_VONG_QUAY, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        return True
    except Exception:
        return False

def thuc_hien_luot_quay_moi(loai_quay="thuong"):
    """
    Xử lý lượt quay Vòng Quay May Mắn 10 Ô:
    - loai_quay: 'thuong', 'super', 'golden'
    """
    data = lay_du_lieu_vong_quay()

    # Kiem tra ve quay
    if loai_quay == "golden":
        if data.get("ve_vang", 0) < 1:
            return False, "Bạn không có đủ VÉ VÀNG! Hãy làm bài đạt điểm 10 hoặc điểm danh 7 ngày để nhận Vé Vàng nhé!", data
        data["ve_vang"] -= 1
    else:
        if data.get("ve_quay", 0) < 1:
            return False, "Bạn đã hết Vé Quay! Hãy hoàn thành 1 bài học để nhận ngay +1 Vé Quay nhé!", data
        data["ve_quay"] -= 1

    # Xac dinh danh sach 10 o thuong
    is_super_spin = (data.get("lucky_meter_percent", 0) >= 100) or (loai_quay == "super")
    if loai_quay == "golden":
        danh_sach_o = DANH_SACH_10_O_GOLDEN_SPIN
    elif is_super_spin:
        danh_sach_o = DANH_SACH_10_O_SUPER_SPIN
    else:
        danh_sach_o = DANH_SACH_10_O_THUONG

    # Roll ngau nhien 10 o (Jackpot 2% loai thuong, 5% super, 10% golden)
    roll = random.random() * 100
    if loai_quay == "golden":
        # Ty le Golden Spin: 100% phan thuong tu Hiem den Jackpot
        if roll < 20: o_idx = 0
        elif roll < 40: o_idx = 1
        elif roll < 55: o_idx = 2
        elif roll < 70: o_idx = 3
        elif roll < 82: o_idx = 4
        elif roll < 90: o_idx = 5
        elif roll < 95: o_idx = 6
        elif roll < 98: o_idx = 7
        else: o_idx = 9 # Jackpot Golden
    elif is_super_spin:
        if roll < 25: o_idx = 0
        elif roll < 50: o_idx = 1
        elif roll < 70: o_idx = 2
        elif roll < 85: o_idx = 3
        elif roll < 93: o_idx = 4
        elif roll < 97: o_idx = 5
        else: o_idx = 9 # Jackpot Super
    else:
        if roll < 30: o_idx = 0
        elif roll < 55: o_idx = 1
        elif roll < 75: o_idx = 2
        elif roll < 88: o_idx = 3
        elif roll < 94: o_idx = 4
        elif roll < 97: o_idx = 5
        elif roll < 99: o_idx = 7
        else: o_idx = 9 # Jackpot Thuong

    o_trung = danh_sach_o[o_idx]

    # Cap nhat Lucky Meter (+20% moi luot, neu 100% dung roi thi reset ve 0%)
    if is_super_spin:
        data["lucky_meter_percent"] = 0
    else:
        data["lucky_meter_percent"] = min(100, data.get("lucky_meter_percent", 0) + 20)

    data["chuoi_quay"] = data.get("chuoi_quay", 0) + 1

    # 1. TRUONG HOP JACKPOT: VAO VI VE (+1 VE VANG + 5 VE THUONG) VA CONG TAI KHOAN (+1000 XP)
    if o_trung["loai"] == "jackpot":
        data["ve_vang"] = data.get("ve_vang", 0) + 1
        data["ve_quay"] = data.get("ve_quay", 0) + 5
        from xu_ly_tro_choi.quan_ly_gap_thu_moi import lay_du_lieu_gap_thu, luu_du_lieu_gap_thu
        d_gap = lay_du_lieu_gap_thu()
        d_gap["ve_gap"] = d_gap.get("ve_gap", 0) + 5
        luu_du_lieu_gap_thu(d_gap)
        cong_phan_thuong(1000)

    # 2. PHAN THUONG VE -> CAP NHAT VAO VI VE
    elif o_trung["loai"] == "ve_gap":
        from xu_ly_tro_choi.quan_ly_gap_thu_moi import lay_du_lieu_gap_thu, luu_du_lieu_gap_thu
        d_gap = lay_du_lieu_gap_thu()
        d_gap["ve_gap"] = d_gap.get("ve_gap", 0) + o_trung["gia_tri"]
        luu_du_lieu_gap_thu(d_gap)
    elif o_trung["loai"] == "ve_vang":
        data["ve_vang"] = data.get("ve_vang", 0) + o_trung["gia_tri"]
    elif o_trung["loai"] == "ve_quay":
        data["ve_quay"] = data.get("ve_quay", 0) + o_trung["gia_tri"]

    # 3. PHAN THUONG CON LAI -> CONG TRUC TIEP VAO TAI KHOAN
    elif o_trung["loai"] in ["xp", "xu", "kim_cuong"]:
        cong_phan_thuong(o_trung["gia_tri"])
    
    # Luu vao kho do neu la skin/mascot/jackpot/mystery box
    if o_trung["loai"] in ["skin", "thu_bong", "jackpot", "mystery_box", "super_mystery_box", "secret"]:
        if "kho_do" not in data:
            data["kho_do"] = []
        data["kho_do"].append({
            "ten": o_trung["ten"],
            "loai": o_trung["loai"],
            "ngay_nhan": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })

    luu_du_lieu_vong_quay(data)

    res_payload = {
        "index": o_idx,
        "ten": o_trung["ten"],
        "loai": o_trung["loai"],
        "rarity": o_trung["rarity"],
        "is_jackpot": (o_trung["loai"] == "jackpot"),
        "is_super_spin": is_super_spin,
        "is_golden": (loai_quay == "golden"),
        "lucky_meter": data["lucky_meter_percent"],
        "ve_quay": data["ve_quay"],
        "ve_vang": data["ve_vang"],
        "chuoi_quay": data["chuoi_quay"]
    }

    return True, res_payload, data
