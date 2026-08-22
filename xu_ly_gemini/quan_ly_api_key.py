# Thu muc: xu_ly_gemini
# File: quan_ly_api_key.py
# Mo ta: Quan ly luu tru, truy xuat va kiem tra tinh hop le cua Gemini API Key va Model AI

import os
import json

DUONG_DAN_CAU_HINH = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "du_lieu", "cau_hinh_gemini.json"))

DANH_SACH_MODEL_HO_TRO = [
    "gemini-3.6-flash",
    "gemini-3.5-flash",
    "gemini-2.5-flash",
    "gemini-2.0-flash",
    "gemini-1.5-flash",
    "gemini-1.5-pro",
    "gemini-flash-latest"
]

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

def lay_model_gemini():
    """Lấy tên phiên bản Model Gemini AI đã chọn cấu hình."""
    if not os.path.exists(DUONG_DAN_CAU_HINH):
        return "gemini-3.6-flash"
    try:
        with open(DUONG_DAN_CAU_HINH, "r", encoding="utf-8") as f:
            data = json.load(f)
            model_saved = data.get("model_name", "gemini-3.6-flash").strip()
            return model_saved if model_saved else "gemini-3.6-flash"
    except Exception:
        return "gemini-3.6-flash"

def luu_gemini_api_key(api_key, model_name="gemini-3.6-flash"):
    """Lưu Gemini API Key và Model Name vào file cấu hình JSON."""
    try:
        thu_muc = os.path.dirname(DUONG_DAN_CAU_HINH)
        if not os.path.exists(thu_muc):
            os.makedirs(thu_muc)

        data = {
            "api_key": api_key.strip(),
            "model_name": model_name.strip() if model_name else "gemini-3.6-flash"
        }
        with open(DUONG_DAN_CAU_HINH, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        return True
    except Exception:
        return False

def lay_danh_sach_model_ho_tro():
    """Trả về danh sách tất cả các phiên bản Mô hình Gemini AI mới nhất."""
    return DANH_SACH_MODEL_HO_TRO

def kiem_tra_api_key_hop_le(api_key):
    """Kiểm tra sơ bộ định dạng chuỗi API Key."""
    if not api_key:
        return False
    api_key_clean = api_key.strip()
    return len(api_key_clean) >= 20
