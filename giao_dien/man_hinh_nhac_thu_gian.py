# Thu muc: giao_dien
# File: man_hinh_nhac_thu_gian.py
# Mo ta: Man hinh phat nhac Tich cuc Buoi sang thu gian va tiep nang luong khi hoc tap sang Tieng Viet co dau

from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, 
    QPushButton, QFrame, QSlider
)
from PyQt6.QtCore import QUrl, Qt
from PyQt6.QtGui import QDesktopServices
from PyQt6.QtWebEngineWidgets import QWebEngineView

from xu_ly_am_thanh.quan_ly_am_thanh import QuanLyAmThanh
from xu_ly_bao_ve.ngan_sao_chep import tao_trang_web_chong_copy, thiet_lap_ngan_copy_web_view

class ManHinhNhacThuGian(QWidget):
    """Màn hình phát Âm Nhạc Tích Cực Buổi Sáng - Thư Giãn, Năng Lượng, May Mắn & Hạnh Phúc."""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(15)

        # Tiêu đề
        title_label = QLabel("NHẠC THƯ GIÃN VÀ TIẾP NĂNG LƯỢNG HỌC TẬP TÍCH CỰC")
        title_label.setStyleSheet("font-size: 22px; font-weight: bold; color: #2C3E50;")
        main_layout.addWidget(title_label)

        # Khung điều khiển nhạc nền Piano Sunrise
        card_bg_music = QFrame()
        card_bg_music.setStyleSheet("background-color: #EBF5FB; border: 1px solid #AED6F1; border-radius: 10px; padding: 10px 15px;")
        layout_bg = QHBoxLayout(card_bg_music)
        
        lbl_bg_title = QLabel("Nhạc nền hệ thống: Piano Sunrise (Nhạc Piano nhẹ nhàng tập trung)")
        lbl_bg_title.setStyleSheet("font-size: 14px; font-weight: bold; color: #1B4F72;")
        
        self.lbl_status = QLabel("Trạng thái: Đã Tắt")
        self.lbl_status.setStyleSheet("color: #E74C3C; font-weight: bold;")

        self.btn_toggle_bg = QPushButton("Bật / Tắt Nhạc Nền")
        self.btn_toggle_bg.setStyleSheet("background-color: #2980B9; color: #FFFFFF; font-weight: bold; padding: 6px 14px; border-radius: 6px;")
        self.btn_toggle_bg.setCursor(Qt.CursorShape.PointingHandCursor)
        self.btn_toggle_bg.clicked.connect(self.xu_ly_bat_tat_nhac_nen)

        lbl_vol = QLabel("Âm lượng:")
        lbl_vol.setStyleSheet("color: #2C3E50; font-weight: bold;")
        
        self.slider_vol = QSlider(Qt.Orientation.Horizontal)
        self.slider_vol.setRange(0, 100)
        self.slider_vol.setValue(QuanLyAmThanh.get_instance().lay_am_luong_nhac_nen())
        self.slider_vol.setFixedWidth(120)
        self.slider_vol.valueChanged.connect(self.thay_doi_am_luong)

        layout_bg.addWidget(lbl_bg_title)
        layout_bg.addStretch()
        layout_bg.addWidget(self.lbl_status)
        layout_bg.addWidget(self.btn_toggle_bg)
        layout_bg.addWidget(lbl_vol)
        layout_bg.addWidget(self.slider_vol)

        main_layout.addWidget(card_bg_music)
        self.cap_nhat_trang_thai_nhac()

        # Khung chứa trình phát video / nhạc Youtube
        card_widget = QFrame()
        card_widget.setProperty("class", "card-widget")
        card_layout = QVBoxLayout(card_widget)
        card_layout.setContentsMargins(15, 15, 15, 15)
        card_layout.setSpacing(10)

        sub_title = QLabel("Âm Nhạc Tích Cực Buổi Sáng - Thư Giãn, Năng Lượng, May Mắn & Hạnh Phúc")
        sub_title.setStyleSheet("font-size: 16px; font-weight: bold; color: #4A90E2;")
        card_layout.addWidget(sub_title)

        # QWebEngineView để nhúng đoạn mã YouTube mới
        self.web_view = QWebEngineView()
        self.web_view.setMinimumHeight(440)
        
        # Ngăn menu chuột phải (Context Menu) trên QWebEngineView
        thiet_lap_ngan_copy_web_view(self.web_view)

        iframe_code = """<iframe 
            src="https://www.youtube.com/embed/GZKSEAlOZRc?autoplay=1&list=RDGZKSEAlOZRc" 
            title="Âm Nhạc Tích Cực Buổi Sáng | Thư Giãn, Năng Lượng, May Mắn & Hạnh Phúc" 
            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
            allowfullscreen>
        </iframe>"""
        
        # Tạo HTML với đầy đủ tính năng chống copy chữ (CSS user-select:none, JS copy/cut/selectstart listener)
        embed_html = tao_trang_web_chong_copy(iframe_code)
        self.web_view.setHtml(embed_html, QUrl("https://www.youtube.com"))
        card_layout.addWidget(self.web_view)

        # Thanh nút bổ trợ
        btn_layout = QHBoxLayout()
        lbl_info = QLabel("Gợi ý: Lắng nghe âm nhạc tích cực buổi sáng giúp tinh thần sảng khoái và tràn đầy năng lượng.")
        lbl_info.setStyleSheet("color: #7F8C8D; font-size: 13px;")

        btn_open_browser = QPushButton("Mở bài nhạc trên Trình duyệt web")
        btn_open_browser.setProperty("class", "btn-secondary")
        btn_open_browser.clicked.connect(self.mo_tren_trinh_duyet)

        btn_reload = QPushButton("Tải lại Trình phát nhạc")
        btn_reload.setProperty("class", "btn-primary")
        btn_reload.clicked.connect(self.tai_lai_nhac)

        btn_layout.addWidget(lbl_info)
        btn_layout.addStretch()
        btn_layout.addWidget(btn_reload)
        btn_layout.addWidget(btn_open_browser)

        card_layout.addLayout(btn_layout)
        main_layout.addWidget(card_widget)

    def xu_ly_bat_tat_nhac_nen(self):
        """Bat hoac tat nhac nen va cap nhat giao dien."""
        QuanLyAmThanh.get_instance().bat_tat_nhac_nen()
        self.cap_nhat_trang_thai_nhac()

    def thay_doi_am_luong(self, val):
        """Thay doi am luong nhac nen khi kéo slider."""
        QuanLyAmThanh.get_instance().dat_am_luong_nhac_nen(val)

    def cap_nhat_trang_thai_nhac(self):
        """Cap nhat nhan trang thai dang phat hay dang tat."""
        dang_phat = QuanLyAmThanh.get_instance().danh_dang_phat_nhac_nen
        if dang_phat:
            self.lbl_status.setText("Trạng thái: Đang Phát (Piano Sunrise)")
            self.lbl_status.setStyleSheet("color: #27AE60; font-weight: bold;")
        else:
            self.lbl_status.setText("Trạng thái: Đã Tắt")
            self.lbl_status.setStyleSheet("color: #E74C3C; font-weight: bold;")

    def mo_tren_trinh_duyet(self):
        """Mở link bài nhạc tích cực trực tiếp trên trình duyệt ngoài."""
        url = QUrl("https://www.youtube.com/watch?v=GZKSEAlOZRc")
        QDesktopServices.openUrl(url)

    def tai_lai_nhac(self):
        """Tải lại khung trình phát nhạc."""
        self.web_view.reload()
