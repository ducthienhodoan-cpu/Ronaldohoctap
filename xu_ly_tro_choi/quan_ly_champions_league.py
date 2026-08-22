# Thu muc: xu_ly_tro_choi
# File: quan_ly_champions_league.py
# Mo ta: Xu ly logic Giai dau Champions League Tong hop kien thuc 1 Chu de cua 1 Mon hoc sang Tieng Viet co dau

import random
from xu_ly_kiem_tra.dong_co_javascript import chay_javascript_sinh_de
from xu_ly_tro_choi.quan_ly_luot_choi import doc_luot_choi_champions_league, luu_luot_choi_champions_league
from xu_ly_tro_choi.quan_ly_vong_bang import lay_danh_sach_doi_thu_vong_bang

def lay_danh_sach_clb_champions_league():
    """Trả về danh sách 8 Câu lạc bộ hàng đầu Châu Âu tham gia Champions League."""
    return [
        {"id": "rm", "ten": "Real Madrid", "co": "ES", "chi_so": 98},
        {"id": "mc", "ten": "Manchester City", "co": "EN", "chi_so": 97},
        {"id": "barca", "ten": "FC Barcelona", "co": "ES", "chi_so": 96},
        {"id": "bayern", "ten": "Bayern Munich", "co": "DE", "chi_so": 95},
        {"id": "psg", "ten": "Paris Saint-Germain", "co": "FR", "chi_so": 94},
        {"id": "liv", "ten": "Liverpool FC", "co": "EN", "chi_so": 94},
        {"id": "inter", "ten": "Inter Milan", "co": "IT", "chi_so": 93},
        {"id": "ars", "ten": "Arsenal FC", "co": "EN", "chi_so": 93}
    ]

def lay_vong_dau_champions_league(clb_user_ten="Real Madrid", vong_bang_tran_idx=0):
    """Trả về các vòng đấu chính của Cúp C1 Champions League với Vòng Bảng 3 trận đấu."""
    tat_ca_clb = [c["ten"] for c in lay_danh_sach_clb_champions_league() if c["ten"] != clb_user_ten]
    random.shuffle(tat_ca_clb)
    
    clb_vb = lay_danh_sach_doi_thu_vong_bang(clb_user_ten, tat_ca_clb)
    clb_v1 = clb_vb[min(vong_bang_tran_idx, len(clb_vb) - 1)]
    
    clb_v2 = tat_ca_clb[1] if len(tat_ca_clb) > 1 else "FC Barcelona"
    clb_v3 = tat_ca_clb[2] if len(tat_ca_clb) > 2 else "Manchester City"
    clb_v4 = tat_ca_clb[3] if len(tat_ca_clb) > 3 else "Paris Saint-Germain"

    return [
        {"vong": 1, "ten": f"Vòng Bảng Cúp C1 (Trận {vong_bang_tran_idx + 1}/3)", "doi_thu": clb_v1, "so_cau": 5, "tran_idx": vong_bang_tran_idx},
        {"vong": 2, "ten": "Vòng Tứ Kết Cúp C1", "doi_thu": clb_v2, "so_cau": 5},
        {"vong": 3, "ten": "Vòng Bán Kết Cúp C1", "doi_thu": clb_v3, "so_cau": 5},
        {"vong": 4, "ten": "TRẬN CHUNG KẾT CÚP C1 CHAMPIONS LEAGUE", "doi_thu": clb_v4, "so_cau": 5}
    ]

def sinh_tran_dau_champions_league(vong_idx, ten_lop="Lớp 6", ten_mon="Toán", ten_chu_de="Chủ đề 1", clb_user_ten="Real Madrid", vong_bang_tran_idx=0):
    """Sinh bộ câu hỏi sút phạt Penalty cho trận đấu Champions League chuyên biệt theo 1 Chủ đề duy nhất."""
    vong_list = lay_vong_dau_champions_league(clb_user_ten, vong_bang_tran_idx)
    vong_info = vong_list[min(vong_idx, len(vong_list) - 1)]
    danh_sach_cau_hoi = chay_javascript_sinh_de(ten_lop, ten_mon, ten_chu_de, vong_info["so_cau"])
    return {
        "vong_info": vong_info,
        "cau_hoi": danh_sach_cau_hoi
    }
