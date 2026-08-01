# Thu muc: xu_ly_hoc_tap
# File: quan_ly_nguoi_dung.py
# Mo ta: Quan ly thong tin nguoi dung va ho ten hoc sinh phan mem Sieu Club Hoc Tap

import json
import os
from datetime import date

FILE_NGUOI_DUNG = "thong_tin_nguoi_dung.json"

def lay_thong_tin_nguoi_dung():
    """Doc thong tin nguoi dung tu file JSON local."""
    if not os.path.exists(FILE_NGUOI_DUNG):
        du_lieu_mac_dinh = {
            "ten_nguoi_dung": "",
            "ngay_tao": str(date.today()),
            "cap_do": 2,
            "giai_doan": "THCS"
        }
        luu_thong_tin_nguoi_dung(du_lieu_mac_dinh)
        return du_lieu_mac_dinh

    try:
        with open(FILE_NGUOI_DUNG, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {
            "ten_nguoi_dung": "",
            "ngay_tao": str(date.today()),
            "cap_do": 2,
            "giai_doan": "THCS"
        }

def luu_thong_tin_nguoi_dung(du_lieu):
    """Luu thong tin nguoi dung vao file JSON local."""
    try:
        with open(FILE_NGUOI_DUNG, "w", encoding="utf-8") as f:
            json.dump(du_lieu, f, ensure_ascii=False, indent=4)
        return True
    except Exception as e:
        print("Loi khi luu thong tin nguoi dung:", e)
        return False

def lay_ten_nguoi_dung():
    """Lay ho va ten cua hoc sinh tu file luu truu."""
    du_lieu = lay_thong_tin_nguoi_dung()
    ten = du_lieu.get("ten_nguoi_dung", "").strip()
    if not ten:
        return "Học sinh Siêu Club"
    return ten

def cap_nhat_ten_nguoi_dung(ten_moi):
    """Cap nhat ten moi cho hoc sinh."""
    ten_sach = ten_moi.strip()
    if not ten_sach:
        return False
    
    du_lieu = lay_thong_tin_nguoi_dung()
    du_lieu["ten_nguoi_dung"] = ten_sach
    return luu_thong_tin_nguoi_dung(du_lieu)

def kiem_tra_da_co_ten():
    """Kiem tra xem hoc sinh da dat ten hay chua."""
    du_lieu = lay_thong_tin_nguoi_dung()
    ten = du_lieu.get("ten_nguoi_dung", "").strip()
    return len(ten) > 0
