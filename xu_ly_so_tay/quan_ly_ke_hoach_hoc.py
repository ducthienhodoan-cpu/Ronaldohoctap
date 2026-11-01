# Thu muc: xu_ly_so_tay
# File: quan_ly_ke_hoach_hoc.py
# Mo ta: Quan ly ke hoach hoc tap hang ngay, tinh chuoi Streak va thuong diem Roblox XP sang Tieng Viet co dau

import os
import json
from datetime import datetime, date

FILE_KE_HOACH = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "du_lieu", "ke_hoach_hoc.json"))

def doc_ke_hoach_hoc():
    """Doc du lieu ke hoach hoc tap tu file JSON."""
    hom_nay = str(date.today())
    du_lieu_mac_dinh = {
        "streak_ngay": 1,
        "ngay_cap_nhat_cuoi": hom_nay,
        "danh_sach_muc_tieu": [
            {"id": 1, "noi_dung": "Hoàn thành 1 bài luyện tập Toán Lớp 7", "hoan_thanh": False, "xp": 50},
            {"id": 2, "noi_dung": "Ôn 10 thẻ ghi nhớ Flashcard Tiếng Anh", "hoan_thanh": False, "xp": 30},
            {"id": 3, "noi_dung": "Làm 1 bài thi thử Khoa học tự nhiên", "hoan_thanh": False, "xp": 100}
        ]
    }

    if not os.path.exists(FILE_KE_HOACH):
        ghi_ke_hoach_hoc(du_lieu_mac_dinh)
        return du_lieu_mac_dinh

    try:
        with open(FILE_KE_HOACH, "r", encoding="utf-8") as f:
            data = json.load(f)
            # Kiem tra phong thu neu data bi luu thanh list thay vi dict
            if isinstance(data, list):
                du_lieu_mac_dinh["danh_sach_muc_tieu"] = data if len(data) > 0 else du_lieu_mac_dinh["danh_sach_muc_tieu"]
                ghi_ke_hoach_hoc(du_lieu_mac_dinh)
                return du_lieu_mac_dinh
            return data
    except Exception:
        return du_lieu_mac_dinh

def ghi_ke_hoach_hoc(data):
    """Ghi du lieu ke hoach hoc tap vao file JSON."""
    os.makedirs(os.path.dirname(FILE_KE_HOACH), exist_ok=True)
    try:
        with open(FILE_KE_HOACH, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        return True
    except Exception:
        return False

def cap_nhat_trang_thai_muc_tieu(muc_tieu_id, trang_thai):
    """Cap nhat trang thai hoan thanh va tinh chuoi Streak mot cach chinh xac theo ngay."""
    data = doc_ke_hoach_hoc()
    danh_sach = data.get("danh_sach_muc_tieu", [])
    
    for item in danh_sach:
        if item.get("id") == muc_tieu_id:
            item["hoan_thanh"] = bool(trang_thai)
            break

    # Tinh xem tat ca muc tieu da hoan thanh hay chua
    if len(danh_sach) > 0:
        all_done = all(item.get("hoan_thanh", False) for item in danh_sach)
        hom_nay = str(date.today())
        ngay_cuoi = data.get("ngay_cap_nhat_cuoi", "")

        # Chi tang streak 1 lan duy nhat trong ngay khi hoan thanh toan bo
        if all_done and ngay_cuoi != hom_nay:
            data["streak_ngay"] = max(1, data.get("streak_ngay", 0) + 1)
            data["ngay_cap_nhat_cuoi"] = hom_nay

    ghi_ke_hoach_hoc(data)
    return data
