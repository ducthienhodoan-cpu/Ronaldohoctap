# Thu muc: giao_dien
# File: man_hinh_chinh.py
# Mo ta: Man hinh chinh ung dung Sieu Club Hoc Tap phong cach Roblox Gaming Edition tich hop Giai Dua Xe Sieu Cap phim A/D/W/S sang Tieng Viet co dau

import os
from PyQt6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
    QLabel, QPushButton, QFrame, QStackedWidget, QScrollArea, QSlider, QMessageBox
)
from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.QtCore import Qt

from giao_dien.phoi_mau_qss import lay_qss_giao_dien
from giao_dien.man_hinh_menu_bat_dau import ManHinhMenuBatDau
from giao_dien.man_hinh_hoc_tap import ManHinhHocTap
from giao_dien.man_hinh_luyen_tap import ManHinhLuyenTap
from giao_dien.man_hinh_kiem_tra import ManHinhKiemTra
from giao_dien.man_hinh_ai_tao_de import ManHinhAITaoDe
from giao_dien.man_hinh_thong_ke import ManHinhThongKe
from giao_dien.man_hinh_thanh_tich import ManHinhThanhTich
from giao_dien.man_hinh_tro_choi import ManHinhTroChoi
from giao_dien.man_hinh_cai_dat import ManHinhCaiDat
from giao_dien.man_hinh_world_cup import ManHinhWorldCup
from giao_dien.man_hinh_champions_league import ManHinhChampionsLeague
from giao_dien.man_hinh_dua_xe import ManHinhDuaXe
from giao_dien.man_hinh_so_tay_cong_thuc import ManHinhSoTayCongThuc
from giao_dien.man_hinh_so_loi_sai import ManHinhSoLoiSai
from giao_dien.man_hinh_ke_hoach_hoc import ManHinhKeHoachHoc
from giao_dien.man_hinh_tap_thi_ielts import ManHinhTapThiIELTS
from giao_dien.man_hinh_obby import ManHinhObby
from giao_dien.hop_thoai_nhap_ten import HopThoaiNhapTen

from xu_ly_hoc_tap.quan_ly_nguoi_dung import lay_ten_nguoi_dung, kiem_tra_da_co_ten
from xu_ly_am_thanh.quan_ly_am_thanh import QuanLyAmThanh
from xu_ly_tro_choi.quan_ly_luot_choi import don_dep_tien_do_tam_thoi_khi_thoat
from xu_ly_mang.kiem_tra_ket_noi import LuongKiemTraMang

