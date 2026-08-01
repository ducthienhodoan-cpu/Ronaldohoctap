# Thu muc: xu_ly_hoc_tap
# File: quan_ly_tien_do.py
# Mo ta: Quan ly tien do hoc tap, mo khoa bai hoc khi dat tren 80% diem va tinh chuoi ngay hoc Streak

import json
import os
from datetime import datetime, date

FILE_TIEN_DO = "tien_do_hoc_tap.json"

def lay_du_lieu_tien_do():
    """Doc du lieu tien do tu file JSON local."""
    if not os.path.exists(FILE_TIEN_DO):
        du_lieu_mac_dinh = {
            "bai_hoc_da_mo": ["Lop 1_Toan_Bai 1", "Lop 6_Toan_So nguyen"],
            "lich_su_diem": [],
            "streak": 1,
            "ngay_hoc_cuoi": str(date.today())
        }
        luu_du_lieu_tien_do(du_lieu_mac_dinh)
        return du_lieu_mac_dinh
    
    try:
        with open(FILE_TIEN_DO, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {
            "bai_hoc_da_mo": ["Lop 1_Toan_Bai 1"],
            "lich_su_diem": [],
            "streak": 1,
            "ngay_hoc_cuoi": str(date.today())
        }

def luu_du_lieu_tien_do(du_lieu):
    """Luu du lieu tien do vao file JSON local."""
    try:
        with open(FILE_TIEN_DO, "w", encoding="utf-8") as f:
            json.dump(du_lieu, f, ensure_ascii=False, indent=4)
    except Exception as e:
        print("Loi khi luu tien do:", e)

def kiem_tra_mo_khoa_bai_hoc(ten_bai, phan_tram_diem):
    """Kiem tra va mo khoa bai hoc tiep theo neu phan tram diem >= 80%."""
    du_lieu = lay_du_lieu_tien_do()
    mo_khoa = False
    
    if phan_tram_diem >= 80.0:
        ten_bai_tiep = f"{ten_bai}_da_mo_khoa"
        if ten_bai_tiep not in du_lieu["bai_hoc_da_mo"]:
            du_lieu["bai_hoc_da_mo"].append(ten_bai_tiep)
            luu_du_lieu_tien_do(du_lieu)
        mo_khoa = True
        
    cap_nhat_streak()
    return mo_khoa

def cap_nhat_streak():
    """Cap nhat chuoi ngay hoc liên tiep (Streak)."""
    du_lieu = lay_du_lieu_tien_do()
    ngay_hom_nay = date.today()
    
    try:
        ngay_cuoi = datetime.strptime(du_lieu.get("ngay_hoc_cuoi", str(ngay_hom_nay)), "%Y-%m-%d").date()
        khoang_cach = (ngay_hom_nay - ngay_cuoi).days
        
        if khoang_cach == 1:
            du_lieu["streak"] += 1
            du_lieu["ngay_hoc_cuoi"] = str(ngay_hom_nay)
        elif khoang_cach > 1:
            du_lieu["streak"] = 1
            du_lieu["ngay_hoc_cuoi"] = str(ngay_hom_nay)
            
        luu_du_lieu_tien_do(du_lieu)
    except Exception:
        pass
    
    return du_lieu.get("streak", 1)
