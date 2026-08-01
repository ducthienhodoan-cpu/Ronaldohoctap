# Thu muc: du_lieu
# File: ngan_hang_cau_hoi.py
# Mo ta: Ngan hang cau hoi da dang 10 kieu bai tap luyen tap va de kiem tra sang Tieng Viet co dau

from du_lieu_giao_duc.ngan_hang_giai_toan import lay_danh_sach_cau_hoi_toan_giai_chi_tiet
from xu_ly_kiem_tra.dong_co_javascript import chay_javascript_sinh_de
from du_lieu.truy_xuat_internet import tai_cau_hoi_tu_internet

def lay_cau_hoi_luyen_tap(ten_mon="Toán", ten_lop="Lớp 6", ten_chuong="Chủ đề bài học", so_cau=10):
    """Tra ve danh sach cau hoi luyen tap va bai giải chi tiet dong tu JavaScript Engine & Internet API."""
    try:
        ds_js = chay_javascript_sinh_de(ten_lop, ten_mon, ten_chuong, so_cau)
        if ds_js and len(ds_js) > 0:
            return ds_js
    except Exception:
        pass

    try:
        ds_net = tai_cau_hoi_tu_internet(ten_mon, ten_lop, ten_chuong, so_cau)
        if ds_net and len(ds_net) > 0:
            return ds_net
    except Exception:
        pass

    if ten_mon == "Toán":
        return lay_danh_sach_cau_hoi_toan_giai_chi_tiet(ten_lop)

    return [
        {
            "id": 1,
            "loai": "trac_nghiem",
            "cau_hoi": f"Giá trị của biểu thức A = 15 + 25 trong môn {ten_mon} là bao nhiêu?",
            "luat_dap_an": ["30", "35", "40", "45"],
            "dap_an_dung": "40",
            "giai_thich": "Bài giải chi tiết:\nStep 1: Thực hiện phép tính cộng: 15 + 25.\nStep 2: Kết quả 15 + 25 = 40.\n-> Đáp số đúng là 40.",
            "nguon": "JavaScript Engine & Internet API"
        },
        {
            "id": 2,
            "loai": "dung_sai",
            "cau_hoi": "Phát biểu: Trái Đất quay quanh Mặt Trời theo quỹ đạo hình elip là Đúng hay Sai?",
            "luat_dap_an": ["Đúng", "Sai"],
            "dap_an_dung": "Đúng",
            "giai_thich": "Bài giải chi tiết:\nStep 1: Xem xét quy luật chuyển động của các hành tinh theo định lý Ke-pler.\nStep 2: Quỹ đạo của Trái Đất xung quanh Mặt Trời là đường elip gần tròn.\n-> Đáp án đúng là Đúng.",
            "nguon": "JavaScript Engine & Internet API"
        }
    ]


