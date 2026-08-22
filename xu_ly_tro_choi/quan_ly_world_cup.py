# Thu muc: xu_ly_tro_choi
# File: quan_ly_world_cup.py
# Mo ta: Xu ly logic Giai dau World Cup Tri thuc Roblox sang Tieng Viet co dau

import random
from xu_ly_kiem_tra.dong_co_javascript import chay_javascript_sinh_de
from xu_ly_tro_choi.quan_ly_luot_choi import doc_luot_choi_world_cup, luu_luot_choi_world_cup
from xu_ly_tro_choi.quan_ly_vong_bang import lay_danh_sach_doi_thu_vong_bang

def lay_danh_sach_doi_tuyen():
    """Trả về danh sách 8 Đội tuyển Quốc gia tham gia Giải đấu World Cup."""
    return [
        {"id": "vn", "ten": "Việt Nam", "co": "VN", "suc_manh": 95},
        {"id": "br", "ten": "Brazil", "co": "BR", "suc_manh": 92},
        {"id": "ar", "ten": "Argentina", "co": "AR", "suc_manh": 94},
        {"id": "fr", "ten": "Pháp", "co": "FR", "suc_manh": 91},
        {"id": "en", "ten": "Anh", "co": "EN", "suc_manh": 90},
        {"id": "de", "ten": "Đức", "co": "DE", "suc_manh": 89},
        {"id": "jp", "ten": "Nhật Bản", "co": "JP", "suc_manh": 88},
        {"id": "es", "ten": "Tây Ban Nha", "co": "ES", "suc_manh": 91}
    ]

def lay_vong_dau_world_cup(ten_doi_user="Việt Nam", vong_bang_tran_idx=0):
    """Trả về các vòng đấu chính của World Cup với Vòng Bảng 3 trận đấu."""
    tat_ca_doi = [d["ten"] for d in lay_danh_sach_doi_tuyen() if d["ten"] != ten_doi_user]
    random.shuffle(tat_ca_doi)
    
    doi_thu_vb = lay_danh_sach_doi_thu_vong_bang(ten_doi_user, tat_ca_doi)
    doi_thu_v1 = doi_thu_vb[min(vong_bang_tran_idx, len(doi_thu_vb) - 1)]
    
    doi_thu_v2 = tat_ca_doi[1] if len(tat_ca_doi) > 1 else "Đức"
    doi_thu_v3 = tat_ca_doi[2] if len(tat_ca_doi) > 2 else "Brazil"
    doi_thu_v4 = tat_ca_doi[3] if len(tat_ca_doi) > 3 else "Argentina"

    return [
        {"vong": 1, "ten": f"Vòng Bảng World Cup (Trận {vong_bang_tran_idx + 1}/3)", "doi_thu": doi_thu_v1, "so_cau": 5, "tran_idx": vong_bang_tran_idx},
        {"vong": 2, "ten": "Vòng Tứ Kết World Cup", "doi_thu": doi_thu_v2, "so_cau": 5},
        {"vong": 3, "ten": "Vòng Bán Kết World Cup", "doi_thu": doi_thu_v3, "so_cau": 5},
        {"vong": 4, "ten": "TRẬN CHUNG KẾT WORLD CUP", "doi_thu": doi_thu_v4, "so_cau": 5}
    ]

def sinh_tran_dau_world_cup(vong_idx, ten_lop="Lớp 6", ten_mon="Toán", ten_doi_user="Việt Nam", vong_bang_tran_idx=0):
    """Sinh bộ câu hỏi sút phạt Penalty cho trận đấu World Cup."""
    vong_list = lay_vong_dau_world_cup(ten_doi_user, vong_bang_tran_idx)
    vong_info = vong_list[min(vong_idx, len(vong_list) - 1)]
    danh_sach_cau_hoi = chay_javascript_sinh_de(ten_lop, ten_mon, f"World Cup {vong_info['ten']}", vong_info["so_cau"])
    return {
        "vong_info": vong_info,
        "cau_hoi": danh_sach_cau_hoi
    }
