# Thu muc: giao_dien
# File: hop_thoai_minigame_giua_gio.py
# Mo ta: Hop thoai Dialog Minigame thu gian giua gio (Lat the ghi nho, Vong quay may man, Sut phat penalty) sang Tieng Viet co dau

from PyQt6.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QLabel, 
    QPushButton, QFrame, QGridLayout, QTabWidget,
    QWidget, QMessageBox
)
from PyQt6.QtCore import pyqtSignal, Qt, QTimer
from xu_ly_tro_choi.minigame_giua_gio import (
    tao_danh_sach_the_lat_tri_nho, quay_vong_quay_may_man, xu_ly_sut_phat_penalty
)
from xu_ly_hoc_tap.he_thong_thuong import cong_phan_thuong
from giao_dien.man_hinh_gap_thu_moi import ManHinhGapThuMoi

class HopThoaiMinigameGiuaGioDialog(QDialog):
    """Hộp thoại Minigame thư giãn giữa giờ học giúp học sinh giải trí và tích lũy XP (Bộ 4 Minigames)."""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("MINIGAME THƯ GIÃN GIỮA GIỜ HỌC & LUYỆN TẬP - BỘ 4 MINIGAMES")
        self.resize(720, 600)

        self.the_list = []
        self.open_cards = []
        self.matched_pairs = 0
        self.card_buttons = []

        self.timer_spin = QTimer(self)
        self.spin_count = 0
        self.timer_spin.timeout.connect(self.hieu_ung_quay_vong_quay)

        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(15, 15, 15, 15)
        main_layout.setSpacing(12)

        # Header tiêu đề chữ trắng
        self.lbl_header = QLabel("MINIGAME THƯ GIÃN GIỮA GIỜ - BỘ 3 MINIGAMES GIẢI TRÍ & TÍCH LŨY XP")
        self.lbl_header.setStyleSheet("font-size: 18px; font-weight: bold; color: #FFFFFF;")
        main_layout.addWidget(self.lbl_header)

        # Tab điều hướng Bộ 3 Minigames
        self.tabs = QTabWidget()
        self.tabs.setStyleSheet("""
            QTabWidget::pane { border: 2px solid #00A2FF; border-radius: 8px; background-color: #001F3F; }
            QTabBar::tab { background-color: #002B4D; color: #FFFFFF; font-weight: bold; font-size: 13px; padding: 8px 12px; margin-right: 4px; border-top-left-radius: 6px; border-top-right-radius: 6px; }
            QTabBar::tab:selected { background-color: #00A2FF; color: #FFFFFF; }
        """)

        # Tab 1: Lật thẻ ghi nhớ
        self.tab_lat_the = QWidget()
        self.init_tab_lat_the()
        self.tabs.addTab(self.tab_lat_the, "1. Lật Thẻ Ghi Nhớ")

        # Tab 2: Vòng quay may mắn
        self.tab_vong_quay = QWidget()
        self.init_tab_vong_quay()
        self.tabs.addTab(self.tab_vong_quay, "2. Vòng Quay May Mắn")

        # Tab 3: Sút phạt penalty
        self.tab_penalty = QWidget()
        self.init_tab_penalty()
        self.tabs.addTab(self.tab_penalty, "3. Sút Phạt Penalty")

        # Tab 4: Máy gắp thú 3D
        self.tab_gap_thu = ManHinhGapThuMoi(self)
        self.tabs.addTab(self.tab_gap_thu, "4. Gắp Thú 3D Siêu Cấp")

        main_layout.addWidget(self.tabs)

        # Nút đóng
        btn_close = QPushButton("Đóng & Tiếp tục học")
        btn_close.setProperty("class", "btn-primary")
        btn_close.setStyleSheet("font-size: 15px; font-weight: bold; color: #FFFFFF; padding: 10px 20px;")
        btn_close.clicked.connect(self.accept)
        
        btn_layout = QHBoxLayout()
        btn_layout.addStretch()
        btn_layout.addWidget(btn_close)
        main_layout.addLayout(btn_layout)

    def mo_tab_ngau_nhien(self, cau_so=1):
        """Mở ngẫu nhiên 1 trong 4 tab Minigame sau khi học sinh làm xong câu hỏi."""
        import random
        idx_tab = random.randint(0, 3)
        self.tabs.setCurrentIndex(idx_tab)
        self.lbl_header.setText(f"CHÚC MỪNG BẠN ĐÃ TRẢ LỜI CÂU {cau_so}! CHƠI MINIGAME NHẬN THƯỞNG!")


    # -------------------------------------------------------------
    # TAB 1: LẬT THẺ GHI NHỚ
    # -------------------------------------------------------------
    def init_tab_lat_the(self):
        layout = QVBoxLayout(self.tab_lat_the)
        layout.setContentsMargins(15, 15, 15, 15)
        layout.setSpacing(10)

        lbl_hd = QLabel("Hướng dẫn: Nhấp lật 2 thẻ ghép đúng cặp đáp án tương ứng (6 cặp). Hoàn thành nhận +100 XP!")
        lbl_hd.setStyleSheet("font-size: 14px; color: #FFFFFF; font-weight: bold;")
        lbl_hd.setWordWrap(True)
        layout.addWidget(lbl_hd)

        self.lbl_score_card = QLabel("Đã ghép đúng: 0 / 6 cặp")
        self.lbl_score_card.setStyleSheet("font-size: 15px; font-weight: bold; color: #00FFCC;")
        layout.addWidget(self.lbl_score_card)

        # Container Lưới thẻ
        self.grid_cards_widget = QWidget()
        self.grid_cards_layout = QGridLayout(self.grid_cards_widget)
        self.grid_cards_layout.setSpacing(10)
        layout.addWidget(self.grid_cards_widget)

        btn_restart = QPushButton("Chơi lại / Trộn thẻ mới")
        btn_restart.setProperty("class", "btn-secondary")
        btn_restart.setStyleSheet("font-size: 14px; font-weight: bold; color: #FFFFFF;")
        btn_restart.clicked.connect(self.khoi_tao_game_lat_the)
        layout.addWidget(btn_restart)

        self.khoi_tao_game_lat_the()

    def khoi_tao_game_lat_the(self):
        """Khởi tạo hoặc chơi lại trò chơi lật thẻ."""
        # Xóa các thẻ cũ
        for i in reversed(range(self.grid_cards_layout.count())):
            w = self.grid_cards_layout.itemAt(i).widget()
            if w:
                w.setParent(None)

        self.the_list = tao_danh_sach_the_lat_tri_nho()
        self.open_cards = []
        self.matched_pairs = 0
        self.card_buttons = []
        self.lbl_score_card.setText("Đã ghép đúng: 0 / 6 cặp")

        for idx, item in enumerate(self.the_list):
            btn = QPushButton("?")
            btn.setProperty("class", "card-option")
            btn.setStyleSheet("font-size: 14px; font-weight: bold; color: #FFFFFF; background-color: #002B4D; border: 2px solid #00A2FF; border-radius: 8px; min-height: 55px;")
            btn.clicked.connect(lambda checked, i=idx, b=btn: self.click_lat_the(i, b))
            
            row = idx // 4
            col = idx % 4
            self.grid_cards_layout.addWidget(btn, row, col)
            self.card_buttons.append(btn)

    def click_lat_the(self, idx, button):
        if len(self.open_cards) >= 2 or idx in [c['idx'] for c in self.open_cards]:
            return

        card_info = self.the_list[idx]
        button.setText(card_info["text"])
        button.setStyleSheet("font-size: 13px; font-weight: bold; color: #FFFFFF; background-color: #005599; border: 2px solid #00FFCC; border-radius: 8px; min-height: 55px;")
        
        self.open_cards.append({"idx": idx, "button": button, "info": card_info})

        if len(self.open_cards) == 2:
            c1 = self.open_cards[0]
            c2 = self.open_cards[1]
            if c1["info"]["pair_id"] == c2["info"]["pair_id"]:
                # Ghép đúng
                c1["button"].setStyleSheet("font-size: 13px; font-weight: bold; color: #00FFCC; background-color: #004422; border: 2px solid #00FF00; border-radius: 8px; min-height: 55px;")
                c2["button"].setStyleSheet("font-size: 13px; font-weight: bold; color: #00FFCC; background-color: #004422; border: 2px solid #00FF00; border-radius: 8px; min-height: 55px;")
                c1["button"].setEnabled(False)
                c2["button"].setEnabled(False)
                self.matched_pairs += 1
                self.lbl_score_card.setText(f"Đã ghép đúng: {self.matched_pairs} / 6 cặp")
                self.open_cards = []

                if self.matched_pairs == 6:
                    cong_phan_thuong(100)
                    QMessageBox.information(self, "Chúc mừng", "Bạn đã lật đúng tất cả 6 cặp thẻ ghi nhớ! Nhận ngay +100 XP Thưởng!")
            else:
                # Ghép sai -> Úp thẻ sau 1 giây
                QTimer.singleShot(1000, self.up_the_sai)

    def up_the_sai(self):
        for c in self.open_cards:
            c["button"].setText("?")
            c["button"].setStyleSheet("font-size: 14px; font-weight: bold; color: #FFFFFF; background-color: #002B4D; border: 2px solid #00A2FF; border-radius: 8px; min-height: 55px;")
        self.open_cards = []

    # -------------------------------------------------------------
    # TAB 2: VÒNG QUAY MAY MẮN
    # -------------------------------------------------------------
    def init_tab_vong_quay(self):
        layout = QVBoxLayout(self.tab_vong_quay)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(15)

        lbl_hd = QLabel("Nhấn 'Quay Thưởng May Mắn' để nhận ngẫu nhiên phần thưởng điểm kinh nghiệm XP tích lũy học tập!")
        lbl_hd.setStyleSheet("font-size: 15px; color: #FFFFFF; font-weight: bold;")
        lbl_hd.setWordWrap(True)
        layout.addWidget(lbl_hd)

        # Khung hiển thị phần thưởng quay được
        self.card_wheel_res = QFrame()
        self.card_wheel_res.setProperty("class", "card-widget")
        card_layout = QVBoxLayout(self.card_wheel_res)
        card_layout.setContentsMargins(20, 25, 20, 25)

        self.lbl_wheel_title = QLabel("BẮT ĐẦU QUAY THƯỞNG")
        self.lbl_wheel_title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lbl_wheel_title.setStyleSheet("font-size: 22px; font-weight: bold; color: #00FFCC;")
        card_layout.addWidget(self.lbl_wheel_title)

        self.lbl_wheel_desc = QLabel("Phần thưởng may mắn của bạn sẽ xuất hiện tại đây...")
        self.lbl_wheel_desc.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lbl_wheel_desc.setStyleSheet("font-size: 16px; color: #FFFFFF; font-weight: bold; margin-top: 10px;")
        card_layout.addWidget(self.lbl_wheel_desc)

        layout.addWidget(self.card_wheel_res)

        self.btn_spin = QPushButton("Quay Thưởng May Mắn Ngay")
        self.btn_spin.setProperty("class", "btn-primary")
        self.btn_spin.setStyleSheet("font-size: 16px; font-weight: bold; color: #FFFFFF; padding: 12px 24px;")
        self.btn_spin.clicked.connect(self.bat_dau_quay)
        layout.addWidget(self.btn_spin)

        # Bang chu thich Huong dan Dieu kien Kiem Ve Vang
        lbl_huong_dan_ve_vang = QLabel(
            "ĐIỀU KIỆN KIẾM VÉ VÀNG (LÀM NHIỆM VỤ):\n"
            "Vé Vàng là vật phẩm quý giá, chỉ có thể kiếm được khi hoàn thành các nhiệm vụ học tập:\n"
            "- Hoàn thành xuất sắc nhiệm vụ ngày (+1 Vé Vàng)\n"
            "- Đạt điểm 10 / Xuất sắc bài kiểm tra (+1 Vé Vàng)\n"
            "- Đạt chuỗi Streak học tập liên tục 7 ngày (+1 Vé Vàng)"
        )
        lbl_huong_dan_ve_vang.setWordWrap(True)
        lbl_huong_dan_ve_vang.setStyleSheet(
            "background-color: #0F172A; color: #F59E0B; font-size: 13px; font-weight: bold; "
            "border: 2px solid #F59E0B; border-radius: 12px; padding: 10px; margin-top: 10px;"
        )
        layout.addWidget(lbl_huong_dan_ve_vang)

        layout.addStretch()

    def bat_dau_quay(self):
        self.btn_spin.setEnabled(False)
        self.spin_count = 0
        self.timer_spin.start(100)

    def hieu_ung_quay_vong_quay(self):
        self.spin_count += 1
        danh_sach_tam = ["Cộng 50 XP", "Cộng 100 XP", "Cộng 150 XP", "Siêu Phần Thưởng 200 XP", "Huy Hiệu Chăm Chỉ"]
        self.lbl_wheel_title.setText(danh_sach_tam[self.spin_count % len(danh_sach_tam)])

        if self.spin_count >= 15:
            self.timer_spin.stop()
            thuong = quay_vong_quay_may_man()
            self.lbl_wheel_title.setText(thuong["ten"])
            self.lbl_wheel_desc.setText(f"Chúc mừng bạn! Hệ thống đã tự động cộng +{thuong['xp']} XP vào tài khoản!")
            self.btn_spin.setEnabled(True)

    # -------------------------------------------------------------
    # TAB 3: SÚT PHẠT PENALTY
    # -------------------------------------------------------------
    def init_tab_penalty(self):
        layout = QVBoxLayout(self.tab_penalty)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(15)

        lbl_hd = QLabel("Chọn góc sút bóng penalty vượt qua thủ môn để ghi bàn và nhận +60 XP Thưởng!")
        lbl_hd.setStyleSheet("font-size: 15px; color: #FFFFFF; font-weight: bold;")
        lbl_hd.setWordWrap(True)
        layout.addWidget(lbl_hd)

        # Khung màn sân bóng
        self.card_pitch = QFrame()
        self.card_pitch.setProperty("class", "card-widget")
        pitch_layout = QVBoxLayout(self.card_pitch)
        pitch_layout.setContentsMargins(15, 20, 15, 20)

        self.lbl_penalty_res = QLabel("SÂN BÓNG PENALTY: CHỌN GÓC SÚT BÊN DƯỚI")
        self.lbl_penalty_res.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lbl_penalty_res.setStyleSheet("font-size: 18px; font-weight: bold; color: #FFFFFF;")
        self.lbl_penalty_res.setWordWrap(True)
        pitch_layout.addWidget(self.lbl_penalty_res)

        layout.addWidget(self.card_pitch)

        # Các góc sút
        grid_sut = QGridLayout()
        grid_sut.setSpacing(10)

        cac_goc = [
            ("Trái Trên", 0, 0),
            ("Phải Trên", 0, 1),
            ("Chính Giữa", 1, 0),
            ("Trái Dưới", 2, 0),
            ("Phải Dưới", 2, 1)
        ]

        for goc_ten, r, c in cac_goc:
            btn = QPushButton(f"Sút Góc {goc_ten}")
            btn.setProperty("class", "btn-secondary")
            btn.setStyleSheet("font-size: 14px; font-weight: bold; color: #FFFFFF; padding: 10px;")
            btn.clicked.connect(lambda checked, g=goc_ten: self.thuc_hien_sut(g))
            grid_sut.addWidget(btn, r, c)

        layout.addLayout(grid_sut)

    def thuc_hien_sut(self, goc_sut):
        res = xu_ly_sut_phat_penalty(goc_sut)
        if res["vao"]:
            self.lbl_penalty_res.setStyleSheet("font-size: 18px; font-weight: bold; color: #00FFCC;")
        else:
            self.lbl_penalty_res.setStyleSheet("font-size: 18px; font-weight: bold; color: #FF6666;")
        self.lbl_penalty_res.setText(res["thong_bao"])
