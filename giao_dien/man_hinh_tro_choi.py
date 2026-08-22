# Thu muc: giao_dien
# File: man_hinh_tro_choi.py
# Mo ta: Man hinh Tro choi Minigame va Ung dung Tien ich Hoc tap voi bo cuc cuon QScrollArea khong bi che chu che nut sang Tieng Viet co dau

import os
from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, 
    QLineEdit, QPushButton, QFrame, QMessageBox,
    QTabWidget, QGridLayout, QProgressBar, QTextEdit,
    QStackedWidget, QScrollArea, QComboBox
)
from PyQt6.QtCore import QTimer, Qt, pyqtSignal
from PyQt6.QtGui import QFont, QPixmap

from du_lieu.kho_noi_dung_hoc import (
    lay_danh_sach_lop, lay_danh_sach_mon_hoc, lay_chu_de_theo_lop_va_mon
)
from xu_ly_tro_choi.quan_ly_tro_choi import (
    sinh_phep_tinh_math_racer, lay_danh_sach_the_memory,
    lay_doan_van_sieu_go_phim, tinh_bieu_thuc_may_tinh,
    luu_ghi_chu_hoc_tap, lay_ghi_chu_hoc_tap
)
from xu_ly_hoc_tap.he_thong_thuong import cong_phan_thuong

