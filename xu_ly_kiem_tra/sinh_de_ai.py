# Thu muc: xu_ly_kiem_tra
# File: sinh_de_ai.py
# Mo ta: Thuat toan AI tao de kiem tra ngau nhien tu Gemini API, Internet & JS Engine theo Lop va Chu de sang Tieng Viet co dau

from du_lieu.truy_xuat_internet import tai_cau_hoi_tu_internet
from xu_ly_gemini.dong_co_gemini import tao_de_thi_gemini_api
from xu_ly_gemini.quan_ly_api_key import lay_gemini_api_key

def tao_de_thi_ai(ten_lop="Lớp 7", ten_mon="Toán", ten_chuong="Biểu thức đại số", so_cau=20, muc_do="Trung bình", api_key=""):
    """Tạo đề kiểm tra tự động bằng Gemini API Key hoặc fallback Internet/JS Engine chuẩn Tiếng Việt có dấu."""
    key_su_dung = api_key.strip() if api_key else lay_gemini_api_key()
    
    # 1. Thử sinh bài tập tự động bằng Gemini API nếu có API Key
    if key_su_dung:
        danh_sach_gemini = tao_de_thi_gemini_api(
            ten_lop=ten_lop,
            ten_mon=ten_mon,
            ten_chuong=ten_chuong,
            so_cau=so_cau,
            muc_do=muc_do,
            api_key=key_su_dung
        )
        if danh_sach_gemini:
            return danh_sach_gemini

    # 2. Fallback nếu không có Gemini Key hoặc gọi API không thành công
    danh_sach_de = tai_cau_hoi_tu_internet(ten_mon=ten_mon, ten_lop=ten_lop, ten_chuong=ten_chuong, so_luong=so_cau)
    
    for idx, item in enumerate(danh_sach_de):
        item["cau_so"] = idx + 1
        item["muc_do"] = muc_do

    return danh_sach_de

