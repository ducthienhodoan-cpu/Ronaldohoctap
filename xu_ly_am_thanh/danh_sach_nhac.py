# Thu muc: xu_ly_am_thanh
# File: danh_sach_nhac.py
# Mo ta: Danh sach cac bai nhac thu gian va hoc tap tich cuc cho hoc sinh

DANH_SACH_BAI_HAT = [
    {
        "id": "8F2s8ivKXNY",
        "ten": "Oliver Tree - Life Goes On"
    },
    {
        "id": "0GnA8VYOfko",
        "ten": "KITSCHKRIEG ft. BLUMENGARTEN & SHIRIN DAVID - GUT GENUG"
    },
    {
        "id": "pRpeEdMmmQ0",
        "ten": "Shakira - Waka Waka (FIFA World Cup 2010)"
    },
    {
        "id": "7-7knsP2n5w",
        "ten": "Shakira - La La La (Brazil 2014)"
    },
    {
        "id": "IwzkfMmNMpM",
        "ten": "Jung Kook (BTS) - Dreamers (FIFA World Cup 2022)"
    },
    {
        "id": "fcnDmrtj6Sk",
        "ten": "Shakira, Burna Boy - Dai Dai"
    },
    {
        "id": "611WYDonzTU",
        "ten": "Glory Glory Man United (Man United F.C Official Anthem)"
    },
    {
        "id": "ovj8Gb_cVgY",
        "ten": "NO BATIDAO"
    },
    {
        "id": "vrY1THC_NQE",
        "ten": "IShowSpeed - World Cup (Champions)"
    },
    {
        "id": "V1508wboZXk",
        "ten": "Animaniacs SING-ALONG - Yakko's World"
    },
    {
        "id": "QHVWNdYgiWE",
        "ten": "SAO DO DAI CHIEN - Suc manh cua Sao Do 2 | Hau Hoang"
    },
    {
        "id": "1juIFmPyG-Y",
        "ten": "[Nhac che] - SUC MANH CUA SAO DO | Hau Hoang"
    },
    {
        "id": "G79jtUaGRwI",
        "ten": "[Nhac che] - LUN THI SAO? | Hau Hoang ft Nhung Phuong"
    },
    {
        "id": "aoeScCrLFhI",
        "ten": "[Nhac che] - CON DAU GEN Z | Hau Hoang"
    },
    {
        "id": "MxpUcpHjo-o",
        "ten": "[Nhac che] - DAI CHIEN LOP TRUONG | Hau Hoang"
    },
    {
        "id": "ebHMAZu8yhg",
        "ten": "Tet Nha Ba Hoan (Nhac Che Parody) - LEG"
    },
    {
        "id": "fpY1wwXx4Gg",
        "ten": "[Nhac che] - DOI BONG BAT ON | Hau Hoang"
    },
    {
        "id": "0-BzQkDH68E",
        "ten": "Dai thoai Tay Du - Tap 27 - RAP Vo Tri: Me ta thuong mang la..."
    },
    {
        "id": "9E6eup3OSDg",
        "ten": "bai hat TAI SINH theo phong cach TINH SAI"
    }
]

def lay_danh_sach_bai_hat():
    """Tra ve toan bo danh sach bai hat thu gian."""
    return DANH_SACH_BAI_HAT

def lay_bai_hat_theo_chi_so(index):
    """Tra ve thong tin bai hat theo vi tri index."""
    if 0 <= index < len(DANH_SACH_BAI_HAT):
        return DANH_SACH_BAI_HAT[index]
    return DANH_SACH_BAI_HAT[0]
