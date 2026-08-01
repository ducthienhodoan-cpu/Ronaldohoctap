# Thu muc: xu_ly_hoc_tap
# File: quan_ly_chung_nhan.py
# Mo ta: Quan ly va luu tru lich su giay chung nhan hoan thanh bai tap chu de

import json
import os
from datetime import datetime

FILE_CHUNG_NHAN = "lich_su_chung_nhan.json"

def lay_danh_sach_chung_nhan():
    """Doc danh sach giay chung nhan da dat duoc tu file JSON local."""
    if not os.path.exists(FILE_CHUNG_NHAN):
        return []
    try:
        with open(FILE_CHUNG_NHAN, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return []

def luu_danh_sach_chung_nhan(danh_sach):
    """Luu danh sach giay chung nhan vao file JSON local."""
    try:
        with open(FILE_CHUNG_NHAN, "w", encoding="utf-8") as f:
            json.dump(danh_sach, f, ensure_ascii=False, indent=4)
        return True
    except Exception as e:
        print("Loi khi luu giay chung nhan:", e)
        return False

def xep_loai_muc_dat(phan_tram_diem):
    """Xac dinh muc dat duoc dua tren phan tram diem so."""
    if phan_tram_diem >= 90.0:
        return f"Xuất sắc ({phan_tram_diem:.0f}%)"
    elif phan_tram_diem >= 80.0:
        return f"Giỏi ({phan_tram_diem:.0f}%)"
    elif phan_tram_diem >= 65.0:
        return f"Khá ({phan_tram_diem:.0f}%)"
    elif phan_tram_diem >= 50.0:
        return f"Hoàn thành ({phan_tram_diem:.0f}%)"
    else:
        return f"Cần cố gắng ({phan_tram_diem:.0f}%)"

def tao_chung_nhan_moi(ten_hoc_sinh, lop_hoc, ten_chu_de, phan_tram_diem, diem_so=0.0):
    """Tao mot giay chung nhan moi va luu vao lich su."""
    muc_dat = xep_loai_muc_dat(phan_tram_diem)
    ngay_cap = datetime.now().strftime("Ngày %d tháng %m năm %Y lúc %H:%M")

    item_chung_nhan = {
        "id": int(datetime.now().timestamp()),
        "ten": ten_hoc_sinh,
        "lop": lop_hoc,
        "chu_de": ten_chu_de,
        "muc_dat": muc_dat,
        "phan_tram": phan_tram_diem,
        "diem_so": diem_so,
        "ngay_cap": ngay_cap
    }

    danh_sach = lay_danh_sach_chung_nhan()
    danh_sach.insert(0, item_chung_nhan)
    luu_danh_sach_chung_nhan(danh_sach)
    return item_chung_nhan
