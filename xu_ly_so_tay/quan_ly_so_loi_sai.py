# Thu muc: xu_ly_so_tay
# File: quan_ly_so_loi_sai.py
# Mo ta: Quan ly luu vet va tai danh sach cac cau hoi lam sai vao file so_loi_sai.json sang Tieng Viet co dau

import os
import json

FILE_SO_LOI_SAI = os.path.join(os.path.dirname(__file__), "..", "du_lieu", "so_loi_sai.json")

def doc_so_loi_sai():
    """Doc danh sach cac cau hoi lam sai tu file JSON."""
    file_path = os.path.abspath(FILE_SO_LOI_SAI)
    if not os.path.exists(file_path):
        return []
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return []

def ghi_so_loi_sai(danh_sach):
    """Ghi danh sach cau hoi lam sai vao file JSON."""
    file_path = os.path.abspath(FILE_SO_LOI_SAI)
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    try:
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(danh_sach, f, ensure_ascii=False, indent=2)
        return True
    except Exception:
        return False

def them_cau_loi_sai(cau_hoi_obj, dap_an_chong_sai=""):
    """Them mot cau hoi hoc sinh lam sai vao so tay loi sai."""
    danh_sach = doc_so_loi_sai()
    cau_text = cau_hoi_obj.get("cau_hoi", "")
    
    for item in danh_sach:
        if item.get("cau_hoi") == cau_text:
            return False # Da ton tai
            
    c_new = dict(cau_hoi_obj)
    c_new["dap_an_da_chon_sai"] = dap_an_chong_sai
    danh_sach.append(c_new)
    return ghi_so_loi_sai(danh_sach)

def xoa_cau_loi_sai(cau_text):
    """Xoa mot cau hoi khoi so loi sai khi hoc sinh da lam dung lai."""
    danh_sach = doc_so_loi_sai()
    danh_sach_moi = [item for item in danh_sach if item.get("cau_hoi") != cau_text]
    return ghi_so_loi_sai(danh_sach_moi)
