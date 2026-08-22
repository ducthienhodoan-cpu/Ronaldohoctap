# Thu muc: xu_ly_tro_choi
# File: quan_ly_reset.py
# Mo ta: Module thuc hien Reset toan bo du lieu hoc tap, luot choi va tien do ve trang thai ban dau

import os
import json
from PyQt6.QtCore import QDate

PATH_DU_LIEU = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "du_lieu"))

def reset_toan_bo_du_lieu():
    """
    Reset tat ca cac tep JSON du lieu trong thu muc du_lieu ve trang thai khoi tao ban dau.
    """
    os.makedirs(PATH_DU_LIEU, exist_ok=True)
    hom_nay = QDate.currentDate().toString("yyyy-MM-dd")

    # 1. Reset luot choi World Cup (ve 0 luot hom nay)
    path_wc = os.path.join(PATH_DU_LIEU, "luot_choi_world_cup.json")
    with open(path_wc, "w", encoding="utf-8") as f:
        json.dump({"ngay_choi": hom_nay, "so_luot_hom_nay": 0}, f, ensure_ascii=False, indent=4)

    # 2. Reset luot choi Champions League (ve 0 luot hom nay)
    path_cl = os.path.join(PATH_DU_LIEU, "luot_choi_champions_league.json")
    with open(path_cl, "w", encoding="utf-8") as f:
        json.dump({"ngay_choi": hom_nay, "so_luot_hom_nay": 0}, f, ensure_ascii=False, indent=4)

    # 3. Reset luot choi Obby (ve 1 luot mac dinh ban dau)
    path_luot_obby = os.path.join(PATH_DU_LIEU, "luot_choi_obby.json")
    with open(path_luot_obby, "w", encoding="utf-8") as f:
        json.dump({"so_luot_obby": 1}, f, ensure_ascii=False, indent=4)

    # 4. Reset tien do Obby (ve Man 1, 0 cores)
    path_tien_do_obby = os.path.join(PATH_DU_LIEU, "tien_do_obby.json")
    data_obby = {
        "man_hien_tai": 1,
        "man_cao_nhat": 1,
        "cores_da_lay": [],
        "hard_mode_unlocked": False
    }
    with open(path_tien_do_obby, "w", encoding="utf-8") as f:
        json.dump(data_obby, f, ensure_ascii=False, indent=4)

    # 5. Reset Ke hoach hoc tập
    path_ke_hoach = os.path.join(PATH_DU_LIEU, "ke_hoach_hoc.json")
    with open(path_ke_hoach, "w", encoding="utf-8") as f:
        json.dump([], f, ensure_ascii=False, indent=4)

    # 6. Reset So loi sai
    path_loi_sai = os.path.join(PATH_DU_LIEU, "so_loi_sai.json")
    with open(path_loi_sai, "w", encoding="utf-8") as f:
        json.dump([], f, ensure_ascii=False, indent=4)

    # 7. Reset Cau hinh diem mong muon (ve 10.0 điểm)
    path_diem = os.path.join(PATH_DU_LIEU, "cau_hinh_diem_mong_muon.json")
    with open(path_diem, "w", encoding="utf-8") as f:
        json.dump({"diem_mong_muon": 10.0}, f, ensure_ascii=False, indent=4)

    return True
