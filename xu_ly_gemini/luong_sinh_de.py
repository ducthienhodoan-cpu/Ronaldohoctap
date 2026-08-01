# Thu muc: xu_ly_gemini
# File: luong_sinh_de.py
# Mo ta: Luong chay ngam QThread sinh de kiem tra Gemini AI giup giao dien mượt mà khong bi đơ lag crash sang Tieng Viet co dau

from PyQt6.QtCore import QThread, pyqtSignal
from xu_ly_kiem_tra.sinh_de_ai import tao_de_thi_ai

class LuongSinhDeGemini(QThread):
    """Luồng QThread xử lý tạo đề thi Gemini AI ngầm để tránh đứng app hoặc giật lag giao diện."""

    # Tín hiệu phát về khi hoàn thành hoặc gặp lỗi
    de_thi_da_sinh = pyqtSignal(list, str)  # (danh_sach_de, thong_bao_loi)

    def __init__(self, ten_lop, ten_mon, ten_chuong, so_cau, muc_do, parent=None):
        super().__init__(parent)
        self.ten_lop = ten_lop
        self.ten_mon = ten_mon
        self.ten_chuong = ten_chuong
        self.so_cau = so_cau
        self.muc_do = muc_do

    def run(self):
        """Thực thi sinh đề ngầm trên luồng phụ."""
        try:
            danh_sach_de = tao_de_thi_ai(
                ten_lop=self.ten_lop,
                ten_mon=self.ten_mon,
                ten_chuong=self.ten_chuong,
                so_cau=self.so_cau,
                muc_do=self.muc_do
            )
            if danh_sach_de:
                self.de_thi_da_sinh.emit(danh_sach_de, "")
            else:
                self.de_thi_da_sinh.emit([], "Không thể kết nối Gemini API. Đã tự động dùng dữ liệu mặc định.")
        except Exception as e:
            self.de_thi_da_sinh.emit([], f"Lỗi sinh đề: {str(e)}")
