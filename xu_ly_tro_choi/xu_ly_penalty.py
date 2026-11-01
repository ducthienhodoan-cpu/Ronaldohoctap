# Thu muc: xu_ly_tro_choi
# File: xu_ly_penalty.py
# Mo ta: Logic xu ly tinh huong sut phat Penalty (Ghi ban ngau nhien goc sut, 50% Sut len troi, 50% Thu mon can pha)

import random
from xu_ly_hoc_tap.he_thong_thuong import cong_phan_thuong

DANH_SACH_GOC_GHI_BAN = [
    {"id": "cao_trai", "ten": "Góc Cao Trái", "mo_ta": "Bóng găm thẳng vào góc chữ A bên trái khung thành"},
    {"id": "thap_trai", "ten": "Góc Thấp Trái", "mo_ta": "Cú sút chìm hiểm hóc sát cột dọc bên trái"},
    {"id": "cao_phai", "ten": "Góc Cao Phải", "mo_ta": "Cú sút mu lai má xoáy vào góc chữ A bên phải"},
    {"id": "thap_phai", "ten": "Góc Thấp Phải", "mo_ta": "Cú sút sệt căng như kẻ chỉ về góc phải"},
    {"id": "chinh_giua", "ten": "Chính Giữa Khung Thành", "mo_ta": "Cú sút Panenka tinh tế đánh lừa thủ môn vào giữa lưới"}
]

def sinh_ket_qua_penalty(la_tra_loi_dung=True, goc_chi_dinh=None):
    """
    Sinh ket qua cho tinh huong sut Penalty:
    - Neu tra loi DUNG: 100% Ghi ban voi goc sut ngau nhien.
    - Neu tra loi SAI:
      + 50% ti le: Sut len troi (bong bay vot xa ngang).
      + 50% ti le: Thu mon can pha xuat sac.
    """
    if la_tra_loi_dung:
        if goc_chi_dinh:
            goc_info = next((g for g in DANH_SACH_GOC_GHI_BAN if g["id"] == goc_chi_dinh or g["ten"] == goc_chi_dinh), None)
            if not goc_info:
                goc_info = random.choice(DANH_SACH_GOC_GHI_BAN)
        else:
            goc_info = random.choice(DANH_SACH_GOC_GHI_BAN)

        xp_thuong, coin_thuong = cong_phan_thuong(60)
        return {
            "ket_qua": "ghi_ban",
            "la_ban_thang": True,
            "goc_id": goc_info["id"],
            "goc_ten": goc_info["ten"],
            "tieu_de": "VAO OOO! BAN THANG TUYET DEP!",
            "mo_ta": f"Ban thang sieu pham vao {goc_info['ten']}! {goc_info['mo_ta']}.",
            "xp_thuong": xp_thuong,
            "coin_thuong": coin_thuong
        }
    else:
        # Ti le 50% Sut len troi va 50% Thu mon can pha
        if random.random() < 0.50:
            return {
                "ket_qua": "sut_len_troi",
                "la_ban_thang": False,
                "goc_id": "len_troi",
                "goc_ten": "Sut Len Troi",
                "tieu_de": "SUT LEN TROI! BONG BAY VOT XA NGANG!",
                "mo_ta": "Cu sut qua manh dua qua bong bay vot xa ngang len thang khan dai!",
                "xp_thuong": 0,
                "coin_thuong": 0
            }
        else:
            goc_can_pha = random.choice(DANH_SACH_GOC_GHI_BAN)
            return {
                "ket_qua": "thu_mon_can_pha",
                "la_ban_thang": False,
                "goc_id": goc_can_pha["id"],
                "goc_ten": goc_can_pha["ten"],
                "tieu_de": "THU MON CAN PHA XUAT SAC!",
                "mo_ta": f"Thu mon doi phuong da bay nguoi het co ve huong {goc_can_pha['ten']} va day bong ra ngoai!",
                "xp_thuong": 0,
                "coin_thuong": 0
            }
