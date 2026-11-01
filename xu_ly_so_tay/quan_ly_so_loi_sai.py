# Thu muc: xu_ly_so_tay
# File: quan_ly_so_loi_sai.py
# Mo ta: Quan ly luu vet va tai danh sach cac cau hoi lam sai vao file so_loi_sai.json sang Tieng Viet co dau

import os
import json

FILE_SO_LOI_SAI = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "du_lieu", "so_loi_sai.json"))

def doc_so_loi_sai():
    """Doc danh sach cac cau hoi lam sai tu file JSON."""
    if not os.path.exists(FILE_SO_LOI_SAI):
        return []
    try:
        with open(FILE_SO_LOI_SAI, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return []

def ghi_so_loi_sai(danh_sach):
    """Ghi danh sach cau hoi lam sai vao file JSON."""
    os.makedirs(os.path.dirname(FILE_SO_LOI_SAI), exist_ok=True)
    try:
        with open(FILE_SO_LOI_SAI, "w", encoding="utf-8") as f:
            json.dump(danh_sach, f, ensure_ascii=False, indent=2)
        return True
    except Exception:
        return False

def them_cau_loi_sai(cau_hoi_obj_hoac_str, dap_an_chong_sai="", dap_an_dung="", giai_thich=""):
    """Them mot cau hoi hoc sinh lam sai vao so tay loi sai ho tro linh hoat ca dict lan string."""
    danh_sach = doc_so_loi_sai()

    if isinstance(cau_hoi_obj_hoac_str, dict):
        cau_text = str(cau_hoi_obj_hoac_str.get("cau_hoi", "")).strip()
        c_new = dict(cau_hoi_obj_hoac_str)
        c_new["dap_an_da_chon_sai"] = dap_an_chong_sai or c_new.get("dap_an_da_chon_sai", "")
    else:
        cau_text = str(cau_hoi_obj_hoac_str).strip()
        c_new = {
            "cau_hoi": cau_text,
            "dap_an_da_chon_sai": str(dap_an_chong_sai),
            "dap_an_dung": str(dap_an_dung),
            "giai_thich": str(giai_thich) or "Chưa có giải thích chi tiết."
        }

    if not cau_text:
        return False

    for item in danh_sach:
        if str(item.get("cau_hoi", "")).strip() == cau_text:
            return False  # Da ton tai khong luu trung

    danh_sach.append(c_new)
    return ghi_so_loi_sai(danh_sach)

def xoa_cau_loi_sai(cau_text):
    """Xoa mot cau hoi khoi so loi sai khi hoc sinh da lam dung lai."""
    danh_sach = doc_so_loi_sai()
    cau_text_clean = str(cau_text).strip()
    danh_sach_moi = [item for item in danh_sach if str(item.get("cau_hoi", "")).strip() != cau_text_clean]
    return ghi_so_loi_sai(danh_sach_moi)
