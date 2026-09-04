# Thu muc: giao_dien
# File: man_hinh_nhac_thu_gian.py
# Mo ta: Man hinh phat nhac thu gian va tiep nang luong khi hoc tap ho tro danh sach bai hat phong phu

from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, 
    QPushButton, QFrame, QSlider, QMessageBox, QComboBox
)
from PyQt6.QtCore import QUrl, Qt
from PyQt6.QtGui import QDesktopServices
from PyQt6.QtWebEngineWidgets import QWebEngineView

from xu_ly_am_thanh.quan_ly_am_thanh import QuanLyAmThanh
from xu_ly_am_thanh.danh_sach_nhac import lay_danh_sach_bai_hat, lay_bai_hat_theo_chi_so
from xu_ly_bao_ve.ngan_sao_chep import tao_trang_web_chong_copy, thiet_lap_ngan_copy_web_view
from xu_ly_mang.kiem_tra_ket_noi import kiem_tra_ket_noi_internet

class ManHinhNhacThuGian(QWidget):
    """Man hinh phat Am Nhac Thu Gian, Nang Luong va May Man."""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.danh_sach_nhac = lay_danh_sach_bai_hat()
        self.vi_tri_bai_hien_tai = 0
        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(15)

        # Tieu de man hinh
        title_label = QLabel("NHAC THU GIAN VA TIEP NANG LUONG HOC TAP TICH CUC")
        title_label.setStyleSheet("font-size: 22px; font-weight: bold; color: #06B6D4;")
        main_layout.addWidget(title_label)

        # Khung dieu khien nhac nen he thong
        card_bg_music = QFrame()
        card_bg_music.setStyleSheet("background-color: #0F172A; border: 2px solid #06B6D4; border-radius: 14px; padding: 10px 15px;")
        layout_bg = QHBoxLayout(card_bg_music)
        
        lbl_bg_title = QLabel("Nhac nen he thong: GUT GENUG")
        lbl_bg_title.setStyleSheet("font-size: 14px; font-weight: bold; color: #00FFCC;")
        
        self.lbl_status = QLabel("Trang thai: Da Tat")
        self.lbl_status.setStyleSheet("color: #E74C3C; font-weight: bold;")

        self.btn_toggle_bg = QPushButton("Bat / Tat Nhac Nen")
        self.btn_toggle_bg.setStyleSheet("background-color: #06B6D4; color: #FFFFFF; font-weight: bold; padding: 6px 14px; border-radius: 6px;")
        self.btn_toggle_bg.setCursor(Qt.CursorShape.PointingHandCursor)
        self.btn_toggle_bg.clicked.connect(self.xu_ly_bat_tat_nhac_nen)

        lbl_vol = QLabel("Am luong:")
        lbl_vol.setStyleSheet("color: #FFFFFF; font-weight: bold;")
        
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

        # Khung chon bai hat trong danh sach 18 bai
        card_selector = QFrame()
        card_selector.setStyleSheet("background-color: #0F172A; border: 2px solid #A855F7; border-radius: 14px; padding: 10px 15px;")
        layout_sel = QHBoxLayout(card_selector)

        lbl_chon = QLabel("Chon bai hat:")
        lbl_chon.setStyleSheet("font-size: 14px; font-weight: bold; color: #FFFFFF;")
        layout_sel.addWidget(lbl_chon)

        self.combo_bai_hat = QComboBox()
        self.combo_bai_hat.setStyleSheet("background-color: #020617; color: #FFFFFF; border: 1.5px solid #06B6D4; border-radius: 8px; padding: 6px 12px; font-weight: bold; font-size: 13px;")
        for i, item in enumerate(self.danh_sach_nhac):
            self.combo_bai_hat.addItem(f"Bai {i+1}/{len(self.danh_sach_nhac)}: {item['ten']}")
        self.combo_bai_hat.currentIndexChanged.connect(self.khi_doi_bai_hat)
        layout_sel.addWidget(self.combo_bai_hat, stretch=1)

        btn_prev = QPushButton("Bai Truoc")
        btn_prev.setStyleSheet("background-color: #A855F7; color: #FFFFFF; font-weight: bold; padding: 6px 14px; border-radius: 8px;")
        btn_prev.setCursor(Qt.CursorShape.PointingHandCursor)
        btn_prev.clicked.connect(self.bai_truoc)
        layout_sel.addWidget(btn_prev)

        btn_next = QPushButton("Bai Sau")
        btn_next.setStyleSheet("background-color: #A855F7; color: #FFFFFF; font-weight: bold; padding: 6px 14px; border-radius: 8px;")
        btn_next.setCursor(Qt.CursorShape.PointingHandCursor)
        btn_next.clicked.connect(self.bai_sau)
        layout_sel.addWidget(btn_next)

        main_layout.addWidget(card_selector)

        # Khung trinh phat video YouTube
        card_widget = QFrame()
        card_widget.setProperty("class", "card-widget")
        card_layout = QVBoxLayout(card_widget)
        card_layout.setContentsMargins(15, 15, 15, 15)
        card_layout.setSpacing(10)

        self.lbl_current_song = QLabel()
        self.lbl_current_song.setStyleSheet("font-size: 15px; font-weight: bold; color: #00FFCC;")
        card_layout.addWidget(self.lbl_current_song)

        self.web_view = QWebEngineView()
        self.web_view.setMinimumHeight(400)
        
        # Ngan context menu sao chep
        thiet_lap_ngan_copy_web_view(self.web_view)

        self.cap_nhat_noi_dung_web_view()
        card_layout.addWidget(self.web_view)

        # Thanh nut bo tro
        btn_layout = QHBoxLayout()
        lbl_info = QLabel("Goi y: Lang nghe am nhac giup tinh than sang khoai va tap trung hoc tap tot hon.")
        lbl_info.setStyleSheet("color: #94A3B8; font-size: 13px;")

        btn_open_browser = QPushButton("Mo tren Trinh duyet")
        btn_open_browser.setStyleSheet("background-color: #2563EB; color: #FFFFFF; font-weight: bold; padding: 8px 16px; border-radius: 8px;")
        btn_open_browser.clicked.connect(self.mo_tren_trinh_duyet)

        btn_reload = QPushButton("Tai lai Trinh phat")
        btn_reload.setStyleSheet("background-color: #10B981; color: #FFFFFF; font-weight: bold; padding: 8px 16px; border-radius: 8px;")
        btn_reload.clicked.connect(self.tai_lai_nhac)

        btn_layout.addWidget(lbl_info)
        btn_layout.addStretch()
        btn_layout.addWidget(btn_reload)
        btn_layout.addWidget(btn_open_browser)

        card_layout.addLayout(btn_layout)
        main_layout.addWidget(card_widget)

    def khi_doi_bai_hat(self, index):
        """Xu ly khi nguoi dung chon bai hat moi tu danh sach."""
        if 0 <= index < len(self.danh_sach_nhac):
            self.vi_tri_bai_hien_tai = index
            self.cap_nhat_noi_dung_web_view()

    def bai_truoc(self):
        """Chuyen sang bai hat lien truoc."""
        new_idx = (self.vi_tri_bai_hien_tai - 1) % len(self.danh_sach_nhac)
        self.combo_bai_hat.setCurrentIndex(new_idx)

    def bai_sau(self):
        """Chuyen sang bai hat ke tiep."""
        new_idx = (self.vi_tri_bai_hien_tai + 1) % len(self.danh_sach_nhac)
        self.combo_bai_hat.setCurrentIndex(new_idx)

    def cap_nhat_noi_dung_web_view(self):
        """Cap nhat giao dien trinh phat YouTube theo bai hat duoc chon."""
        bai = lay_bai_hat_theo_chi_so(self.vi_tri_bai_hien_tai)
        self.lbl_current_song.setText(f"Dang phat: Bai {self.vi_tri_bai_hien_tai + 1}/{len(self.danh_sach_nhac)} - {bai['ten']}")
        
        if kiem_tra_ket_noi_internet():
            video_id = bai["id"]
            iframe_code = f"""<iframe 
                width="100%" height="380"
                src="https://www.youtube.com/embed/{video_id}?autoplay=1&enablejsapi=1" 
                title="{bai['ten']}" 
                frameborder="0" 
                allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" 
                referrerpolicy="strict-origin-when-cross-origin" 
                allowfullscreen>
            </iframe>"""
            embed_html = tao_trang_web_chong_copy(iframe_code)
            self.web_view.setHtml(embed_html, QUrl("https://www.youtube.com"))
        else:
            offline_html = """
            <div style="background-color: #020617; color: #ffffff; height: 360px; display: flex; flex-direction: column; align-items: center; justify-content: center; font-family: sans-serif; border-radius: 12px; text-align: center; padding: 20px;">
                <h2 style="color: #F59E0B; margin-bottom: 10px;">CHE DO NGOAI TUYEN (OFFLINE MODE)</h2>
                <p style="font-size: 15px; max-width: 600px; line-height: 1.6; color: #CBD5E1;">
                    Hien tai thiet bi dang khong co ket noi Internet de phat YouTube online.<br>
                    Ung dung da tu dong bat <b>Nhac nen he thong (Local Audio)</b> de giup em tap trung hoc tap!
                </p>
                <p style="font-size: 14px; color: #10B981; margin-top: 15px; font-weight: bold;">
                    Tat ca bai hoc, cau hoi luyen tap va minigame van hoat dong 100% binh thuong.
                </p>
            </div>
            """
            embed_html = tao_trang_web_chong_copy(offline_html)
            self.web_view.setHtml(embed_html, QUrl("about:blank"))

    def xu_ly_bat_tat_nhac_nen(self):
        """Bat hoac tat nhac nen va cap nhat giao dien."""
        QuanLyAmThanh.get_instance().bat_tat_nhac_nen()
        self.cap_nhat_trang_thai_nhac()

    def thay_doi_am_luong(self, val):
        """Thay doi am luong nhac nen khi keo slider."""
        QuanLyAmThanh.get_instance().dat_am_luong_nhac_nen(val)

    def cap_nhat_trang_thai_nhac(self):
        """Cap nhat nhan trang thai dang phat hay dang tat."""
        dang_phat = QuanLyAmThanh.get_instance().danh_dang_phat_nhac_nen
        ten_bai = QuanLyAmThanh.get_instance().lay_ten_bai_hat_nen()
        if dang_phat:
            self.lbl_status.setText(f"Trang thai: Dang Phat ({ten_bai})")
            self.lbl_status.setStyleSheet("color: #10B981; font-weight: bold;")
        else:
            self.lbl_status.setText("Trang thai: Da Tat")
            self.lbl_status.setStyleSheet("color: #EF4444; font-weight: bold;")

    def mo_tren_trinh_duyet(self):
        """Mo link bai nhac truc tiep tren trinh duyet ngoai."""
        if not kiem_tra_ket_noi_internet():
            QMessageBox.warning(self, "Ngoai tuyen", "Hien tai thiet bi dang khong co ket noi Internet.")
            return
        bai = lay_bai_hat_theo_chi_so(self.vi_tri_bai_hien_tai)
        url = QUrl(f"https://www.youtube.com/watch?v={bai['id']}")
        QDesktopServices.openUrl(url)

    def tai_lai_nhac(self):
        """Tai lai khung trinh phat nhac."""
        self.cap_nhat_noi_dung_web_view()
