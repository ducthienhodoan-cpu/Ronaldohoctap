# Thu muc: root
# File: main.py
# Mo ta: File khoi chay chinh cua phan mem Sieu Club Hoc Tap tuong tac sang Tieng Viet co dau

import sys
import os

try:
    from PyQt6.QtWebEngineWidgets import QWebEngineView
except ImportError:
    pass

from PyQt6.QtWidgets import QApplication, QMessageBox
from PyQt6.QtCore import Qt

def kiem_tra_thu_vien():
    """Kiem tra cac thu vien phu thuoc truoc khi khoi chay ung dung."""
    try:
        import PyQt6
        import pygame
        import matplotlib
        import requests
    except ImportError as e:
        print(f"Loi thieu thu vien phu thuoc: {e}")
        return False
    return True

def main():
    """Ham main khoi chay ung dung Sieu Club Hoc Tap."""
    if not kiem_tra_thu_vien():
        print("Vui long cai dat day du cac thu vien qua pip: pip install PyQt6 pygame matplotlib requests")
        return

    # Thiét lap ung dung PyQt6
    app = QApplication(sys.argv)
    app.setApplicationName("SIÊU CLUB HỌC TẬP")
    app.setOrganizationName("Siêu Club Education")

    # Import CuaSoChinh tu giao_dien.man_hinh_chinh
    from giao_dien.man_hinh_chinh import CuaSoChinh

    # Khoi tao va hien thi CuaSoChinh Siêu Club Học Tập
    cua_so_chinh = CuaSoChinh()
    cua_so_chinh.show()

    # Vong lap su kien PyQt6
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
