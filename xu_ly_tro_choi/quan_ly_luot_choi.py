# Thu muc: xu_ly_tro_choi
# File: quan_ly_luot_choi.py
# Mo ta: Module quan ly luu tru luot choi World Cup, Champions League va don dep tien do tam thoi khi thoat ung dung

import os
import json
from PyQt6.QtCore import QDate

PATH_LUOT_WC = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "du_lieu", "luot_choi_world_cup.json"))
PATH_LUOT_CL = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "du_lieu", "luot_choi_champions_league.json"))
PATH_LUOT_OBBY = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "du_lieu", "luot_choi_obby.json"))
PATH_TIEN_DO_OBBY = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "du_lieu", "tien_do_obby.json"))

def lay_so_luot_choi_obby():
    """Doc so luot choi Obby kha dung tu file JSON. Mac dinh bat dau co 1 luot."""
    if not os.path.exists(PATH_LUOT_OBBY):
        return 1
    try:
        with open(PATH_LUOT_OBBY, "r", encoding="utf-8") as f:
            data = json.load(f)
            return max(0, int(data.get("so_luot_obby", 1)))
    except Exception:
        return 1

def them_luot_choi_obby(so_luot=1):
    """Cong them so luot choi Obby khi hoc sinh hoan thanh 1 bai luyen tap."""
    luot_hien_tai = lay_so_luot_choi_obby()
    luot_moi = luot_hien_tai + max(1, int(so_luot))
    try:
        os.makedirs(os.path.dirname(PATH_LUOT_OBBY), exist_ok=True)
        with open(PATH_LUOT_OBBY, "w", encoding="utf-8") as f:
            json.dump({"so_luot_obby": luot_moi}, f, ensure_ascii=False, indent=4)
    except Exception:
        pass
    return luot_moi

def su_dung_luot_choi_obby():
    """Su dung 1 luot choi Obby. Tra ve True neu tru thanh cong, False neu het luot."""
    luot_hien_tai = lay_so_luot_choi_obby()
    if luot_hien_tai <= 0:
        return False
    luot_moi = luot_hien_tai - 1
    try:
        os.makedirs(os.path.dirname(PATH_LUOT_OBBY), exist_ok=True)
        with open(PATH_LUOT_OBBY, "w", encoding="utf-8") as f:
            json.dump({"so_luot_obby": luot_moi}, f, ensure_ascii=False, indent=4)
    except Exception:
        pass
    return True

def doc_luot_choi_world_cup():
    """Doc luot choi World Cup tu file JSON. Reset ve 0 neu sang ngay moi."""
    hom_nay = QDate.currentDate().toString("yyyy-MM-dd")
    if not os.path.exists(PATH_LUOT_WC):
        return {"ngay_choi": hom_nay, "so_luot_hom_nay": 0}
    try:
        with open(PATH_LUOT_WC, "r", encoding="utf-8") as f:
            data = json.load(f)
            if data.get("ngay_choi") != hom_nay:
                return {"ngay_choi": hom_nay, "so_luot_hom_nay": 0}
            return data
    except Exception:
        return {"ngay_choi": hom_nay, "so_luot_hom_nay": 0}

def luu_luot_choi_world_cup(date_str, so_luot):
    """Ghi luot choi World Cup vao file JSON co dinh."""
    try:
        os.makedirs(os.path.dirname(PATH_LUOT_WC), exist_ok=True)
        data = {"ngay_choi": date_str, "so_luot_hom_nay": int(so_luot)}
        with open(PATH_LUOT_WC, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
    except Exception:
        pass

def doc_luot_choi_champions_league():
    """Doc luot choi Champions League tu file JSON. Reset ve 0 neu sang ngay moi."""
    hom_nay = QDate.currentDate().toString("yyyy-MM-dd")
    if not os.path.exists(PATH_LUOT_CL):
        return {"ngay_choi": hom_nay, "so_luot_hom_nay": 0}
    try:
        with open(PATH_LUOT_CL, "r", encoding="utf-8") as f:
            data = json.load(f)
            if data.get("ngay_choi") != hom_nay:
                return {"ngay_choi": hom_nay, "so_luot_hom_nay": 0}
            return data
    except Exception:
        return {"ngay_choi": hom_nay, "so_luot_hom_nay": 0}

def luu_luot_choi_champions_league(date_str, so_luot):
    """Ghi luot choi Champions League vao file JSON co dinh."""
    try:
        os.makedirs(os.path.dirname(PATH_LUOT_CL), exist_ok=True)
        data = {"ngay_choi": date_str, "so_luot_hom_nay": int(so_luot)}
        with open(PATH_LUOT_CL, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
    except Exception:
        pass

def don_dep_tien_do_tam_thoi_khi_thoat():
    """
    KHI THOAT UNG DUNG: Cac thao tac/tien do choi minigame tam thoi se KHONG duoc luu (duoc reset),
    TRU DUY NHAT luot choi Dau truong World Cup va Champions League.
    """
    try:
        # Reset tien do choi tam thoi Obby ve man 1 ban dau khi thoat app
        du_lieu_reset_obby = {
            "man_hien_tai": 1,
            "man_cao_nhat": 1,
            "cores_da_lay": [],
            "hard_mode_unlocked": False
        }
        os.makedirs(os.path.dirname(PATH_TIEN_DO_OBBY), exist_ok=True)
        with open(PATH_TIEN_DO_OBBY, "w", encoding="utf-8") as f:
            json.dump(du_lieu_reset_obby, f, ensure_ascii=False, indent=4)
    except Exception:
        pass
