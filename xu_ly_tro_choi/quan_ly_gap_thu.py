# Thu muc: xu_ly_tro_choi
# File: quan_ly_gap_thu.py
# Mo ta: Module quan ly logic va ti le thanh cong game Gap Thu tich luy XP cho hoc sinh THCS

import random

# Danh sach cac loai thu bong va ti le thanh cong, diem XP tuong ung
DANH_SACH_THU = [
    {
        "id": "thuong",
        "ten": "Gau Bong Thuong",
        "mo_ta": "Gau bong de thuong, ti le gap thanh cong 75%",
        "ti_le": 75,
        "xp": 50
    },
    {
        "id": "hiem",
        "ten": "Tho Bong Hiem",
        "mo_ta": "Tho bong tinh anh, ti le gap thanh cong 50%",
        "ti_le": 50,
        "xp": 200
    },
    {
        "id": "huyen_thoai",
        "ten": "Rong Bong Huyen Thoai",
        "mo_ta": "Rong bong huyen thoai, ti le gap thanh cong 25%",
        "ti_le": 25,
        "xp": 500
    }
]

def lay_danh_sach_thu():
    """Tra ve danh sach cac loai thu bong trong may gap."""
    return DANH_SACH_THU

def lay_thong_tin_thu(loai_id):
    """Tim va tra ve thong tin cua loai thu bong theo id."""
    for thu in DANH_SACH_THU:
        if thu["id"] == loai_id:
            return thu
    return DANH_SACH_THU[0]

def thuc_hien_gap_thu(loai_id):
    """
    Thuc hien thao tac gap thu bong va kiem tra ket qua ngau nhien theo ti le.
    Tra ve tuple: (thanh_cong: bool, xp_nhan_duoc: int, thong_bao: str)
    """
    thu_info = lay_thong_tin_thu(loai_id)
    ti_le_thanh_cong = thu_info["ti_le"]
    xp_thuong = thu_info["xp"]
    ten_thu = thu_info["ten"]

    # Sinh so ngau nhien tu 1 den 100
    so_may_man = random.randint(1, 100)

    if so_may_man <= ti_le_thanh_cong:
        # Gap thanh cong
        thong_bao = f"Chuc mung em da gap thanh cong {ten_thu}! Nhan ngay +{xp_thuong} XP!"
        return True, xp_thuong, thong_bao
    else:
        # Gap truat
        thong_bao = f"Tay gap bi truat khi gap {ten_thu}. Ti le la {ti_le_thanh_cong}%. Hay thu lai nhe!"
        return False, 0, thong_bao
