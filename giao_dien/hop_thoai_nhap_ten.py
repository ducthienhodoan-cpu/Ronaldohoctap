# Thu muc: giao_dien
# File: hop_thoai_nhap_ten.py
# Mo ta: Hop thoai nhap ho ten hoc sinh phong cach Roblox Character Creation Tat ca chu mau trang sang ro net

import os
from PyQt6.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QLabel, 
    QLineEdit, QPushButton, QFrame, QMessageBox
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap, QIcon

from giao_dien.phoi_mau_qss import lay_qss_giao_dien
from xu_ly_hoc_tap.quan_ly_nguoi_dung import cap_nhat_ten_nguoi_dung, lay_ten_nguoi_dung

class HopThoaiNhapTen(QDialog):
    """Hộp thoại đặt tên Roblox Avatar cho học sinh với TẤT CẢ VĂN BẢN ĐỀU LÀ CHỮ TRẮNG SÁNG."""

    def __init__(self, parent=None, bat_buoc=True):
        super().__init__(parent)
        self.bat_buoc = bat_buoc
        self.setWindowTitle("ROBLOX EDITION - Đặt tên nhân vật Roblox")
        self.resize(520, 440)
        self.setMinimumSize(480, 400)
        self.setStyleSheet(lay_qss_giao_dien())
        
        # Đường dẫn hình ảnh Roblox 3D
        self.logo_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "ChatGPT Image 12_02_50 19 thg 5, 2026.png"))
        self.roblox_3d_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "hinh_anh_3d", "roblox_linh_vat_3d.png"))
        
        if os.path.exists(self.logo_path):
            self.setWindowIcon(QIcon(self.logo_path))

        self.init_ui()

    def init_ui(self):
        layout_chinh = QVBoxLayout(self)
        layout_chinh.setContentsMargins(20, 20, 20, 20)
        layout_chinh.setSpacing(15)

        # Khung Card trung tam Roblox
        card = QFrame()
        card.setProperty("class", "card-widget")
        card_layout = QVBoxLayout(card)
        card_layout.setContentsMargins(20, 20, 20, 20)
        card_layout.setSpacing(12)

        # Hiển thị linh vật 3D Roblox
        if os.path.exists(self.roblox_3d_path):
            pixmap_3d = QPixmap(self.roblox_3d_path).scaled(150, 150, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
            lbl_3d = QLabel()
            lbl_3d.setPixmap(pixmap_3d)
            lbl_3d.setAlignment(Qt.AlignmentFlag.AlignCenter)
            card_layout.addWidget(lbl_3d)

        # Tiêu đề Roblox chữ trắng
        lbl_tieu_de = QLabel("TẠO NHÂN VẬT ROBLOX HỌC SINH")
        lbl_tieu_de.setStyleSheet("font-size: 18px; font-weight: bold; color: #FFFFFF;")
        lbl_tieu_de.setAlignment(Qt.AlignmentFlag.AlignCenter)
        card_layout.addWidget(lbl_tieu_de)

        # Mô tả hướng dẫn chữ trắng
        lbl_mota = QLabel("Nhập họ và tên đầy đủ của em để bắt đầu tham gia thế giới Siêu Club Roblox:")
        lbl_mota.setStyleSheet("font-size: 14px; color: #FFFFFF; font-weight: bold;")
        lbl_mota.setAlignment(Qt.AlignmentFlag.AlignCenter)
        lbl_mota.setWordWrap(True)
        card_layout.addWidget(lbl_mota)

        # Ô nhập tên Roblox chữ trắng
        self.txt_ho_ten = QLineEdit()
        self.txt_ho_ten.setPlaceholderText("Nhập họ tên (Ví dụ: Nguyễn Văn An)...")
        self.txt_ho_ten.setStyleSheet("font-size: 15px; padding: 10px; color: #FFFFFF; font-weight: bold;")
        
        ten_hien_tai = lay_ten_nguoi_dung()
        if ten_hien_tai and ten_hien_tai != "Học sinh Siêu Club":
            self.txt_ho_ten.setText(ten_hien_tai)
            
        self.txt_ho_ten.returnPressed.connect(self.xac_nhan_luu_ten)
        card_layout.addWidget(self.txt_ho_ten)

        # Nhãn thông báo lỗi chữ trắng
        self.lbl_thong_bao_loi = QLabel("")
        self.lbl_thong_bao_loi.setStyleSheet("color: #FFFFFF; font-weight: bold; font-size: 13px;")
        self.lbl_thong_bao_loi.setAlignment(Qt.AlignmentFlag.AlignCenter)
        card_layout.addWidget(self.lbl_thong_bao_loi)

        # Nút xác nhận Roblox Green chữ trắng
        btn_layout = QHBoxLayout()
        self.btn_xac_nhan = QPushButton("XÁC NHẬN ROBLOX & BẮT ĐẦU CHƠI")
        self.btn_xac_nhan.setProperty("class", "btn-primary")
        self.btn_xac_nhan.setStyleSheet("color: #FFFFFF; font-weight: bold;")
        self.btn_xac_nhan.setCursor(Qt.CursorShape.PointingHandCursor)
        self.btn_xac_nhan.clicked.connect(self.xac_nhan_luu_ten)
        btn_layout.addWidget(self.btn_xac_nhan)

        card_layout.addLayout(btn_layout)
        layout_chinh.addWidget(card)

    def xac_nhan_luu_ten(self):
        """Kiểm tra và lưu tên vào hệ thống."""
        ten_nhap = self.txt_ho_ten.text().strip()
        if not ten_nhap:
            self.lbl_thong_bao_loi.setText("Vui lòng nhập tên nhân vật của em trước khi chơi!")
            return

        if cap_nhat_ten_nguoi_dung(ten_nhap):
            self.accept()
        else:
            self.lbl_thong_bao_loi.setText("Lỗi khi lưu tên. Vui lòng thử lại!")

    def reject(self):
        """Không cho phép đóng bằng nút Esc nếu bắt buộc."""
        if self.bat_buoc and not lay_ten_nguoi_dung():
            self.lbl_thong_bao_loi.setText("Em cần đặt tên nhân vật trước khi tham gia ứng dụng!")
            return
        super().reject()
