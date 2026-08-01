# Thu muc: xu_ly_so_tay
# File: quan_ly_ke_hoach_hoc.py
# Mo ta: Quan ly ke hoach hoc tap hang ngay, tinh chuoi Streak va thuong diem Roblox XP sang Tieng Viet co dau

import os
import json
from datetime import datetime

FILE_KE_HOACH = os.path.join(os.path.dirname(__file__), "..", "du_lieu", "ke_hoach_hoc.json")

def doc_ke_hoach_hoc():
    """Doc du lieu ke hoach hoc tap tu file JSON."""
    file_path = os.path.abspath(FILE_KE_HOACH)
    if not os.path.exists(file_path):
        return {
            "streak_ngay": 5,
            "ngay_cap_nhat_cuoi": datetime.now().strftime("%Y-%m-%d"),
            "danh_sach_muc_tieu": [
                {"id": 1, "noi_dung": "Hoàn thành 1 bài luyện tập Toán Lớp 7", "hoan_thanh": True, "xp": 50},
                {"id": 2, "noi_dung": "Ôn 10 thẻ ghi nhớ Flashcard Tiếng Anh", "hoan_thanh": False, "xp": 30},
                {"id": 3, "noi_dung": "Làm 1 bài thi thử Khoa học tự nhiên", "hoan_thanh": False, "xp": 100}
            ]
        }
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {
            "streak_ngay": 1,
            "ngay_cap_nhat_cuoi": datetime.now().strftime("%Y-%m-%d"),
            "danh_sach_muc_tieu": []
        }

def ghi_ke_hoach_hoc(data):
    """Ghi du lieu ke hoach hoc tap vao file JSON."""
    file_path = os.path.abspath(FILE_KE_HOACH)
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    try:
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        return True
    except Exception:
        return False

def cap_nhat_trang_thai_muc_tieu(muc_tieu_id, trang_thai):
    """Cap nhat trang thai hoan thanh va tinh chuoi Streak."""
    data = doc_ke_hoach_hoc()
    for item in data.get("danh_sach_muc_tieu", []):
        if item.get("id") == muc_tieu_id:
            item["hoan_thanh"] = trang_thai
            break
            
    # Tinh xem tat ca cac muc tieu da hoan thanh chua
    all_done = all(item.get("hoan_thanh", False) for item in data.get("danh_sach_muc_tieu", []))
    if all_done:
        data["streak_ngay"] = data.get("streak_ngay", 0) + 1
        data["ngay_cap_nhat_cuoi"] = datetime.now().strftime("%Y-%m-%d")

    ghi_ke_hoach_hoc(data)
    return data
