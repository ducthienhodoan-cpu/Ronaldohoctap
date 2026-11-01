# Thu muc: xu_ly_hoc_tap
# File: quan_ly_chung_nhan.py
# Mo ta: Quan ly va luu tru lich su giay chung nhan hoan thanh bai tap chu de

import json
import os
from datetime import datetime

FILE_CHUNG_NHAN = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "lich_su_chung_nhan.json"))

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
        os.makedirs(os.path.dirname(FILE_CHUNG_NHAN), exist_ok=True)
        with open(FILE_CHUNG_NHAN, "w", encoding="utf-8") as f:
            json.dump(danh_sach, f, ensure_ascii=False, indent=4)
        return True
    except Exception as e:
        print("Loi khi luu giay chung nhan:", e)
        return False

def xep_loai_muc_dat(phan_tram_diem):
    """Xac dinh muc dat duoc dua tren phan tram diem so."""
    try:
        pt = float(phan_tram_diem)
    except Exception:
        pt = 100.0

    if pt >= 90.0:
        return f"Xuất sắc ({pt:.0f}%)"
    elif pt >= 80.0:
        return f"Giỏi ({pt:.0f}%)"
    elif pt >= 65.0:
        return f"Khá ({pt:.0f}%)"
    elif pt >= 50.0:
        return f"Hoàn thành ({pt:.0f}%)"
    else:
        return f"Cần cố gắng ({pt:.0f}%)"

def tao_chung_nhan_moi(ten_hoc_sinh="Học sinh Siêu Club", lop_hoc="THCS", ten_chu_de="Bài kiểm tra", phan_tram_diem=100.0, diem_so=10.0):
    """Tao mot giay chung nhan moi va luu vao lich su (ho tro linh hoat tat ca so luong tham so)."""
    # Xu ly truong hop goi bang 2 tham so tao_chung_nhan_moi(chu_de, diem_so)
    if isinstance(lop_hoc, (int, float)) and ten_chu_de == "Bài kiểm tra":
        diem_so = float(lop_hoc)
        ten_chu_de = str(ten_hoc_sinh)
        phan_tram_diem = diem_so * 10.0 if diem_so <= 10.0 else diem_so
        lop_hoc = "THCS"
        ten_hoc_sinh = "Học sinh Siêu Club"

    muc_dat = xep_loai_muc_dat(phan_tram_diem)
    ngay_cap = datetime.now().strftime("Ngày %d tháng %m năm %Y lúc %H:%M")

    item_chung_nhan = {
        "id": int(datetime.now().timestamp()),
        "ten": str(ten_hoc_sinh),
        "lop": str(lop_hoc),
        "chu_de": str(ten_chu_de),
        "muc_dat": muc_dat,
        "phan_tram": float(phan_tram_diem) if isinstance(phan_tram_diem, (int, float)) else 100.0,
        "diem_so": float(diem_so) if isinstance(diem_so, (int, float)) else 10.0,
        "ngay_cap": ngay_cap
    }

    danh_sach = lay_danh_sach_chung_nhan()
    danh_sach.insert(0, item_chung_nhan)
    luu_danh_sach_chung_nhan(danh_sach)
    return item_chung_nhan
