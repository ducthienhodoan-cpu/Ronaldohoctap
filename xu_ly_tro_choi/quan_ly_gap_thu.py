# Thu muc: xu_ly_tro_choi
# File: quan_ly_gap_thu.py
# Mo ta: Module quan ly logic tro choi Gap Thu voi 1 nut gap duy nhat, ti le rot 30% va ngau nhien 1 trong 3 thu bong

import random

# Danh sach 3 loai thu bong va phan thuong XP
DANH_SACH_THU = [
    {
        "id": "thuong",
        "ten": "Gau Bong Thuong",
        "xp": 50,
        "trong_so": 60
    },
    {
        "id": "hiem",
        "ten": "Tho Bong Hiem",
        "xp": 200,
        "trong_so": 30
    },
    {
        "id": "huyen_thoai",
        "ten": "Rong Bong Huyen Thoai",
        "xp": 500,
        "trong_so": 10
    }
]

def lay_danh_sach_thu():
    """Tra ve danh sach cac loai thu bong trong may gap."""
    return DANH_SACH_THU

def thuc_hien_gap_thu():
    """
    Thuc hien thao tac gap thu bong khi bam nut Gap.
    - Ti le rot: 30%
    - Ti le trung: 70%, ngau nhien nhan duoc 1 trong 3 loai thu bong.
    Tra ve tuple: (thanh_cong: bool, xp_nhan_duoc: int, thong_bao: str, thu_info: dict hoac None)
    """
    so_may_man = random.randint(1, 100)

    # 30% rot tuong ung so_may_man tu 1 den 30
    if so_may_man <= 30:
        thong_bao = "Tiec qua! Tay gap bi truat rot mat thu bong roi. Hay thu lai nhe!"
        return False, 0, thong_bao, None
    else:
        # 70% thanh cong nhan ngau nhien 1 trong 3 thu bong
        danh_sach_id = [t["id"] for t in DANH_SACH_THU]
        trong_so = [t["trong_so"] for t in DANH_SACH_THU]
        thu_id_duoc_chon = random.choices(danh_sach_id, weights=trong_so, k=1)[0]
        
        thu_info = None
        for thu in DANH_SACH_THU:
            if thu["id"] == thu_id_duoc_chon:
                thu_info = thu
                break
        
        ten_thu = thu_info["ten"]
        xp_thuong = thu_info["xp"]
        thong_bao = f"Chuc mung em da gap thanh cong {ten_thu}! Nhan ngay +{xp_thuong} XP!"
        return True, xp_thuong, thong_bao, thu_info

