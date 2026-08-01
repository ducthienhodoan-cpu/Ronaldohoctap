# Thu muc: giao_dien
# File: hop_thoai_chung_nhan.py
# Mo ta: Hop thoai hien thi Giay chung nhan phong cach Roblox Badge Unlocked Tat ca chu mau trang sang ro net

import os
from PyQt6.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QLabel, 
    QPushButton, QFrame, QMessageBox
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap, QIcon

from giao_dien.phoi_mau_qss import lay_qss_giao_dien
from xu_ly_hoc_tap.quan_ly_nguoi_dung import lay_ten_nguoi_dung
from xu_ly_hoc_tap.quan_ly_chung_nhan import tao_chung_nhan_moi

class HopThoaiChungNhan(QDialog):
    """Hộp thoại hiển thị Giấy chứng nhận phong cách Roblox Badge Award với TẤT CẢ CHỮ LÀ CHỮ TRẮNG SÁNG."""

    def __init__(self, parent=None, lop="Lớp 6", chu_de="Số nguyên", phan_tram_diem=100.0, diem_so=10.0):
        super().__init__(parent)
        self.ten_hoc_sinh = lay_ten_nguoi_dung()
        self.lop = lop
        self.chu_de = chu_de
        self.phan_tram_diem = phan_tram_diem
        self.diem_so = diem_so

        # Tạo và lưu chứng nhận vào lịch sử
        self.item_cert = tao_chung_nhan_moi(self.ten_hoc_sinh, self.lop, self.chu_de, self.phan_tram_diem, self.diem_so)

        self.setWindowTitle("ROBLOX BADGE UNLOCKED - GIẤY CHỨNG NHẬN HOÀN THÀNH CHỦ ĐỀ")
        self.resize(660, 530)
        self.setMinimumSize(600, 480)
        self.setStyleSheet(lay_qss_giao_dien())

        # Đường dẫn logo và linh vật Roblox 3D
        self.logo_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "ChatGPT Image 12_02_50 19 thg 5, 2026.png"))
        self.roblox_3d_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "hinh_anh_3d", "roblox_linh_vat_3d.png"))

        if os.path.exists(self.logo_path):
            self.setWindowIcon(QIcon(self.logo_path))

        self.init_ui()

    def init_ui(self):
        layout_chinh = QVBoxLayout(self)
        layout_chinh.setContentsMargins(20, 20, 20, 20)
        layout_chinh.setSpacing(15)

        # Khung Giấy chứng nhận viền Gold Roblox Dark Gaming
        frame_cert = QFrame()
        frame_cert.setStyleSheet(
            "QFrame { "
            "   background-color: #232527; "
            "   border: 3px solid #00A2FF; "
            "   border-radius: 16px; "
            "   padding: 20px; "
            "}"
        )
        cert_layout = QVBoxLayout(frame_cert)
        cert_layout.setContentsMargins(20, 15, 20, 15)
        cert_layout.setSpacing(10)

        # Hiển thị Linh vật Roblox 3D
        if os.path.exists(self.roblox_3d_path):
            pixmap_3d = QPixmap(self.roblox_3d_path).scaled(110, 110, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
            lbl_3d = QLabel()
            lbl_3d.setPixmap(pixmap_3d)
            lbl_3d.setAlignment(Qt.AlignmentFlag.AlignCenter)
            cert_layout.addWidget(lbl_3d)

        # Tiêu đề Giấy chứng nhận Roblox chữ trắng
        lbl_tieu_de = QLabel("ROBLOX BADGE UNLOCKED - GIẤY CHỨNG NHẬN HOÀN THÀNH")
        lbl_tieu_de.setStyleSheet("font-size: 19px; font-weight: bold; color: #FFFFFF; margin-top: 5px;")
        lbl_tieu_de.setAlignment(Qt.AlignmentFlag.AlignCenter)
        cert_layout.addWidget(lbl_tieu_de)

        lbl_sub = QLabel("Hệ thống Siêu Club Roblox trân trọng vinh danh")
        lbl_sub.setStyleSheet("font-size: 14px; color: #FFFFFF; font-style: italic; font-weight: bold;")
        lbl_sub.setAlignment(Qt.AlignmentFlag.AlignCenter)
        cert_layout.addWidget(lbl_sub)

        # 1. TÊN HỌC SINH ROBLOX chữ trắng
        lbl_ten = QLabel(f"Học sinh Roblox: {self.ten_hoc_sinh}")
        lbl_ten.setStyleSheet("font-size: 20px; font-weight: bold; color: #FFFFFF; margin-top: 6px;")
        lbl_ten.setAlignment(Qt.AlignmentFlag.AlignCenter)
        cert_layout.addWidget(lbl_ten)

        # 2. LỚP HỌC chữ trắng
        lbl_lop = QLabel(f"Cấp học / Lớp: {self.lop}")
        lbl_lop.setStyleSheet("font-size: 15px; color: #FFFFFF; font-weight: bold;")
        lbl_lop.setAlignment(Qt.AlignmentFlag.AlignCenter)
        cert_layout.addWidget(lbl_lop)

        # 3. CHỦ ĐỀ BÀI TẬP chữ trắng
        lbl_chu_de = QLabel(f"Đã hoàn thành xuất sắc chủ đề bài tập:\n'{self.chu_de}'")
        lbl_chu_de.setStyleSheet("font-size: 16px; color: #FFFFFF; font-weight: bold; line-height: 1.4;")
        lbl_chu_de.setAlignment(Qt.AlignmentFlag.AlignCenter)
        lbl_chu_de.setWordWrap(True)
        cert_layout.addWidget(lbl_chu_de)

        # 4. MỨC ĐẠT ROBLOX chữ trắng
        lbl_muc_dat = QLabel(f"Mức đạt: {self.item_cert['muc_dat']}")
        lbl_muc_dat.setStyleSheet("font-size: 16px; font-weight: bold; color: #FFFFFF; background-color: #111214; padding: 6px 16px; border-radius: 12px; border: 2px solid #00A2FF;")
        lbl_muc_dat.setAlignment(Qt.AlignmentFlag.AlignCenter)
        cert_layout.addWidget(lbl_muc_dat)

        # Ngày cấp & Đơn vị chữ trắng
        lbl_ngay = QLabel(f"{self.item_cert['ngay_cap']} | Roblox Education Council")
        lbl_ngay.setStyleSheet("font-size: 13px; color: #FFFFFF; font-weight: bold; margin-top: 5px;")
        lbl_ngay.setAlignment(Qt.AlignmentFlag.AlignCenter)
        cert_layout.addWidget(lbl_ngay)

        layout_chinh.addWidget(frame_cert)

        # Các nút hành động Roblox Style chữ trắng
        btn_layout = QHBoxLayout()
        btn_luu = QPushButton("Lưu Roblox Badge vào bộ sưu tập")
        btn_luu.setProperty("class", "btn-secondary")
        btn_luu.setStyleSheet("color: #FFFFFF; font-weight: bold;")
        btn_luu.setCursor(Qt.CursorShape.PointingHandCursor)
        btn_luu.clicked.connect(self.luu_thanh_cong)

        btn_dong = QPushButton("Đóng & Tiếp tục chơi và học")
        btn_dong.setProperty("class", "btn-primary")
        btn_dong.setStyleSheet("color: #FFFFFF; font-weight: bold;")
        btn_dong.setCursor(Qt.CursorShape.PointingHandCursor)
        btn_dong.clicked.connect(self.accept)

        btn_layout.addWidget(btn_luu)
        btn_layout.addWidget(btn_dong)
        layout_chinh.addLayout(btn_layout)

    def luu_thanh_cong(self):
        """Thông báo đã lưu chứng nhận vào lịch sử thành tích."""
        QMessageBox.information(self, "Lưu Roblox Badge", "Giấy chứng nhận Roblox Badge đã được lưu vào bộ sưu tập Thành tích của em!")
