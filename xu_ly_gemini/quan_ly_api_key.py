# Thu muc: xu_ly_gemini
# File: quan_ly_api_key.py
# Mo ta: Quan ly luu tru, truy xuat va kiem tra tinh hop le cua Gemini API Key sang Tieng Viet co dau

import os
import json

DUONG_DAN_CAU_HINH = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "du_lieu", "cau_hinh_gemini.json"))

def lay_gemini_api_key():
    """Lấy Gemini API Key đã lưu trong file cấu hình JSON."""
    if not os.path.exists(DUONG_DAN_CAU_HINH):
        return ""
    try:
        with open(DUONG_DAN_CAU_HINH, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data.get("api_key", "").strip()
    except Exception:
        return ""

def luu_gemini_api_key(api_key):
    """Lưu Gemini API Key vào file cấu hình JSON."""
    try:
        thu_muc = os.path.dirname(DUONG_DAN_CAU_HINH)
        if not os.path.exists(thu_muc):
            os.makedirs(thu_muc)

        data = {"api_key": api_key.strip()}
        with open(DUONG_DAN_CAU_HINH, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        return True
    except Exception:
        return False

def kiem_tra_api_key_hop_le(api_key):
    """Kiểm tra sơ bộ định dạng chuỗi API Key."""
    if not api_key:
        return False
    api_key_clean = api_key.strip()
    return len(api_key_clean) >= 20
