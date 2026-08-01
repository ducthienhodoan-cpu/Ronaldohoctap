# Thu muc: giao_dien
# File: man_hinh_menu_bat_dau.py
# Mo ta: Man hinh Menu Khoi dau phong cach Roblox 3D voi hinh nen welcome, nut Vao ung dung va nut Thoat sang Tieng Viet co dau

import os
from PyQt6.QtWidgets import QWidget, QPushButton
from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtGui import QPixmap, QPainter, QColor
from xu_ly_am_thanh.quan_ly_am_thanh import QuanLyAmThanh

class ManHinhMenuBatDau(QWidget):
    """Màn hình Menu Khởi đầu (Welcome Landing Screen) chỉ giữ nút VÀO ỨNG DỤNG và nút THOÁT."""

    bat_dau_clicked = pyqtSignal()
    thoat_clicked = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.bg_3d_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "hinh_anh_3d", "trang_chao_mung_3d.png"))
        
        # Khởi tạo các nút bấm trung tâm: VÀO ỨNG DỤNG và THOÁT
        self.btn_vao_app = QPushButton(self)
        self.btn_thoat = QPushButton(self)

        self.init_ui()

    def init_ui(self):
        style_hotspot = (
            "QPushButton { "
            "   background-color: transparent; "
            "   border: 2px solid transparent; "
            "   border-radius: 16px; "
            "} "
            "QPushButton:hover { "
            "   background-color: rgba(255, 255, 255, 0.20); "
            "   border: 2px solid rgba(255, 255, 255, 0.7); "
            "} "
            "QPushButton:pressed { "
            "   background-color: rgba(0, 0, 0, 0.25); "
            "}"
        )

        for btn in [self.btn_vao_app, self.btn_thoat]:
            btn.setCursor(Qt.CursorShape.PointingHandCursor)
            btn.setStyleSheet(style_hotspot)

        self.btn_vao_app.clicked.connect(self.xu_ly_vao_ung_dung)
        self.btn_thoat.clicked.connect(self.xu_ly_thoat)

    def paintEvent(self, event):
        """Vẽ hình nền 3D mẫu khớp tràn vừa vặn màn hình."""
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        painter.setRenderHint(QPainter.RenderHint.SmoothPixmapTransform)

        if os.path.exists(self.bg_3d_path):
            pixmap = QPixmap(self.bg_3d_path)
            painter.drawPixmap(self.rect(), pixmap)
        else:
            painter.fillRect(self.rect(), QColor("#001B36"))
        super().paintEvent(event)

    def resizeEvent(self, event):
        """Căn chỉnh vị trí hai nút bấm VÀO ỨNG DỤNG và THOÁT đè chính xác ĐÚNG KHU NÚT GỐC."""
        super().resizeEvent(event)
        w = self.width()
        h = self.height()

        # 1. Nút VÀO ỨNG DỤNG (Khu vực nút xanh lá trung tâm ảnh gốc)
        x_vao = int(w * 0.348)
        y_vao = int(h * 0.468)
        w_vao = int(w * 0.304)
        h_vao = int(h * 0.155)
        self.btn_vao_app.setGeometry(x_vao, y_vao, w_vao, h_vao)

        # 2. Nút THOÁT (Khu vực nút đỏ trung tâm ảnh gốc)
        x_thoat = int(w * 0.375)
        y_thoat = int(h * 0.670)
        w_thoat = int(w * 0.250)
        h_thoat = int(h * 0.138)
        self.btn_thoat.setGeometry(x_thoat, y_thoat, w_thoat, h_thoat)

    def xu_ly_vao_ung_dung(self):
        """Xử lý khi học sinh bấm vào nút VÀO ỨNG DỤNG."""
        QuanLyAmThanh.get_instance().phat_hieu_ung_tra_loi_dung()
        self.bat_dau_clicked.emit()

    def xu_ly_thoat(self):
        """Xử lý khi học sinh bấm vào nút THOÁT."""
        QuanLyAmThanh.get_instance().phat_hieu_ung_dap_an()
        self.thoat_clicked.emit()