class CuaSoChinh(QMainWindow):
    """Cửa sổ chính phần mềm Siêu Club Học Tập tích hợp Màn hình Menu Khởi đầu có nút Bắt đầu và Nút Thoát."""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("SIÊU CLUB HỌC TẬP - Roblox Grand Prix Racing Edition")
        self.resize(1180, 760)
        self.setMinimumSize(900, 600)
        self.setStyleSheet(lay_qss_giao_dien())
        
        # Đường dẫn logo và linh vật Roblox 3D
        self.logo_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "ChatGPT Image 12_02_50 19 thg 5, 2026.png"))
        self.roblox_3d_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "hinh_anh_3d", "roblox_linh_vat_3d.png"))
        
        if os.path.exists(self.logo_path):
            self.setWindowIcon(QIcon(self.logo_path))

        # Kiểm tra và yêu cầu nhập tên ban đầu nếu chưa có tên
        self.kiem_tra_nhap_ten_ban_dau()

        self.init_ui()

        # Khoi tao luong ngam kiem tra mang va cap nhat giao dien
        self.luong_mang = LuongKiemTraMang(chu_ky_giay=10, parent=self)
        self.luong_mang.mang_thay_doi.connect(self.cap_nhat_trang_thai_mang)
        self.luong_mang.start()

        # Phat nhac nen Piano Sunrise tu dong khi mo ung dung
        QuanLyAmThanh.get_instance().phat_nhac_nen()

    def kiem_tra_nhap_ten_ban_dau(self):
        """Hiển thị hộp thoại nhập tên học sinh trước khi vào ứng dụng nếu chưa có tên."""
        if not kiem_tra_da_co_ten():
            dlg = HopThoaiNhapTen(parent=self, bat_buoc=True)
            dlg.exec()

    def init_ui(self):
        main_widget = QWidget()
        self.setCentralWidget(main_widget)

        main_layout = QHBoxLayout(main_widget)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        # 1. Thanh điều hướng Sidebar bên trái phong cách Roblox
        self.sidebar = QFrame()
        self.sidebar.setObjectName("sidebarFrame")
        self.sidebar.setMinimumWidth(220)
        sidebar_layout = QVBoxLayout(self.sidebar)
        sidebar_layout.setContentsMargins(10, 15, 10, 15)
        sidebar_layout.setSpacing(6)

        # Hiển thị thương hiệu Siêu Club Roblox chữ trắng
        lbl_logo = QLabel("SIÊU CLUB ROBLOX")
        lbl_logo.setStyleSheet("font-size: 18px; font-weight: bold; color: #FFFFFF; padding: 6px 10px;")
        sidebar_layout.addWidget(lbl_logo)

        lbl_sub = QLabel("Nền tảng Học tập & Thi thử Lớp 1-12")
        lbl_sub.setStyleSheet("font-size: 12px; color: #FFFFFF; padding-left: 10px; margin-bottom: 8px;")
        lbl_sub.setWordWrap(True)
        sidebar_layout.addWidget(lbl_sub)

        # Các nút điều hướng Roblox chữ trắng bọc trong scroll area
        scroll_sidebar = QScrollArea()
        scroll_sidebar.setWidgetResizable(True)
        scroll_sidebar.setStyleSheet("QScrollArea { border: none; background-color: transparent; }")

        sidebar_content = QWidget()
        sidebar_content_layout = QVBoxLayout(sidebar_content)
        sidebar_content_layout.setContentsMargins(0, 0, 0, 0)
        sidebar_content_layout.setSpacing(6)

        self.nav_buttons = []
        cacc_chuc_nang = [
            ("Menu Khởi Đầu", 0),
            ("Trang chủ Discover", 1),
            ("Nội dung học tập", 2),
            ("Luyện tập Roblox", 3),
            ("Kiểm tra & Thi thử", 4),
            ("AI Tạo đề thi", 5),
            ("Đấu trường World Cup", 6),
            ("Champions League Cúp C1", 7),
            ("Giải Đua Xe Siêu Cấp", 8),
            ("Thống kê tiến độ", 9),
            ("Thành tích & Roblox XP", 10),
            ("Trò chơi & Ứng dụng", 11),
            ("Cài đặt Roblox Avatar", 12),
            ("Sổ tay Công thức", 13),
            ("Sổ Lỗi Sai Bài Khó", 14),
            ("Lịch Học & Streak", 15),
            ("Tập Thi IELTS", 16),
            ("Đấu Trường Obby 100 Màn", 17)
        ]


        for text, index in cacc_chuc_nang:
            btn = QPushButton(text)
            btn.setCheckable(True)
            btn.setProperty("class", "btn-nav")
            btn.setStyleSheet("color: #FFFFFF; font-weight: bold; font-size: 14px; padding: 10px 14px;")
            btn.setCursor(Qt.CursorShape.PointingHandCursor)
            btn.clicked.connect(lambda checked, idx=index: self.chuyen_man_hinh(idx))
            sidebar_content_layout.addWidget(btn)
            self.nav_buttons.append(btn)

        sidebar_content_layout.addStretch()
        scroll_sidebar.setWidget(sidebar_content)
        sidebar_layout.addWidget(scroll_sidebar)

        # Footer sidebar chữ trắng
        lbl_ver = QLabel("Phiên bản Grand Prix 5.0")
        lbl_ver.setStyleSheet("font-size: 12px; color: #FFFFFF; padding-left: 10px;")
        sidebar_layout.addWidget(lbl_ver)

        main_layout.addWidget(self.sidebar)

        # 2. Vùng nội dung bên phải (Header + StackedWidget)
        right_container = QWidget()
        right_layout = QVBoxLayout(right_container)
        right_layout.setContentsMargins(0, 0, 0, 0)
        right_layout.setSpacing(0)

        # Header bar phong cách Roblox Topbar chữ trắng
        self.header = QFrame()
        self.header.setObjectName("headerFrame")
        header_layout = QHBoxLayout(self.header)
        header_layout.setContentsMargins(20, 10, 20, 10)

        self.lbl_header_title = QLabel("Menu Khởi Đầu")
        self.lbl_header_title.setStyleSheet("font-size: 20px; font-weight: bold; color: #FFFFFF;")
        
        # Nhan hien thi trang thai ket noi mang True/False
        self.lbl_trang_thai_mang = QLabel("Kiểm tra kết nối...")
        self.lbl_trang_thai_mang.setStyleSheet("background-color: #333333; color: #FFFFFF; border-radius: 12px; padding: 4px 12px; font-weight: bold; font-size: 13px;")

        ten_hoc_sinh = lay_ten_nguoi_dung()
        self.lbl_user = QLabel(f"Học sinh: {ten_hoc_sinh} | Roblox Level 2")
        self.lbl_user.setStyleSheet("background-color: #002B4D; color: #FFFFFF; border: 2px solid #00A2FF; padding: 6px 16px; border-radius: 14px; font-weight: bold; font-size: 14px;")

        btn_doi_ten_nhanh = QPushButton("Đổi tên Avatar")
        btn_doi_ten_nhanh.setProperty("class", "btn-secondary")
        btn_doi_ten_nhanh.setStyleSheet("color: #FFFFFF; font-weight: bold;")
        btn_doi_ten_nhanh.setCursor(Qt.CursorShape.PointingHandCursor)
        btn_doi_ten_nhanh.clicked.connect(lambda: self.chuyen_man_hinh(12))

        btn_nhac_nen = QPushButton("Bật/Tắt Nhạc nền")
        btn_nhac_nen.setProperty("class", "btn-primary")
        btn_nhac_nen.setStyleSheet("color: #FFFFFF; font-weight: bold; background-color: #00A2FF;")
        btn_nhac_nen.setCursor(Qt.CursorShape.PointingHandCursor)
        btn_nhac_nen.clicked.connect(self.bat_tat_nhac_nen)

        lbl_vol_hdr = QLabel("Âm lượng:")
        lbl_vol_hdr.setStyleSheet("color: #FFFFFF; font-weight: bold; font-size: 13px; margin-left: 8px;")

        self.slider_vol_header = QSlider(Qt.Orientation.Horizontal)
        self.slider_vol_header.setRange(0, 100)
        self.slider_vol_header.setValue(QuanLyAmThanh.get_instance().lay_am_luong_nhac_nen())
        self.slider_vol_header.setFixedWidth(80)
        self.slider_vol_header.setToolTip("Điều chỉnh âm lượng nhạc nền")
        self.slider_vol_header.valueChanged.connect(self.thay_doi_am_luong_header)

        header_layout.addWidget(self.lbl_header_title)
        header_layout.addStretch()
        header_layout.addWidget(self.lbl_trang_thai_mang)
        header_layout.addWidget(self.lbl_user)
        header_layout.addWidget(btn_doi_ten_nhanh)
        header_layout.addWidget(btn_nhac_nen)
        header_layout.addWidget(lbl_vol_hdr)
        header_layout.addWidget(self.slider_vol_header)

        right_layout.addWidget(self.header)

        # QStackedWidget chứa các màn hình
        self.stacked_widget = QStackedWidget()

        # Thêm các màn hình
        self.screen_menu_bat_dau = ManHinhMenuBatDau()
        self.screen_menu_bat_dau.bat_dau_clicked.connect(lambda: self.chuyen_man_hinh(1))
        self.screen_menu_bat_dau.thoat_clicked.connect(self.close)

        self.screen_trang_chu = self.wrap_in_scroll(self.tao_trang_chu_overview())
        self.screen_hoc_tap = ManHinhHocTap()
        self.screen_luyen_tap = ManHinhLuyenTap()
        self.screen_kiem_tra = ManHinhKiemTra()
        self.screen_ai_tao_de = ManHinhAITaoDe()
        self.screen_world_cup = ManHinhWorldCup()
        self.screen_champions_league = ManHinhChampionsLeague()
        self.screen_dua_xe = ManHinhDuaXe()
        self.screen_thong_ke = ManHinhThongKe()
        self.screen_thanh_tich = ManHinhThanhTich()
        self.screen_tro_choi = ManHinhTroChoi()
        self.screen_cai_dat = ManHinhCaiDat()
        self.screen_so_tay = ManHinhSoTayCongThuc()
        self.screen_so_loi_sai = ManHinhSoLoiSai()
        self.screen_ke_hoach = ManHinhKeHoachHoc()
        self.screen_tap_thi_ielts = ManHinhTapThiIELTS()
        self.screen_obby = ManHinhObby()

        self.screen_cai_dat.ten_da_thay_doi.connect(self.cap_nhat_hien_thi_ten)
        self.screen_luyen_tap.yeu_cau_chuyen_obby.connect(lambda: self.chuyen_man_hinh(17))
        self.screen_hoc_tap.yeu_cau_chuyen_obby.connect(lambda: self.chuyen_man_hinh(17))

        self.stacked_widget.addWidget(self.screen_menu_bat_dau)        # 0
        self.stacked_widget.addWidget(self.screen_trang_chu)           # 1
        self.stacked_widget.addWidget(self.screen_hoc_tap)             # 2
        self.stacked_widget.addWidget(self.screen_luyen_tap)           # 3
        self.stacked_widget.addWidget(self.screen_kiem_tra)            # 4
        self.stacked_widget.addWidget(self.screen_ai_tao_de)           # 5
        self.stacked_widget.addWidget(self.screen_world_cup)           # 6
        self.stacked_widget.addWidget(self.screen_champions_league)    # 7
        self.stacked_widget.addWidget(self.screen_dua_xe)              # 8
        self.stacked_widget.addWidget(self.screen_thong_ke)            # 9
        self.stacked_widget.addWidget(self.screen_thanh_tich)          # 10
        self.stacked_widget.addWidget(self.screen_tro_choi)            # 11
        self.stacked_widget.addWidget(self.screen_cai_dat)             # 12
        self.stacked_widget.addWidget(self.screen_so_tay)              # 13
        self.stacked_widget.addWidget(self.screen_so_loi_sai)          # 14
        self.stacked_widget.addWidget(self.screen_ke_hoach)            # 15
        self.stacked_widget.addWidget(self.screen_tap_thi_ielts)       # 16
        self.stacked_widget.addWidget(self.screen_obby)                # 17


        right_layout.addWidget(self.stacked_widget)
        main_layout.addWidget(right_container)

        self.chuyen_man_hinh(0)

    def wrap_in_scroll(self, widget):
        """Bọc widget vào trong QScrollArea để đảm bảo 100% không bị che khuất bất kỳ văn bản hay nút bấm nào."""
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setStyleSheet("QScrollArea { border: none; background-color: transparent; }")
        scroll.setWidget(widget)
        return scroll

    def cap_nhat_hien_thi_ten(self, ten_moi):
        """Cập nhật tên học sinh trên nhãn Header bar ngay lập tức."""
        self.lbl_user.setText(f"Học sinh: {ten_moi} | Roblox Level 2")

    def tao_trang_chu_overview(self):
        """Tạo widget Trang chủ Discover phong cách Roblox Game Tiles với TẤT CẢ VĂN BẢN LÀ CHỮ TRẮNG SÁNG."""
        w = QWidget()
        l = QVBoxLayout(w)
        l.setContentsMargins(20, 20, 20, 20)
        l.setSpacing(15)

        card = QFrame()
        card.setProperty("class", "card-widget")
        cl = QHBoxLayout(card)
        cl.setContentsMargins(20, 20, 20, 20)
        cl.setSpacing(20)

        if os.path.exists(self.roblox_3d_path):
            pixmap_roblox = QPixmap(self.roblox_3d_path).scaled(180, 180, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
            lbl_r3d = QLabel()
            lbl_r3d.setPixmap(pixmap_roblox)
            lbl_r3d.setAlignment(Qt.AlignmentFlag.AlignCenter)
            cl.addWidget(lbl_r3d)

        content_box = QVBoxLayout()
        content_box.setSpacing(10)

        t = QLabel("CHÀO MỪNG EM ĐẾN VỚI SIÊU CLUB HỌC TẬP - GRAND PRIX RACING EDITION")
        t.setStyleSheet("font-size: 20px; font-weight: bold; color: #FFFFFF;")
        t.setWordWrap(True)
        
        desc = QLabel(
            "Hệ thống học tập chuẩn Roblox Gaming giúp em rèn luyện kiến thức Lớp 1 - 12 một cách cực kỳ sinh động:\n"
            "- GIẢI ĐUA XE SIÊU CẤP: Phím A/D điều khiển rẽ làn, W nhảy cao, S núp chổm, ăn Hộp Quà May Mắn nhận thưởng!\n"
            "- CHAMPIONS LEAGUE CÚP C1: Giải đấu tổng hợp toàn diện kiến thức 1 Chủ đề của 1 Môn học!\n"
            "- ĐẤU TRƯỜNG WORLD CUP: Giải đấu Quốc gia tranh Cúp Vàng 3D lộng lẫy.\n"
            "- Hệ thống 10 dạng bài tập tương tác như một Roblox Minigame hấp dẫn."
        )
        desc.setStyleSheet("font-size: 15px; line-height: 1.5; color: #FFFFFF; font-weight: bold;")
        desc.setWordWrap(True)

        content_box.addWidget(t)
        content_box.addWidget(desc)
        cl.addLayout(content_box, 1)
        l.addWidget(card)

        lbl_mode_title = QLabel("CHỌN CHẾ ĐỘ CHƠI VÀ HỌC TẬP (ROBLOX DISCOVER)")
        lbl_mode_title.setStyleSheet("font-size: 17px; font-weight: bold; color: #FFFFFF; margin-top: 10px;")
        l.addWidget(lbl_mode_title)

        grid_frame = QFrame()
        grid_frame.setProperty("class", "card-widget")
        grid_layout = QHBoxLayout(grid_frame)
        grid_layout.setSpacing(15)

        b0 = QPushButton("Giải Đua Xe Siêu Cấp")
        b0.setProperty("class", "btn-primary")
        b0.setStyleSheet("color: #FFFFFF; font-weight: bold; font-size: 15px; background-color: #FF9100;")
        b0.setCursor(Qt.CursorShape.PointingHandCursor)
        b0.clicked.connect(lambda: self.chuyen_man_hinh(7))

        b1 = QPushButton("Champions League Cúp C1")
        b1.setProperty("class", "btn-primary")
        b1.setStyleSheet("color: #FFFFFF; font-weight: bold; font-size: 15px; background-color: #0052A3;")
        b1.setCursor(Qt.CursorShape.PointingHandCursor)
        b1.clicked.connect(lambda: self.chuyen_man_hinh(6))

        b2 = QPushButton("Đấu trường World Cup")
        b2.setProperty("class", "btn-primary")
        b2.setStyleSheet("color: #FFFFFF; font-weight: bold; font-size: 15px; background-color: #007E3E;")
        b2.setCursor(Qt.CursorShape.PointingHandCursor)
        b2.clicked.connect(lambda: self.chuyen_man_hinh(5))

        b3 = QPushButton("Luyện tập Minigame")
        b3.setProperty("class", "btn-success")
        b3.setStyleSheet("color: #FFFFFF; font-weight: bold; font-size: 15px;")
        b3.setCursor(Qt.CursorShape.PointingHandCursor)
        b3.clicked.connect(lambda: self.chuyen_man_hinh(2))

        grid_layout.addWidget(b0)
        grid_layout.addWidget(b1)
        grid_layout.addWidget(b2)
        grid_layout.addWidget(b3)

        l.addWidget(grid_frame)
        l.addStretch()
        return w

    def dung_tat_ca_dong_ho(self):
        """Dừng tất cả đồng hồ đếm ngược khi chuyển màn hình hoặc chọn mục khác."""
        try:
            if hasattr(self, 'screen_hoc_tap') and hasattr(self.screen_hoc_tap, 'timer'):
                self.screen_hoc_tap.timer.stop()
                self.screen_hoc_tap.lbl_dong_ho.setText("Thời gian: Chưa bắt đầu")
            if hasattr(self, 'screen_luyen_tap') and hasattr(self.screen_luyen_tap, 'timer'):
                self.screen_luyen_tap.timer.stop()
                self.screen_luyen_tap.lbl_dong_ho.setText("Thời gian còn lại: Chưa bắt đầu")
            if hasattr(self, 'screen_kiem_tra') and hasattr(self.screen_kiem_tra, 'timer'):
                self.screen_kiem_tra.timer.stop()
                self.screen_kiem_tra.lbl_dong_ho.setText("Thời gian còn lại: Chưa bắt đầu")
            if hasattr(self, 'screen_ai_tao_de') and hasattr(self.screen_ai_tao_de, 'timer'):
                self.screen_ai_tao_de.timer.stop()
                self.screen_ai_tao_de.lbl_dong_ho.setText("Thời gian: Chưa bắt đầu")
            if hasattr(self, 'screen_world_cup') and hasattr(self.screen_world_cup, 'timer'):
                self.screen_world_cup.timer.stop()
                self.screen_world_cup.lbl_timer_wc.setText("Thời gian trận đấu: Chưa bắt đầu")
            if hasattr(self, 'screen_champions_league') and hasattr(self.screen_champions_league, 'timer'):
                self.screen_champions_league.timer.stop()
                self.screen_champions_league.lbl_timer_cl.setText("Thời gian trận đấu: Chưa bắt đầu")
            if hasattr(self, 'screen_tro_choi'):
                if hasattr(self.screen_tro_choi, 'typing_timer'):
                    self.screen_tro_choi.typing_timer.stop()
                if hasattr(self.screen_tro_choi, 'pomo_timer'):
                    self.screen_tro_choi.pomo_timer.stop()
        except Exception:
            pass

    def cap_nhat_trang_thai_mang(self, is_online):
        """Cập nhật giao diện nhãn thể hiện trạng thái kết nối mạng trên thanh Header bar."""
        if is_online:
            self.lbl_trang_thai_mang.setText("Trạng thái: Trực tuyến")
            self.lbl_trang_thai_mang.setStyleSheet("background-color: #007E3E; color: #FFFFFF; border-radius: 12px; padding: 4px 12px; font-weight: bold; font-size: 13px;")
        else:
            self.lbl_trang_thai_mang.setText("Trạng thái: Ngoại tuyến (Offline Mode)")
            self.lbl_trang_thai_mang.setStyleSheet("background-color: #D35400; color: #FFFFFF; border-radius: 12px; padding: 4px 12px; font-weight: bold; font-size: 13px;")

    def closeEvent(self, event):
        """Dừng tất cả đồng hồ, dọn dẹp luồng ngầm và tiến độ tạm thời khi thoát ứng dụng."""
        if hasattr(self, 'luong_mang'):
            self.luong_mang.dung_luong()
        self.dung_tat_ca_dong_ho()
        don_dep_tien_do_tam_thoi_khi_thoat()
        super().closeEvent(event)

    def bat_tat_nhac_nen(self):
        """Bat hoac tat nhac nen khi nguoi dung bam nut Topbar."""
        dang_phat = QuanLyAmThanh.get_instance().bat_tat_nhac_nen()
        ten_bai = QuanLyAmThanh.get_instance().lay_ten_bai_hat_nen()
        thong_bao = f"Đã BẬT nhạc nền thư giãn ({ten_bai})" if dang_phat else f"Đã TẮT nhạc nền thư giãn ({ten_bai})"
        QMessageBox.information(self, "Âm thanh", thong_bao)

    def thay_doi_am_luong_header(self, val):
        """Thay đổi âm lượng trực tiếp từ Topbar header."""
        QuanLyAmThanh.get_instance().dat_am_luong_nhac_nen(val)
        if hasattr(self, 'screen_cai_dat') and hasattr(self.screen_cai_dat, 'slider_am_luong'):
            self.screen_cai_dat.slider_am_luong.setValue(val)
            self.screen_cai_dat.lbl_phan_tram_vol.setText(f"{val}%")

    def chuyen_man_hinh(self, index):
        """Chuyển đổi màn hình và ẩn/hiện Sidebar và Header khi ở Menu Khởi đầu."""
        self.dung_tat_ca_dong_ho()
        self.stacked_widget.setCurrentIndex(index)

        if index == 0:
            if hasattr(self, 'sidebar'):
                self.sidebar.hide()
            if hasattr(self, 'header'):
                self.header.hide()
        else:
            if hasattr(self, 'sidebar'):
                self.sidebar.show()
            if hasattr(self, 'header'):
                self.header.show()

        titles = [
            "Menu Khởi Đầu",
            "Trang chủ Discover (Roblox Edition)",
            "Nội dung học SGK (Lớp 1 - 12)",
            "Luyện tập phân dạng bài tập Roblox",
            "Trung tâm Kiểm tra & Thi thử",
            "AI Tạo đề thi ngẫu nhiên",
            "Đấu trường World Cup Tri thức Roblox",
            "Champions League Cúp C1 Tri thức Roblox",
            "Giải Đua Xe Siêu Cấp Roblox Grand Prix",
            "Thống kê và Biểu đồ tiến độ",
            "Thành tích & Roblox XP Rewards",
            "Trung tâm Trò chơi & Ứng dụng Học tập",
            "Cài đặt Roblox Avatar & Đổi tên",
            "Sổ tay Công thức & Khái niệm Trọng tâm SGK",
            "Sổ Lỗi Sai & Ôn Lại Bài Khó (Mistake Notebook)",
            "Lịch Học Tập & Nhắc Nhở Mục Tiêu (Roblox Streak)",
            "Tập Thi IELTS Tiếng Anh",
            "Đấu Trường Obby 100 Màn Parkour Glitch World"
        ]
        
        if 0 <= index < len(titles):
            self.lbl_header_title.setText(titles[index])

        for i, btn in enumerate(self.nav_buttons):
            btn.setChecked(i == index)
        
        if index == 12:
            self.screen_cai_dat.tai_lai_thong_tin()
        elif index == 17:
            if hasattr(self, 'screen_obby'):
                self.screen_obby.tai_lai_ban_do()