class ManHinhTroChoi(QWidget):
    """Màn hình Trung tâm Trò chơi Minigame và Ứng dụng Học tập với BỐ CỤC CUỘN TỰ ĐỘNG KHÔNG BỊ CHE CHỮ KHÔNG BỊ CHE NÚT."""

    def __init__(self, parent=None):
        super().__init__(parent)
        
        # State Game Math Racer
        self.math_racer_score = 0
        self.math_racer_progress = 0
        self.math_racer_current = None
        
        # State Game Memory Match
        self.memory_cards = []
        self.memory_selected = []
        self.memory_matched_ids = set()
        
        # State Game Siêu Gõ Phím 3 Phút
        self.typing_sample_text = ""
        self.typing_seconds_left = 180
        self.typing_timer = QTimer(self)
        self.typing_timer.timeout.connect(self.cap_nhat_typing_timer)
        self.typing_running = False
        self.typing_stage = 1

        # State App Pomodoro
        self.pomo_seconds = 1500
        self.pomo_timer = QTimer(self)
        self.pomo_timer.timeout.connect(self.cap_nhat_pomo)
        self.pomo_running = False

        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(15, 15, 15, 15)
        main_layout.setSpacing(12)

        # Tiêu đề chữ trắng
        title_label = QLabel("TRUNG TÂM TRÒ CHƠI MINIGAME VÀ ỨNG DỤNG HỌC TẬP")
        title_label.setStyleSheet("font-size: 22px; font-weight: bold; color: #FFFFFF;")
        main_layout.addWidget(title_label)

        # Thanh chọn Lớp, Môn học và 5 Chủ đề chơi chữ trắng
        filter_frame = QFrame()
        filter_frame.setProperty("class", "card-widget")
        filter_layout = QHBoxLayout(filter_frame)
        filter_layout.setContentsMargins(12, 10, 12, 10)

        lbl_lop = QLabel("Lớp:")
        lbl_lop.setStyleSheet("font-weight: bold; color: #FFFFFF; font-size: 15px;")
        self.cbo_lop = QComboBox()
        self.cbo_lop.setStyleSheet("color: #FFFFFF; font-weight: bold; font-size: 15px;")
        self.cbo_lop.addItems(lay_danh_sach_lop())
        self.cbo_lop.setCurrentText("Lớp 6")
        self.cbo_lop.currentTextChanged.connect(self.thay_doi_lop)

        lbl_mon = QLabel("Môn:")
        lbl_mon.setStyleSheet("font-weight: bold; color: #FFFFFF; font-size: 15px;")
        self.cbo_mon = QComboBox()
        self.cbo_mon.setStyleSheet("color: #FFFFFF; font-weight: bold; font-size: 15px;")
        self.cbo_mon.currentTextChanged.connect(self.thay_doi_mon)

        lbl_chu_de = QLabel("5 Chủ đề chơi:")
        lbl_chu_de.setStyleSheet("font-weight: bold; color: #FFFFFF; font-size: 15px;")
        self.cbo_chu_de = QComboBox()
        self.cbo_chu_de.setStyleSheet("color: #FFFFFF; font-weight: bold; font-size: 15px;")

        filter_layout.addWidget(lbl_lop)
        filter_layout.addWidget(self.cbo_lop)
        filter_layout.addWidget(lbl_mon)
        filter_layout.addWidget(self.cbo_mon)
        filter_layout.addWidget(lbl_chu_de)
        filter_layout.addWidget(self.cbo_chu_de, 2)

        main_layout.addWidget(filter_frame)

        # Tab Widget chính
        self.tab_widget = QTabWidget()
        self.tab_widget.setStyleSheet(
            "QTabWidget::pane { border: 2px solid #393B3D; border-radius: 10px; background-color: #191B1D; } "
            "QTabBar::tab { background-color: #232527; color: #FFFFFF; font-weight: bold; padding: 10px 20px; border-top-left-radius: 8px; border-top-right-radius: 8px; margin-right: 4px; } "
            "QTabBar::tab:selected { background-color: #0084FF; color: #FFFFFF; border-bottom: 3px solid #0052A3; }"
        )
        self.tab_widget.currentChanged.connect(self.on_tab_widget_changed)

        # Tab 1: Trò chơi Minigame
        tab_games = QWidget()
        layout_games = QVBoxLayout(tab_games)
        layout_games.setContentsMargins(10, 10, 10, 10)
        layout_games.setSpacing(10)

        # Thanh chọn Game
        nav_game_layout = QHBoxLayout()
        btn_g1 = QPushButton("Roblox Math Racer (Đua xe Toán)")
        btn_g1.setProperty("class", "btn-primary")
        btn_g1.setStyleSheet("color: #FFFFFF; font-weight: bold;")
        btn_g1.clicked.connect(lambda: self.stack_game.setCurrentIndex(0))

        btn_g2 = QPushButton("Memory Card Match (Lật thẻ Thuật ngữ)")
        btn_g2.setProperty("class", "btn-success")
        btn_g2.setStyleSheet("color: #FFFFFF; font-weight: bold;")
        btn_g2.clicked.connect(lambda: self.stack_game.setCurrentIndex(1))

        btn_g3 = QPushButton("Siêu Gõ Phím (Đoạn văn 3 Phút)")
        btn_g3.setProperty("class", "btn-secondary")
        btn_g3.setStyleSheet("color: #FFFFFF; font-weight: bold;")
        nav_game_layout.addWidget(btn_g1)
        nav_game_layout.addWidget(btn_g2)
        nav_game_layout.addWidget(btn_g3)
        layout_games.addLayout(nav_game_layout)

        # StackedWidget các trò chơi Minigame
        self.stack_game = QStackedWidget()
        self.stack_game.addWidget(self.create_math_racer_widget())
        self.stack_game.addWidget(self.create_memory_match_widget())
        self.stack_game.addWidget(self.create_super_typing_widget())
        self.stack_game.currentChanged.connect(self.on_stack_game_changed)

        layout_games.addWidget(self.stack_game)
        self.tab_widget.addTab(tab_games, "Trò chơi Minigame Giáo dục")

        # Tab 2: Ứng dụng Tiện ích
        tab_apps = QWidget()
        layout_apps = QVBoxLayout(tab_apps)
        layout_apps.setContentsMargins(10, 10, 10, 10)
        layout_apps.setSpacing(10)

        # Thanh chọn Ứng dụng
        nav_app_layout = QHBoxLayout()
        btn_a1 = QPushButton("Máy tính Khoa học Roblox")
        btn_a1.setProperty("class", "btn-primary")
        btn_a1.setStyleSheet("color: #FFFFFF; font-weight: bold;")
        btn_a1.clicked.connect(lambda: self.stack_app.setCurrentIndex(0))

        btn_a2 = QPushButton("Đồng hồ Pomodoro (25 phút)")
        btn_a2.setProperty("class", "btn-success")
        btn_a2.setStyleSheet("color: #FFFFFF; font-weight: bold;")
        btn_a2.clicked.connect(lambda: self.stack_app.setCurrentIndex(1))

        btn_a3 = QPushButton("Sổ tay Ghi chú & Lịch học")
        btn_a3.setProperty("class", "btn-secondary")
        btn_a3.setStyleSheet("color: #FFFFFF; font-weight: bold;")
        btn_a3.clicked.connect(lambda: self.stack_app.setCurrentIndex(2))

        nav_app_layout.addWidget(btn_a1)
        nav_app_layout.addWidget(btn_a2)
        nav_app_layout.addWidget(btn_a3)
        layout_apps.addLayout(nav_app_layout)

        # StackedWidget các ứng dụng tiện ích
        self.stack_app = QStackedWidget()
        self.stack_app.addWidget(self.create_calculator_widget())
        self.stack_app.addWidget(self.create_pomodoro_widget())
        self.stack_app.addWidget(self.create_notes_widget())

        layout_apps.addWidget(self.stack_app)
        self.tab_widget.addTab(tab_apps, "Ứng dụng Tiện ích Học tập")

        main_layout.addWidget(self.tab_widget)

        # Tải danh sách Lớp và Môn ban đầu
        self.thay_doi_lop(self.cbo_lop.currentText())

    def wrap_in_scroll(self, widget):
        """Bọc widget trong QScrollArea để đảm bảo 100% không bị che khuất chữ hay nút bấm."""
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setStyleSheet("QScrollArea { border: none; background-color: transparent; }")
        scroll.setWidget(widget)
        return scroll

    def on_stack_game_changed(self, index):
        """Khi chuyển game trong tab Minigame: chỉ chạy đồng hồ khi VÀO MÀN HÌNH SIÊU GÕ PHÍM (index 2)."""
        if index == 2:
            if self.typing_running and self.typing_seconds_left > 0:
                self.typing_timer.start(1000)
        else:
            self.typing_timer.stop()

    def on_tab_widget_changed(self, index):
        """Khi chuyển giữa tab Trò chơi và Ứng dụng: tạm dừng đồng hồ khi thoát khỏi tab Trò chơi."""
        if index == 0 and self.stack_game.currentIndex() == 2:
            if self.typing_running and self.typing_seconds_left > 0:
                self.typing_timer.start(1000)
        else:
            self.typing_timer.stop()

    def showEvent(self, event):
        """Khi mở màn hình Trò chơi: chỉ tiếp tục chạy đồng hồ gõ phím nếu đang ở đúng màn hình Siêu gõ phím."""
        super().showEvent(event)
        if hasattr(self, 'stack_game') and self.stack_game.currentIndex() == 2 and hasattr(self, 'tab_widget') and self.tab_widget.currentIndex() == 0:
            if self.typing_running and self.typing_seconds_left > 0:
                self.typing_timer.start(1000)

    def hideEvent(self, event):
        """Khi thoát khỏi màn hình Trò chơi: TẠM DỪNG ĐỒNG HỒ ĐẾM NGƯỢC SIÊU GÕ PHÍM NGAY LẬP TỨC."""
        super().hideEvent(event)
        if hasattr(self, 'typing_timer'):
            self.typing_timer.stop()

    def thay_doi_lop(self, ten_lop):
        self.cbo_mon.blockSignals(True)
        self.cbo_mon.clear()
        danh_sach_mon = lay_danh_sach_mon_hoc(ten_lop)
        self.cbo_mon.addItems(danh_sach_mon)
        self.cbo_mon.blockSignals(False)
        if danh_sach_mon:
            self.thay_doi_mon(danh_sach_mon[0])

    def thay_doi_mon(self, ten_mon):
        if not ten_mon:
            return
        ten_lop = self.cbo_lop.currentText()
        danh_sach_5_chu_de = lay_chu_de_theo_lop_va_mon(ten_lop, ten_mon)
        
        self.cbo_chu_de.blockSignals(True)
        self.cbo_chu_de.clear()
        self.cbo_chu_de.addItems(danh_sach_5_chu_de)
        self.cbo_chu_de.blockSignals(False)

        # Reset dữ liệu trò chơi theo môn học mới
        self.init_math_racer()
        self.init_memory_match()

    # --- GAME 1: ROBLOX MATH RACER ---
    def create_math_racer_widget(self):
        w = QWidget()
        l = QVBoxLayout(w)
        l.setContentsMargins(15, 15, 15, 15)
        l.setSpacing(12)

        title = QLabel("GAME ĐUA XE TOÁN HỌC ROBLOX MATH RACER")
        title.setStyleSheet("font-size: 18px; font-weight: bold; color: #FFFFFF;")
        l.addWidget(title)

        self.lbl_racer_score = QLabel("Điểm số: 0 XP | Vị trí đua: Khởi động")
        self.lbl_racer_score.setStyleSheet("font-size: 15px; font-weight: bold; color: #FFFFFF;")
        l.addWidget(self.lbl_racer_score)

        self.progress_racer = QProgressBar()
        self.progress_racer.setValue(0)
        self.progress_racer.setHeight = 24
        l.addWidget(self.progress_racer)

        card_q = QFrame()
        card_q.setProperty("class", "card-widget")
        card_layout = QVBoxLayout(card_q)

        self.lbl_racer_question = QLabel("Giải phép tính tăng tốc Xe đua Roblox:")
        self.lbl_racer_question.setStyleSheet("font-size: 17px; font-weight: bold; color: #FFFFFF;")
        card_layout.addWidget(self.lbl_racer_question)

        self.txt_racer_answer = QLineEdit()
        self.txt_racer_answer.setPlaceholderText("Nhập kết quả rồi bấm Enter hoặc 'Tăng tốc'...")
        self.txt_racer_answer.returnPressed.connect(self.check_math_racer_answer)
        card_layout.addWidget(self.txt_racer_answer)

        btn_submit_racer = QPushButton("Tăng tốc Xe Đua")
        btn_submit_racer.setProperty("class", "btn-primary")
        btn_submit_racer.setStyleSheet("color: #FFFFFF; font-weight: bold; font-size: 15px;")
        btn_submit_racer.clicked.connect(self.check_math_racer_answer)
        card_layout.addWidget(btn_submit_racer)

        l.addWidget(card_q)
        l.addStretch()
        return w

    def init_math_racer(self):
        ten_lop = self.cbo_lop.currentText()
        self.math_racer_current = sinh_phep_tinh_math_racer(ten_lop)
        if hasattr(self, 'lbl_racer_question'):
            self.lbl_racer_question.setText(f"Giải phép tính tăng tốc Xe đua Roblox: {self.math_racer_current['cau_hoi']}")
            self.txt_racer_answer.clear()

    def check_math_racer_answer(self):
        if not self.math_racer_current:
            return
        ans = self.txt_racer_answer.text().strip()
        correct = str(self.math_racer_current['dap_an_dung']).strip()

        if ans == correct:
            self.math_racer_score += 10
            self.math_racer_progress = min(100, self.math_racer_progress + 20)
            self.progress_racer.setValue(self.math_racer_progress)
            self.lbl_racer_score.setText(f"Điểm số: {self.math_racer_score} XP | Vị trí đua: Đang dẫn đầu ({self.math_racer_progress}%)")
            
            if self.math_racer_progress >= 100:
                cong_phan_thuong(10.0, 5)
                QMessageBox.information(self, "Về đích Xe Đua Roblox", "XUẤT SẮC! Xe đua Roblox của em đã VỀ ĐÍCH ĐẦU TIÊN!\nThưởng +50 XP và +20 Robux Coin!")
                self.math_racer_progress = 0
                self.progress_racer.setValue(0)
            
            self.init_math_racer()
        else:
            QMessageBox.warning(self, "Chưa chính xác", f"Kết quả chưa đúng. Đáp án đúng là {correct}. Hãy thử câu tiếp theo!")
            self.init_math_racer()

    # --- GAME 2: MEMORY CARD MATCH ---
    def create_memory_match_widget(self):
        w = QWidget()
        l = QVBoxLayout(w)
        l.setContentsMargins(15, 15, 15, 15)
        l.setSpacing(12)

        title = QLabel("GAME LẬT THẺ THUẬT NGỮ KHÁM PHÁ ARCHIEVEMENT")
        title.setStyleSheet("font-size: 18px; font-weight: bold; color: #FFFFFF;")
        l.addWidget(title)

        self.lbl_memory_status = QLabel("Lật ghép 2 thẻ tương ứng thuật ngữ bài học:")
        self.lbl_memory_status.setStyleSheet("font-size: 15px; font-weight: bold; color: #FFFFFF;")
        l.addWidget(self.lbl_memory_status)

        self.grid_cards_container = QWidget()
        self.grid_cards_layout = QGridLayout(self.grid_cards_container)
        self.grid_cards_layout.setSpacing(10)
        l.addWidget(self.grid_cards_container)

        l.addStretch()
        return w

    def init_memory_match(self):
        if not hasattr(self, 'grid_cards_layout'):
            return

        for i in reversed(range(self.grid_cards_layout.count())):
            widget = self.grid_cards_layout.itemAt(i).widget()
            if widget:
                widget.setParent(None)

        ten_mon = self.cbo_mon.currentText()
        self.memory_cards = lay_danh_sach_the_memory(ten_mon)
        self.memory_selected = []
        self.memory_matched_ids = set()
        self.btn_card_dict = {}

        for idx, card in enumerate(self.memory_cards):
            btn = QPushButton("?")
            btn.setProperty("class", "card-option")
            btn.setStyleSheet("font-size: 15px; font-weight: bold; color: #FFFFFF; min-height: 60px;")
            btn.clicked.connect(lambda checked, i=idx: self.on_click_memory_card(i))
            
            row = idx // 3
            col = idx % 3
            self.grid_cards_layout.addWidget(btn, row, col)
            self.btn_card_dict[idx] = btn

    def on_click_memory_card(self, card_idx):
        if card_idx in self.memory_matched_ids or card_idx in self.memory_selected:
            return

        card = self.memory_cards[card_idx]
        btn = self.btn_card_dict[card_idx]
        btn.setText(card["noi_dung"])
        btn.setStyleSheet("font-size: 14px; font-weight: bold; color: #00E676; background-color: #002B4D; border: 2px solid #00E676; min-height: 60px;")

        self.memory_selected.append(card_idx)

        if len(self.memory_selected) == 2:
            idx1, idx2 = self.memory_selected[0], self.memory_selected[1]
            c1, c2 = self.memory_cards[idx1], self.memory_cards[idx2]

            if c1["pair_id"] == c2["pair_id"]:
                self.memory_matched_ids.add(idx1)
                self.memory_matched_ids.add(idx2)
                self.memory_selected = []

                if len(self.memory_matched_ids) == len(self.memory_cards):
                    cong_phan_thuong(10.0, 6)
                    QMessageBox.information(self, "Hoàn thành Lật thẻ", "CHÚC MỪNG! Em đã ghép đúng TẤT CẢ CÁC THẺ THUẬT NGỮ!\nThưởng +50 XP!")
                    self.init_memory_match()
            else:
                QTimer.singleShot(800, lambda: self.up_lai_the(idx1, idx2))
                self.memory_selected = []

    def up_lai_the(self, idx1, idx2):
        if idx1 in self.btn_card_dict:
            self.btn_card_dict[idx1].setText("?")
            self.btn_card_dict[idx1].setStyleSheet("font-size: 15px; font-weight: bold; color: #FFFFFF; min-height: 60px;")
        if idx2 in self.btn_card_dict:
            self.btn_card_dict[idx2].setText("?")
            self.btn_card_dict[idx2].setStyleSheet("font-size: 15px; font-weight: bold; color: #FFFFFF; min-height: 60px;")

    # --- GAME 3: SIÊU GÕ PHÍM 3 PHÚT ---
    def create_super_typing_widget(self):
        w = QWidget()
        l = QVBoxLayout(w)
        l.setContentsMargins(15, 15, 15, 15)
        l.setSpacing(12)

        title = QLabel("SIÊU GÕ PHÍM - LUYỆN GÕ PHÍM SIÊU TỐC (3 PHÚT / MÀN CHƠI)")
        title.setStyleSheet("font-size: 18px; font-weight: bold; color: #FFFFFF;")
        l.addWidget(title)

        status_row = QHBoxLayout()
        self.lbl_typing_stage = QLabel("Màn chơi: Màn 1")
        self.lbl_typing_stage.setStyleSheet("font-size: 16px; font-weight: bold; color: #FFFFFF;")

        self.lbl_typing_wpm = QLabel("Tốc độ gõ: 0 WPM | Độ chính xác: 100%")
        self.lbl_typing_wpm.setStyleSheet("font-size: 15px; font-weight: bold; color: #FFFFFF;")

        self.lbl_typing_timer = QLabel("Thời gian còn lại: 03:00")
        self.lbl_typing_timer.setStyleSheet("font-size: 16px; font-weight: bold; color: #FFFFFF; background-color: #002B4D; padding: 6px 16px; border-radius: 12px; border: 2px solid #00A2FF;")

        status_row.addWidget(self.lbl_typing_stage)
        status_row.addWidget(self.lbl_typing_wpm)
        status_row.addStretch()
        status_row.addWidget(self.lbl_typing_timer)
        l.addLayout(status_row)

        card_sample = QFrame()
        card_sample.setProperty("class", "card-widget")
        layout_sample = QVBoxLayout(card_sample)

        lbl_s_title = QLabel("Đoạn văn mẫu cần gõ luyện tập:")
        lbl_s_title.setStyleSheet("font-size: 14px; color: #FFFFFF; font-weight: bold;")
        layout_sample.addWidget(lbl_s_title)

        self.txt_typing_sample = QTextEdit()
        self.txt_typing_sample.setReadOnly(True)
        self.txt_typing_sample.setStyleSheet("color: #FFFFFF; font-size: 16px; font-weight: bold; background-color: #111214; border: 2px solid #393B3D; max-height: 100px;")
        layout_sample.addWidget(self.txt_typing_sample)

        l.addWidget(card_sample)

        card_input = QFrame()
        card_input.setProperty("class", "card-widget")
        layout_input = QVBoxLayout(card_input)

        lbl_i_title = QLabel("Ô gõ nhập liệu luyện tập tốc độ:")
        lbl_i_title.setStyleSheet("font-size: 14px; color: #FFFFFF; font-weight: bold;")
        layout_input.addWidget(lbl_i_title)

        self.txt_typing_input = QTextEdit()
        self.txt_typing_input.setStyleSheet("color: #FFFFFF; font-size: 16px; font-weight: bold; background-color: #111214; border: 2px solid #00A2FF; max-height: 110px;")
        self.txt_typing_input.setPlaceholderText("Gõ chính xác đoạn văn mẫu phía trên vào đây...")
        self.txt_typing_input.textChanged.connect(self.on_typing_input_changed)
        layout_input.addWidget(self.txt_typing_input)

        l.addWidget(card_input)

        btn_layout = QHBoxLayout()
        self.btn_next_stage = QPushButton("Màn tiếp theo")
        self.btn_next_stage.setProperty("class", "btn-primary")
        self.btn_next_stage.setStyleSheet("color: #FFFFFF; font-weight: bold; font-size: 15px; padding: 10px 18px;")
        self.btn_next_stage.clicked.connect(self.go_to_next_typing_stage)

        btn_new_paragraph = QPushButton("Đổi đoạn văn khác")
        btn_new_paragraph.setProperty("class", "btn-secondary")
        btn_new_paragraph.setStyleSheet("color: #FFFFFF; font-weight: bold; font-size: 15px; padding: 10px 18px;")
        btn_new_paragraph.clicked.connect(self.load_new_typing_paragraph)

        btn_submit_typing = QPushButton("Nộp bài Gõ phím")
        btn_submit_typing.setProperty("class", "btn-success")
        btn_submit_typing.setStyleSheet("color: #FFFFFF; font-weight: bold; font-size: 15px; padding: 10px 18px;")
        btn_submit_typing.clicked.connect(self.finish_super_typing)

        btn_layout.addWidget(self.btn_next_stage)
        btn_layout.addWidget(btn_new_paragraph)
        btn_layout.addWidget(btn_submit_typing)
        l.addLayout(btn_layout)

        self.load_new_typing_paragraph()
        return w

    def load_new_typing_paragraph(self):
        """Tải đoạn văn mới Siêu Gõ Phím, chỉ bật đồng hồ đếm ngược khi đang ở màn hình Siêu Gõ Phím."""
        self.typing_timer.stop()
        self.typing_seconds_left = 180
        self.typing_sample_text = lay_doan_van_sieu_go_phim()
        self.txt_typing_sample.setText(self.typing_sample_text)
        self.txt_typing_input.clear()
        self.txt_typing_input.setEnabled(True)
        self.lbl_typing_timer.setText("Thời gian còn lại: 03:00")
        self.lbl_typing_wpm.setText("Tốc độ gõ: 0 WPM | Độ chính xác: 100%")
        self.lbl_typing_stage.setText(f"Màn chơi: Màn {self.typing_stage}")
        
        self.typing_running = True
        # Chỉ chạy timer nếu người dùng đang thực sự xem màn hình Siêu gõ phím
        if hasattr(self, 'stack_game') and self.stack_game.currentIndex() == 2 and hasattr(self, 'tab_widget') and self.tab_widget.currentIndex() == 0:
            self.typing_timer.start(1000)

    def on_typing_input_changed(self):
        typed = self.txt_typing_input.toPlainText()
        if not typed:
            return

        if not self.typing_running:
            self.typing_running = True
            if hasattr(self, 'stack_game') and self.stack_game.currentIndex() == 2 and hasattr(self, 'tab_widget') and self.tab_widget.currentIndex() == 0:
                self.typing_timer.start(1000)

        sample = self.typing_sample_text
        
        so_ky_tu_dung = 0
        min_len = min(len(typed), len(sample))
        for i in range(min_len):
            if typed[i] == sample[i]:
                so_ky_tu_dung += 1
                
        accuracy = (so_ky_tu_dung / len(typed) * 100) if len(typed) > 0 else 100
        
        elapsed_sec = max(1, 180 - self.typing_seconds_left)
        elapsed_min = elapsed_sec / 60.0
        words_typed = len(typed.split())
        wpm = int(words_typed / elapsed_min)

        self.lbl_typing_wpm.setText(f"Tốc độ gõ: {wpm} WPM | Độ chính xác: {accuracy:.1f}%")

        if typed.strip() == sample.strip():
            self.typing_timer.stop()
            self.typing_running = False
            QMessageBox.information(self, "Hoàn thành Màn chơi", f"CHÚC MỪNG! Em đã hoàn thành xuất sắc Màn {self.typing_stage}!\nBấm 'Màn tiếp theo' để qua màn nhé!")

    def go_to_next_typing_stage(self):
        """Chuyển qua Màn chơi tiếp theo và thưởng XP."""
        self.typing_stage += 1
        cong_phan_thuong(10.0, 5)
        QMessageBox.information(self, "Qua Màn thành công", f"ĐÃ QUA MÀN! Chào mừng em đến với Màn {self.typing_stage}!\nThưởng: +50 XP và +20 Robux Coin!")
        self.load_new_typing_paragraph()

    def cap_nhat_typing_timer(self):
        """Cập nhật đếm ngược mỗi giây cho game Siêu Gõ Phím."""
        if self.typing_seconds_left > 0:
            self.typing_seconds_left -= 1
            m = self.typing_seconds_left // 60
            s = self.typing_seconds_left % 60
            self.lbl_typing_timer.setText(f"Thời gian còn lại: {m:02d}:{s:02d}")
        else:
            self.typing_timer.stop()
            self.typing_running = False
            QMessageBox.information(self, "Hết giờ 3 phút", "Hết thời gian 3 phút làm bài Siêu Gõ Phím! Hệ thống tự động tính điểm.")
            self.finish_super_typing()

    def finish_super_typing(self):
        self.typing_timer.stop()
        self.typing_running = False
        
        typed = self.txt_typing_input.toPlainText()
        sample = self.typing_sample_text
        
        so_ky_tu_dung = 0
        min_len = min(len(typed), len(sample))
        for i in range(min_len):
            if typed[i] == sample[i]:
                so_ky_tu_dung += 1
                
        accuracy = (so_ky_tu_dung / len(typed) * 100) if len(typed) > 0 else 0
        elapsed_sec = max(1, 180 - self.typing_seconds_left)
        words_typed = len(typed.split())
        wpm = int((words_typed / elapsed_sec) * 60)

        cong_phan_thuong(9.0, 5)
        
        msg = f"""
KẾT QUẢ SIÊU GÕ PHÍM (MÀN {self.typing_stage}):
- Tốc độ gõ trung bình: {wpm} WPM (từ/phút)
- Độ chính xác: {accuracy:.1f}%
- Thời gian thực hiện: {elapsed_sec} giây
- Phần thưởng: +40 XP và +15 Robux Coin!
        """
        QMessageBox.information(self, "Tổng kết Siêu Gõ Phím", msg)

    # --- APP 1: MÁY TÍNH KHOA HỌC ROBLOX ---
    def create_calculator_widget(self):
        w = QWidget()
        l = QVBoxLayout(w)
        l.setContentsMargins(15, 15, 15, 15)
        l.setSpacing(12)

        title = QLabel("MÁY TÍNH KHOA HỌC KỸ THUẬT ROBLOX")
        title.setStyleSheet("font-size: 18px; font-weight: bold; color: #FFFFFF;")
        l.addWidget(title)

        card_calc = QFrame()
        card_calc.setProperty("class", "card-widget")
        layout_calc = QVBoxLayout(card_calc)

        self.txt_calc_input = QLineEdit()
        self.txt_calc_input.setStyleSheet("font-size: 22px; font-weight: bold; color: #00E676; background-color: #111214; padding: 12px; border: 2px solid #00A2FF;")
        self.txt_calc_input.setPlaceholderText("Nhập biểu thức ví dụ: 25 * 4 + sin(30)...")
        self.txt_calc_input.returnPressed.connect(self.calculate_expression)
        layout_calc.addWidget(self.txt_calc_input)

        grid_calc = QGridLayout()
        grid_calc.setSpacing(8)

        buttons = [
            ('7', 0, 0), ('8', 0, 1), ('9', 0, 2), ('/', 0, 3), ('sin', 0, 4),
            ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('*', 1, 3), ('cos', 1, 4),
            ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('-', 2, 3), ('sqrt', 2, 4),
            ('0', 3, 0), ('.', 3, 1), ('+', 3, 2), ('=', 3, 3), ('C', 3, 4)
        ]

        for text, r, c in buttons:
            btn = QPushButton(text)
            if text == '=':
                btn.setProperty("class", "btn-primary")
            elif text == 'C':
                btn.setProperty("class", "btn-success")
            else:
                btn.setProperty("class", "btn-secondary")
            btn.setStyleSheet("font-size: 16px; font-weight: bold; min-height: 45px;")
            btn.clicked.connect(lambda checked, t=text: self.on_calc_button_clicked(t))
            grid_calc.addWidget(btn, r, c)

        layout_calc.addLayout(grid_calc)
        l.addWidget(card_calc)
        l.addStretch()
        return w

    def on_calc_button_clicked(self, char):
        if char == 'C':
            self.txt_calc_input.clear()
        elif char == '=':
            self.calculate_expression()
        elif char in ['sin', 'cos', 'sqrt']:
            self.txt_calc_input.setText(self.txt_calc_input.text() + f"{char}(")
        else:
            self.txt_calc_input.setText(self.txt_calc_input.text() + char)

    def calculate_expression(self):
        expr = self.txt_calc_input.text()
        ket_qua = tinh_bieu_thuc_may_tinh(expr)
        self.txt_calc_input.setText(str(ket_qua))

    # --- APP 2: ĐỒNG HỒ POMODORO ---
    def create_pomodoro_widget(self):
        w = QWidget()
        l = QVBoxLayout(w)
        l.setContentsMargins(15, 15, 15, 15)
        l.setSpacing(12)

        title = QLabel("ĐỒNG HỒ THỜI GIAN BIỂU POMODORO HỌC TẬP TẬP TRUNG")
        title.setStyleSheet("font-size: 18px; font-weight: bold; color: #FFFFFF;")
        l.addWidget(title)

        card_pomo = QFrame()
        card_pomo.setProperty("class", "card-widget")
        layout_pomo = QVBoxLayout(card_pomo)
        layout_pomo.setSpacing(15)

        self.lbl_pomo_clock = QLabel("25:00")
        self.lbl_pomo_clock.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lbl_pomo_clock.setStyleSheet("font-size: 52px; font-weight: bold; color: #00E676; background-color: #111214; padding: 20px; border-radius: 16px; border: 3px solid #00E676;")
        layout_pomo.addWidget(self.lbl_pomo_clock)

        row_pomo_btn = QHBoxLayout()
        btn_start_pomo = QPushButton("Bắt đầu Học tập 25 phút")
        btn_start_pomo.setProperty("class", "btn-primary")
        btn_start_pomo.setStyleSheet("color: #FFFFFF; font-weight: bold; font-size: 15px; padding: 10px 20px;")
        btn_start_pomo.clicked.connect(self.start_pomo)

        btn_pause_pomo = QPushButton("Tạm dừng")
        btn_pause_pomo.setProperty("class", "btn-secondary")
        btn_pause_pomo.setStyleSheet("color: #FFFFFF; font-weight: bold; font-size: 15px; padding: 10px 20px;")
        btn_pause_pomo.clicked.connect(self.pause_pomo)

        btn_reset_pomo = QPushButton("Đặt lại Đồng hồ")
        btn_reset_pomo.setProperty("class", "btn-success")
        btn_reset_pomo.setStyleSheet("color: #FFFFFF; font-weight: bold; font-size: 15px; padding: 10px 20px;")
        btn_reset_pomo.clicked.connect(self.reset_pomo)

        row_pomo_btn.addWidget(btn_start_pomo)
        row_pomo_btn.addWidget(btn_pause_pomo)
        row_pomo_btn.addWidget(btn_reset_pomo)
        layout_pomo.addLayout(row_pomo_btn)

        l.addWidget(card_pomo)
        l.addStretch()
        return w

    def start_pomo(self):
        self.pomo_running = True
        self.pomo_timer.start(1000)

    def pause_pomo(self):
        self.pomo_running = False
        self.pomo_timer.stop()

    def reset_pomo(self):
        self.pomo_timer.stop()
        self.pomo_running = False
        self.pomo_seconds = 1500
        self.lbl_pomo_clock.setText("25:00")

    def cap_nhat_pomo(self):
        if self.pomo_seconds > 0:
            self.pomo_seconds -= 1
            m = self.pomo_seconds // 60
            s = self.pomo_seconds % 60
            self.lbl_pomo_clock.setText(f"{m:02d}:{s:02d}")
        else:
            self.pomo_timer.stop()
            self.pomo_running = False
            cong_phan_thuong(10.0, 10)
            QMessageBox.information(self, "Hoàn thành Pomodoro", "XUẤT SẮC! Em đã hoàn thành phiên học 25 phút tập trung!\nThưởng +60 XP và +25 Robux Coin!")

    # --- APP 3: SỔ TAY GHI CHÚ ---
    def create_notes_widget(self):
        w = QWidget()
        l = QVBoxLayout(w)
        l.setContentsMargins(15, 15, 15, 15)
        l.setSpacing(12)

        title = QLabel("SỔ TAY GHI CHÚ VÀ LỊCH HỌC TẬP THÔNG MINH")
        title.setStyleSheet("font-size: 18px; font-weight: bold; color: #FFFFFF;")
        l.addWidget(title)

        card_note = QFrame()
        card_note.setProperty("class", "card-widget")
        layout_note = QVBoxLayout(card_note)

        lbl_n_title = QLabel("Nội dung ghi chú cá nhân:")
        lbl_n_title.setStyleSheet("font-size: 14px; color: #FFFFFF; font-weight: bold;")
        layout_note.addWidget(lbl_n_title)

        self.txt_notes = QTextEdit()
        self.txt_notes.setStyleSheet("color: #FFFFFF; font-size: 15px; font-weight: bold; background-color: #111214; border: 2px solid #393B3D; min-height: 180px;")
        self.txt_notes.setPlainText(lay_ghi_chu_hoc_tap())
        layout_note.addWidget(self.txt_notes)

        btn_save_note = QPushButton("Lưu Ghi Chú Cá Nhân")
        btn_save_note.setProperty("class", "btn-primary")
        btn_save_note.setStyleSheet("color: #FFFFFF; font-weight: bold; font-size: 15px; padding: 10px 20px;")
        btn_save_note.clicked.connect(self.save_notes)
        layout_note.addWidget(btn_save_note)

        l.addWidget(card_note)
        l.addStretch()
        return w

    def save_notes(self):
        text = self.txt_notes.toPlainText()
        luu_ghi_chu_hoc_tap(text)
        QMessageBox.information(self, "Đã lưu ghi chú", "Ghi chú và lịch học tập cá nhân đã được lưu thành công!")
