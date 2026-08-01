# Thu muc: xu_ly_cai_dat
# File: quan_ly_diem_mong_muon.py
# Mo ta: Quan ly doc va ghi cau hinh diem so mong muon, Band IELTS Target va muc tieu hoc tap hang ngay sang Tieng Viet co dau

import os
import json

FILE_CAU_HINH = os.path.join(os.path.dirname(__file__), "..", "du_lieu", "cau_hinh_diem_mong_muon.json")

def lay_cai_dat_diem_mong_muon():
    """Lấy cấu hình điểm số mong muốn và Target Band IELTS của học sinh."""
    file_path = os.path.abspath(FILE_CAU_HINH)
    mac_dinh = {
        "diem_mong_muon": "9.0 - 10.0 điểm (Xuất sắc)",
        "band_ielts_mong_muon": "Band 6.5 - 7.0 (Nâng cao)",
        "thoi_gian_hoc_ngay": "45 Phút / Ngày"
    }
    if not os.path.exists(file_path):
        luu_cai_dat_diem_mong_muon(mac_dinh)
        return mac_dinh
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data
    except Exception:
        return mac_dinh

def luu_cai_dat_diem_mong_muon(data):
    """Lưu cấu hình điểm mong muốn vào file JSON."""
    file_path = os.path.abspath(FILE_CAU_HINH)
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    try:
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        return True
    except Exception as e:
        print("Lỗi khi lưu cài đặt điểm mong muốn:", e)
        return False
