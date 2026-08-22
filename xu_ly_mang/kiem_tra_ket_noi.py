# Thu muc: xu_ly_mang
# File: kiem_tra_ket_noi.py
# Mo ta: Module kiem tra ket noi Internet va luong cap nhat trang thai ngam bang QThread

import socket
from PyQt6.QtCore import QThread, pyqtSignal

def kiem_tra_ket_noi_internet(host="8.8.8.8", port=53, timeout=1.0):
    """
    Kiem tra nhanh ket noi Internet qua DNS public Google (8.8.8.8:53).
    Thoi gian cho toi da 1 giay, khong lam treo giao dien nguoi dung.
    Tra ve True neu co internet, False neu ngoai tuyen (offline).
    """
    try:
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
        return True
    except (socket.error, Exception):
        return False

class LuongKiemTraMang(QThread):
    """
    Luong chay ngam trong PyQt6 de dinh ky kiem tra trang thai ket noi mang
    va phat tin hieu mang_thay_doi de giao dien cap nhat tu dong.
    """
    mang_thay_doi = pyqtSignal(bool)

    def __init__(self, chu_ky_giay=10, parent=None):
        super().__init__(parent)
        self.chu_ky_giay = chu_ky_giay
        self.dang_chay = True
        self.trang_thai_truoc = None

    def run(self):
        while self.dang_chay:
            trang_thai_hien_tai = kiem_tra_ket_noi_internet()
            if trang_thai_hien_tai != self.trang_thai_truoc:
                self.trang_thai_truoc = trang_thai_hien_tai
                self.mang_thay_doi.emit(trang_thai_hien_tai)
            self.msleep(self.chu_ky_giay * 1000)

    def dung_luong(self):
        self.dang_chay = False
        self.wait()
