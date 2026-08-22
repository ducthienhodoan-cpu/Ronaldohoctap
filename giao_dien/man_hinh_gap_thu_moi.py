# Thu muc: giao_dien
# File: man_hinh_gap_thu_moi.py
# Mo ta: Giao dien Trung tam May Gap Thu 3D tuong tac Joystick 4 huong phien ban PyQt6 sang Tieng Viet co dau

from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, 
    QPushButton, QFrame, QGridLayout, QComboBox, 
    QProgressBar, QMessageBox, QDialog
)
from PyQt6.QtCore import Qt, QTimer
from xu_ly_tro_choi.quan_ly_gap_thu_moi import (
    lay_du_lieu_gap_thu, thuc_hien_luot_gap_moi, 
    CAC_MAY_GAP, DANH_MUC_BO_SUU_TAP, cong_ve_gap_tu_hoc_tap
)
from xu_ly_hoc_tap.he_thong_thuong import cong_phan_thuong

class ManHinhGapThuMoi(QWidget):
    """Giao diện Trung tâm Trò chơi Máy Gắp Thú 3D với cần Joystick 4 hướng và tích lũy vé gắp."""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.dang_gap = False
        self.combo_count = 0
        self.time_remaining = 20
        self.may_duoc_chon = "cute"

        self.timer_gap = QTimer(self)
        self.timer_gap.timeout.connect(self.cap_nhat_tien_trinh_gap)

        self.timer_countdown = QTimer(self)
        self.timer_countdown.timeout.connect(self.dem_nguoc_thoi_gian)

        self.init_ui()
        self.cap_nhat_giao_dien_tai_san()

    def init_ui(self):
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(15, 15, 15, 15)
        main_layout.setSpacing(12)

        # Header Thanh Tài sản & Cấp độ
        top_bar = QFrame()
        top_bar.setProperty("class", "card-widget")
        top_layout = QHBoxLayout(top_bar)
        top_layout.setContentsMargins(12, 10, 12, 10)

        self.lbl_ve_gap = QLabel("Vé Gắp: 5 Vé")
        self.lbl_ve_gap.setStyleSheet("font-size: 14px; font-weight: bold; color: #00FFCC;")

        self.lbl_ve_vang = QLabel("Vé Vàng: 1 Vé")
        self.lbl_ve_vang.setStyleSheet("font-size: 14px; font-weight: bold; color: #FFCC00;")

        self.lbl_combo = QLabel("Combo: 0x")
        self.lbl_combo.setStyleSheet("font-size: 14px; font-weight: bold; color: #FF66CC;")

        self.lbl_timer = QLabel("Thời gian: 20s")
        self.lbl_timer.setStyleSheet("font-size: 14px; font-weight: bold; color: #00A2FF;")

        top_layout.addWidget(self.lbl_ve_gap)
        top_layout.addWidget(self.lbl_ve_vang)
        top_layout.addWidget(self.lbl_combo)
        top_layout.addStretch()
        top_layout.addWidget(self.lbl_timer)

        main_layout.addWidget(top_bar)

        # Thanh chọn 6 Máy Gắp Thú
        may_bar = QHBoxLayout()
        may_bar.setSpacing(8)

        self.cbo_may_gap = QComboBox()
        self.cbo_may_gap.setStyleSheet("font-size: 14px; font-weight: bold; color: #FFFFFF; background-color: #002B4D; padding: 6px;")
        for mid, mobj in CAC_MAY_GAP.items():
            self.cbo_may_gap.addItem(mobj["ten"], mid)
        self.cbo_may_gap.currentIndexChanged.connect(self.doi_may_gap)

        btn_bo_suu_tap = QPushButton("Bộ Sưu Tập (Collections)")
        btn_bo_suu_tap.setProperty("class", "btn-secondary")
        btn_bo_suu_tap.setStyleSheet("font-size: 13px; font-weight: bold; color: #FFFFFF;")
        btn_bo_suu_tap.clicked.connect(self.hien_thi_bo_suu_tap)

        btn_nhiem_vu = QPushButton("Nhiệm Vụ Kiếm Vé")
        btn_nhiem_vu.setProperty("class", "btn-secondary")
        btn_nhiem_vu.setStyleSheet("font-size: 13px; font-weight: bold; color: #FFFFFF;")
        btn_nhiem_vu.clicked.connect(self.hien_thi_nhiem_vu)

        may_bar.addWidget(QLabel("Chọn Máy Gắp:"))
        may_bar.addWidget(self.cbo_may_gap)
        may_bar.addStretch()
        may_bar.addWidget(btn_bo_suu_tap)
        may_bar.addWidget(btn_nhiem_vu)

        main_layout.addLayout(may_bar)

        # Khung Màn hiển thị Máy Gắp Thú & Joystick
        game_frame = QFrame()
        game_frame.setProperty("class", "card-widget")
        game_layout = QVBoxLayout(game_frame)
        game_layout.setContentsMargins(15, 15, 15, 15)

        self.lbl_status = QLabel("MÁY GẮP THÚ 3D: DÙNG CẦN JOYSTICK 4 HƯỚNG ĐIỀU CHỈNH TAY GẮP")
        self.lbl_status.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lbl_status.setStyleSheet("font-size: 16px; font-weight: bold; color: #00FFCC;")
        game_layout.addWidget(self.lbl_status)

        self.progress_bar = QProgressBar()
        self.progress_bar.setRange(0, 100)
        self.progress_bar.setValue(0)
        self.progress_bar.setStyleSheet("""
            QProgressBar { border: 2px solid #00A2FF; border-radius: 8px; text-align: center; color: #FFFFFF; font-weight: bold; background-color: #001F3F; }
            QProgressBar::chunk { background-color: #00FFCC; border-radius: 6px; }
        """)
        game_layout.addWidget(self.progress_bar)

        # Bảng Cần Joystick 4 Hướng D-Pad
        dpad_widget = QWidget()
        dpad_grid = QGridLayout(dpad_widget)
        dpad_grid.setSpacing(6)

        btn_up = QPushButton("Tiến (Lên)")
        btn_up.setProperty("class", "btn-secondary")
        btn_up.setStyleSheet("font-size: 13px; font-weight: bold; color: #FFFFFF; padding: 8px;")
        btn_up.clicked.connect(lambda: self.dieu_khien_joystick("up"))

        btn_down = QPushButton("Lùi (Xuống)")
        btn_down.setProperty("class", "btn-secondary")
        btn_down.setStyleSheet("font-size: 13px; font-weight: bold; color: #FFFFFF; padding: 8px;")
        btn_down.clicked.connect(lambda: self.dieu_khien_joystick("down"))

        btn_left = QPushButton("Sang Trái")
        btn_left.setProperty("class", "btn-secondary")
        btn_left.setStyleSheet("font-size: 13px; font-weight: bold; color: #FFFFFF; padding: 8px;")
        btn_left.clicked.connect(lambda: self.dieu_khien_joystick("left"))

        btn_right = QPushButton("Sang Phải")
        btn_right.setProperty("class", "btn-secondary")
        btn_right.setStyleSheet("font-size: 13px; font-weight: bold; color: #FFFFFF; padding: 8px;")
        btn_right.clicked.connect(lambda: self.dieu_khien_joystick("right"))

        dpad_grid.addWidget(btn_up, 0, 1)
        dpad_grid.addWidget(btn_left, 1, 0)
        dpad_grid.addWidget(btn_right, 1, 2)
        dpad_grid.addWidget(btn_down, 2, 1)

        game_layout.addWidget(dpad_widget)

        # Nút GẮP THÚ BẮT ĐẦU
        self.btn_gap = QPushButton("GẮP THÚ NGAY (1 VÉ GẮP)")
        self.btn_gap.setProperty("class", "btn-primary")
        self.btn_gap.setStyleSheet("font-size: 18px; font-weight: bold; color: #FFFFFF; padding: 14px 28px; background: linear-gradient(135deg, #EC4899, #A855F7);")
        self.btn_gap.clicked.connect(self.bat_dau_gap)
        game_layout.addWidget(self.btn_gap)

        # Bảng chú thích Hướng dẫn Điều kiện Kiếm Vé
        lbl_huong_dan = QLabel(
            "HƯỚNG DẪN ĐIỀU KIỆN KIẾM VÉ GẮP:\n"
            "Vé Gắp Thường: Điểm danh mỗi ngày (+3 Vé) | Hoàn thành 1 bài học (+1 Vé) | Đúng 10 câu liên tiếp (+1 Vé) | Nhiệm vụ ngày (+2 Vé)\n"
            "Vé Vàng (Golden Ticket): Điểm danh mỗi ngày (+1 Vé) | Đạt điểm 10 kiểm tra (+1 Vé) | Chuỗi Streak 7 ngày (+1 Vé)"
        )
        lbl_huong_dan.setWordWrap(True)
        lbl_huong_dan.setStyleSheet(
            "background-color: #0F172A; color: #00FFCC; font-size: 13px; font-weight: bold; "
            "border: 2px solid #06B6D4; border-radius: 12px; padding: 10px; margin-top: 10px;"
        )
        game_layout.addWidget(lbl_huong_dan)

        main_layout.addWidget(game_frame)

    def doi_may_gap(self, index):
        self.may_duoc_chon = self.cbo_may_gap.currentData()
        may_obj = CAC_MAY_GAP.get(self.may_duoc_chon, {})
        self.lbl_status.setText(f"{may_obj.get('ten', 'Máy Gắp')}: {may_obj.get('mo_ta', '')}")

    def dieu_khien_joystick(self, huong):
        if self.dang_gap:
            return
        huong_map = {
            "up": "Tay gắp di chuyển Tiến lên phía trước",
            "down": "Tay gắp di chuyển Lùi lại phía sau",
            "left": "Tay gắp di chuyển Sang Trái",
            "right": "Tay gắp di chuyển Sang Phải"
        }
        self.lbl_status.setText(huong_map.get(huong, "Đang di chuyển tay gắp"))

    def cap_nhat_giao_dien_tai_san(self):
        data = lay_du_lieu_gap_thu()
        self.lbl_ve_gap.setText(f"Vé Gắp: {data.get('ve_gap', 0)} Vé")
        self.lbl_ve_vang.setText(f"Vé Vàng: {data.get('ve_vang', 0)} Vé")
        self.lbl_combo.setText(f"Combo: {data.get('combo_streak', 0)}x")

    def bat_dau_gap(self):
        if self.dang_gap:
            return

        su_dung_ve_vang = (self.may_duoc_chon == "golden")
        ok, res, data = thuc_hien_luot_gap_moi(may_id=self.may_duoc_chon, su_dung_ve_vang=su_dung_ve_vang)
        
        if not ok:
            QMessageBox.warning(self, "Thông báo", res)
            return

        self.dang_gap = True
        self.btn_gap.setEnabled(False)
        self.result_temp = res
        self.progress_value = 0
        self.progress_bar.setValue(0)
        self.lbl_status.setText("Tay gắp 3D đang từ từ hạ xuống đống thú bông...")
        
        self.timer_gap.start(40)
        
        self.time_remaining = 20
        self.timer_countdown.start(1000)

    def dem_nguoc_thoi_gian(self):
        self.time_remaining -= 1
        self.lbl_timer.setText(f"Thời gian: {self.time_remaining}s")
        if self.time_remaining <= 0:
            self.timer_countdown.stop()

    def cap_nhat_tien_trinh_gap(self):
        self.progress_value += 2
        self.progress_bar.setValue(self.progress_value)

        if self.progress_value == 40:
            self.lbl_status.setText("Tay gắp kẹp chặt vật phẩm và kéo lên...")
        elif self.progress_value == 70:
            self.lbl_status.setText("Tay gắp di chuyển sang khay nhận thưởng...")
        elif self.progress_value >= 100:
            self.timer_gap.stop()
            self.timer_countdown.stop()
            self.hoan_thanh_gap()

    def hoan_thanh_gap(self):
        self.dang_gap = False
        self.btn_gap.setEnabled(True)
        res = self.result_temp
        
        self.lbl_status.setText(res["thong_bao"])
        self.cap_nhat_giao_dien_tai_san()

    def hien_thi_bo_suu_tap(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("BỘ SƯU TẬP VẬT PHẨM (COLLECTIONS)")
        dialog.resize(500, 400)
        layout = QVBoxLayout(dialog)

        data = lay_du_lieu_gap_thu()
        bo_data = data.get("bo_suu_tap", {})

        for key, info in DANH_MUC_BO_SUU_TAP.items():
            da_co = bo_data.get(key, [])
            tong = len(info["danh_sach"])
            lbl = QLabel(f"{info['ten']}: Đã thu thập {len(da_co)}/{tong} ({', '.join(da_co) if da_co else 'Chưa có'})")
            lbl.setStyleSheet("font-size: 13px; font-weight: bold; color: #FFFFFF; margin: 4px 0;")
            layout.addWidget(lbl)

        btn_close = QPushButton("Đóng")
        btn_close.clicked.connect(dialog.accept)
        layout.addWidget(btn_close)
        dialog.exec()

    def hien_thi_nhiem_vu(self):
        QMessageBox.information(
            self, "Nhiệm Vụ Kiếm Vé",
            "CÁCH KIẾM VÉ GẮP TỪ HỌC TẬP:\n\n"
            "1. Hoàn thành 1 Bài học -> +1 Vé Gắp\n"
            "2. Trả lời đúng 10 câu liên tiếp -> +1 Vé Gắp\n"
            "3. Hoàn thành Nhiệm vụ ngày -> +2 Vé Gắp\n"
            "4. Đạt điểm 10 Bài kiểm tra / Streak 7 ngày -> +1 VÉ VÀNG (Golden Ticket)"
        )
