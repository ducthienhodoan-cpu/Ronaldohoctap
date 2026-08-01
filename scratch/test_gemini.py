# Script kiem thu tinh nang Gemini API tao de thi theo do kho va mon tu nhap

import sys
import os

sys.stdout.reconfigure(encoding='utf-8')
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from xu_ly_gemini.quan_ly_api_key import lay_gemini_api_key, luu_gemini_api_key, kiem_tra_api_key_hop_le
from xu_ly_kiem_tra.sinh_de_ai import tao_de_thi_ai

def chay_kiem_thu():
    print("=== TESTCASE 1: Kiem tra doc luu API Key ===")
    api_hien_tai = lay_gemini_api_key()
    print(f"API Key hien tai: '{api_hien_tai}'")
    
    print("\n=== TESTCASE 2: Sinh de thi voi Mon tu nhap ('Lich su the gioi') & Do kho ('Kho') ===")
    de_lich_su = tao_de_thi_ai(
        ten_lop="Lớp 9",
        ten_mon="Lịch sử thế giới",
        ten_chuong="Cách mạng công nghiệp",
        so_cau=3,
        muc_do="Khó"
    )
    print(f"So cau sinh duoc: {len(de_lich_su)}")
    if de_lich_su:
        cau_1 = de_lich_su[0]
        print(f"Cau 1: {cau_1.get('cau_hoi')}")
        print(f"Dap an: {cau_1.get('dap_an')}")
        print(f"Dap an dung: {cau_1.get('dap_an_dung')}")
        print(f"Nguon: {cau_1.get('nguon')}")

    print("\n=== TESTCASE 3: Sinh de thi voi Mon tu nhap ('Tieng Nhat') & Do kho ('Nang cao') ===")
    de_tieng_nhat = tao_de_thi_ai(
        ten_lop="Lớp 8",
        ten_mon="Tiếng Nhật",
        ten_chuong="Bảng chữ cái Hiragana",
        so_cau=2,
        muc_do="Nâng cao"
    )
    print(f"So cau sinh duoc: {len(de_tieng_nhat)}")
    if de_tieng_nhat:
        print(f"Cau 1: {de_tieng_nhat[0].get('cau_hoi')}")

    print("\n=== KIEM THU BAN BAN THANH CONG ===")

if __name__ == "__main__":
    chay_kiem_thu()
