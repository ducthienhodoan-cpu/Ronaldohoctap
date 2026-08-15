# Thu muc: giao_dien
# File: man_hinh_obby.py
# Mo ta: Man hinh Dau truong Obby 100 Man Parkour Vuot Chuong Ngoai Vat Glitch World sang Tieng Viet co dau

import os
import random
from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, 
    QPushButton, QFrame, QMessageBox, QScrollArea, QGridLayout,
    QComboBox, QProgressBar
)
from PyQt6.QtCore import QTimer, Qt
from PyQt6.QtGui import QPixmap

from xu_ly_tro_choi.quan_ly_obby import (
    lay_danh_sach_10_world, lay_thong_tin_man_obby,
    doc_tien_do_obby, luu_hoan_thanh_man_obby
)
from xu_ly_kiem_tra.dong_co_javascript import chay_javascript_sinh_de
from xu_ly_hoc_tap.he_thong_thuong import cong_phan_thuong
from giao_dien.dap_an_tuong_tac import TheDapAnGroup
from giao_dien.hop_thoai_chung_nhan import HopThoaiChungNhan

class ManHinhObby(QWidget):
    """Màn hình Đấu trường Obby 100 Màn Parkour Vượt Chướng Ngại Vật Glitch World."""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.danh_sach_world = lay_danh_sach_10_world()
        self.tien_do = doc_tien_do_obby()
        self.man_hien_tai = self.tien_do.get("man_hien_tai", 1)
        self.world_selected_idx = 0
        self.cau_hoi_current = None
        self.dap_an_user = ""
        self.thoi_gian_con_lai = 45
        self.boss_phase = 1

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.cap_nhat_dong_ho)

        self.path_mascot_3d = r"C:\Users\Admin\.gemini\antigravity-ide\brain\fcb0a507-c860-48bb-bc03-3398a0afb7bf\world_cup_player_3d_mascot_1785124545093.png"

        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(15, 15, 15, 15)
        main_layout.setSpacing(12)

        # 1. Tiêu đề Obby 100 Màn Parkour
        title_label = QLabel("ĐẤU TRƯỜNG OBBY 100 MÀN PARKOUR VƯỢT CHƯỚNG NGẠI VẬT - GLITCH WORLD")
        title_label.setStyleSheet("font-size: 20px; font-weight: bold; color: #FFFFFF;")
        main_layout.addWidget(title_label)

        # 2. Khung Header Tiến trình 10 Glitch Cores & Chọn World
        header_frame = QFrame()
        header_frame.setStyleSheet(
            "QFrame { "
            "   background-color: #111214; "
            "   border: 2px solid #A855F7; "
            "   border-radius: 12px; "
            "   padding: 10px; "
            "}"
        )
        header_layout = QHBoxLayout(header_frame)
        header_layout.setSpacing(15)

        # Ảnh 3D Mascot Obby
        self.lbl_img_mascot = QLabel()
        self.lbl_img_mascot.setFixedSize(90, 90)
        self.lbl_img_mascot.setScaledContents(True)
        if os.path.exists(self.path_mascot_3d):
            self.lbl_img_mascot.setPixmap(QPixmap(self.path_mascot_3d))
        header_layout.addWidget(self.lbl_img_mascot)

        info_vbox = QVBoxLayout()
        self.lbl_core_progress = QLabel("Số Glitch Cores đã thu thập: 0 / 10 Cores | Checkpoint cao nhất: Màn 1")
        self.lbl_core_progress.setStyleSheet("font-size: 15px; font-weight: bold; color: #06B6D4;")
        info_vbox.addWidget(self.lbl_core_progress)

        row_sel = QHBoxLayout()
        lbl_world = QLabel("Chọn World Obby:")
        lbl_world.setStyleSheet("color: #FFFFFF; font-weight: bold;")
        self.cbo_world = QComboBox()
        self.cbo_world.setStyleSheet("color: #FFFFFF; font-weight: bold; font-size: 14px;")
        for w in self.danh_sach_world:
            self.cbo_world.addItem(f"{w['ten']} ({w['vong']})")
        self.cbo_world.currentIndexChanged.connect(self.thay_doi_world)

        btn_refresh_map = QPushButton("Tải lại bản đồ Obby")
        btn_refresh_map.setProperty("class", "btn-secondary")
        btn_refresh_map.setStyleSheet("color: #FFFFFF; font-weight: bold;")
        btn_refresh_map.clicked.connect(self.tai_lai_ban_do)

        row_sel.addWidget(lbl_world)
        row_sel.addWidget(self.cbo_world, 2)
        row_sel.addWidget(btn_refresh_map)
        info_vbox.addLayout(row_sel)

        header_layout.addLayout(info_vbox, 2)
        main_layout.addWidget(header_frame)

        # 3. Lưới 10 Nút Màn chơi thuộc World đang chọn
        self.grid_levels_frame = QFrame()
        self.grid_levels_frame.setProperty("class", "card-widget")
        self.grid_levels_layout = QHBoxLayout(self.grid_levels_frame)
        self.grid_levels_layout.setSpacing(8)
        main_layout.addWidget(self.grid_levels_frame)

        # 4. Vùng thi đấu Obby Parkour & Trả lời câu hỏi Tri thức (QScrollArea)
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setStyleSheet("QScrollArea { border: none; background-color: transparent; }")

        self.stadium_frame = QFrame()
        self.stadium_frame.setProperty("class", "card-widget")
        stadium_layout = QVBoxLayout(self.stadium_frame)
        stadium_layout.setContentsMargins(15, 15, 15, 15)

        self.lbl_level_title = QLabel("MÀN 1 - THE BEGINNING (WORLD 1 - GLITCH CITY)")
        self.lbl_level_title.setStyleSheet("font-size: 18px; font-weight: bold; color: #F59E0B;")
        stadium_layout.addWidget(self.lbl_level_title)

        self.lbl_mechanic_desc = QLabel("Cơ chế: Obby cơ bản + thành phố bị lỗi. Chạy nhảy vượt qua các platform và chạm Checkpoint!")
        self.lbl_mechanic_desc.setStyleSheet("font-size: 14px; color: #CBD5E1; font-weight: bold; margin-bottom: 8px;")
        self.lbl_mechanic_desc.setWordWrap(True)
        stadium_layout.addWidget(self.lbl_mechanic_desc)

        self.lbl_timer_obby = QLabel("Thời gian vượt màn: 00:45")
        self.lbl_timer_obby.setStyleSheet("font-size: 15px; font-weight: bold; color: #FFFFFF; background-color: #002B4D; padding: 6px 14px; border-radius: 10px; border: 2px solid #00A2FF;")
        stadium_layout.addWidget(self.lbl_timer_obby)

        self.lbl_question_text = QLabel("Bấm 'BẮT ĐẦU VƯỢT MÀN OBBY' để nhận thử thách Parkour!")
        self.lbl_question_text.setStyleSheet("font-size: 16px; font-weight: bold; color: #FFFFFF; background-color: #111214; padding: 14px; border-radius: 10px; border: 2px solid #A855F7;")
        self.lbl_question_text.setWordWrap(True)
        stadium_layout.addWidget(self.lbl_question_text)

        # Vùng chứa thẻ đáp án
        self.vung_options_container = QWidget()
        self.vung_options_layout = QVBoxLayout(self.vung_options_container)
        stadium_layout.addWidget(self.vung_options_container)

        self.scroll_area.setWidget(self.stadium_frame)
        main_layout.addWidget(self.scroll_area)

        # 5. Thanh Nút Bấm Thao Tác Chạy Nhảy & Nộp Bài
        nav_layout = QHBoxLayout()
        self.btn_action_jump = QPushButton("BẮT ĐẦU VƯỢT MÀN OBBY")
        self.btn_action_jump.setProperty("class", "btn-primary")
        self.btn_action_jump.setStyleSheet("color: #FFFFFF; font-weight: bold; font-size: 15px; padding: 10px 24px; background: linear-gradient(135deg, #EC4899, #A855F7);")
        self.btn_action_jump.clicked.connect(self.bat_dau_man_obby)

        self.btn_submit_obby = QPushButton("NỘP BÀI & CHẠM CHECKPOINT")
        self.btn_submit_obby.setProperty("class", "btn-success")
        self.btn_submit_obby.setStyleSheet("color: #FFFFFF; font-weight: bold; font-size: 15px; padding: 10px 24px;")
        self.btn_submit_obby.clicked.connect(self.tong_ket_man_obby)

        nav_layout.addWidget(self.btn_action_jump)
        nav_layout.addStretch()
        nav_layout.addWidget(self.btn_submit_obby)

        main_layout.addLayout(nav_layout)

        # Tai du lieu ban dau
        self.tai_lai_ban_do()

    def tai_lai_ban_do(self):
        """Cập nhật giao diện thanh Glitch Cores và lưới 10 Nút Màn chơi."""
        self.tien_do = doc_tien_do_obby()
        cores = self.tien_do.get("cores_da_lay", [])
        man_max = self.tien_do.get("man_cao_nhat", 1)
        self.lbl_core_progress.setText(f"Số Glitch Cores đã thu thập: {len(cores)} / 10 Cores | Checkpoint cao nhất mở khóa: Màn {man_max}")

        self.cap_nhat_luoi_man_choi()

    def thay_doi_world(self, index):
        self.world_selected_idx = index
        self.cap_nhat_luoi_man_choi()

    def cap_nhat_luoi_man_choi(self):
        """Vẽ lại 10 nút Màn chơi cho World được chọn."""
        for i in reversed(range(self.grid_levels_layout.count())):
            w = self.grid_levels_layout.itemAt(i).widget()
            if w:
                w.setParent(None)

        start_level = self.world_selected_idx * 10 + 1
        man_max = self.tien_do.get("man_cao_nhat", 1)

        for lvl in range(start_level, start_level + 10):
            btn_lvl = QPushButton(f"Màn {lvl}")
            btn_lvl.setCursor(Qt.CursorShape.PointingHandCursor)
            
            if lvl == self.man_hien_tai:
                btn_lvl.setStyleSheet("color: #FFFFFF; font-weight: bold; background-color: #F59E0B; border: 2px solid #FFFFFF; border-radius: 8px; padding: 8px;")
            elif lvl <= man_max:
                btn_lvl.setStyleSheet("color: #FFFFFF; font-weight: bold; background-color: #10B981; border-radius: 8px; padding: 8px;")
            else:
                btn_lvl.setStyleSheet("color: #FFFFFF; font-weight: bold; background-color: #3B82F6; border-radius: 8px; padding: 8px;")

            btn_lvl.clicked.connect(lambda checked, l=lvl: self.chon_man_choi(l))
            self.grid_levels_layout.addWidget(btn_lvl)

    def chon_man_choi(self, lvl):
        self.man_hien_tai = lvl
        self.cap_nhat_luoi_man_choi()
        self.bat_dau_man_obby()

    def bat_dau_man_obby(self):
        """Bắt đầu màn chơi Obby hiện tại."""
        info = lay_thong_tin_man_obby(self.man_hien_tai)
        self.lbl_level_title.setText(f"{info['ten_man'].upper()} - {info['ten_world'].upper()}")
        self.lbl_mechanic_desc.setText(f"Cơ chế thi đấu: {info['co_che']}. Thời gian: {info['thoi_gian_lim']} giây. Thưởng: +{info['thuong_xp']} Roblox XP!")

        # Sinh câu hỏi thử thách Parkour
        cau_hoi_list = chay_javascript_sinh_de("Lớp 6", "Toán", f"Obby {info['ten_world']}", 1)
        if cau_hoi_list:
            self.cau_hoi_current = cau_hoi_list[0]
            self.lbl_question_text.setText(f"Thử thách tri thức Obby {info['ten_man']}: {self.cau_hoi_current['cau_hoi']}")
            
            # Clear options
            for i in reversed(range(self.vung_options_layout.count())):
                w = self.vung_options_layout.itemAt(i).widget()
                if w:
                    w.setParent(None)

            widget_options = TheDapAnGroup(self.cau_hoi_current["dap_an"], dap_an_hien_tai="")
            widget_options.dap_an_thay_doi.connect(self.luu_dap_an)
            self.vung_options_layout.addWidget(widget_options)

        self.thoi_gian_con_lai = info["thoi_gian_lim"]
        self.timer.start(1000)

    def luu_dap_an(self, text):
        self.dap_an_user = text

    def cap_nhat_dong_ho(self):
        if self.thoi_gian_con_lai > 0:
            self.thoi_gian_con_lai -= 1
            m = self.thoi_gian_con_lai // 60
            s = self.thoi_gian_con_lai % 60
            self.lbl_timer_obby.setText(f"Thời gian vượt màn còn lại: {m:02d}:{s:02d}")
        else:
            self.timer.stop()
            QMessageBox.warning(self, "Hết thời gian Obby", f"Hết thời gian vượt {lay_thong_tin_man_obby(self.man_hien_tai)['ten_man']}! Bạn rơi khỏi sàn parkour và quay lại Checkpoint trước.")
            self.bat_dau_man_obby()

    def tong_ket_man_obby(self):
        self.timer.stop()
        if not self.cau_hoi_current:
            return

        info = lay_thong_tin_man_obby(self.man_hien_tai)
        dap_an_dung = str(self.cau_hoi_current.get("dap_an_dung", "")).strip()
        dap_an_user_str = str(self.dap_an_user).strip()

        if dap_an_user_str == dap_an_dung:
            cong_phan_thuong(10.0, 1)
            luu_hoan_thanh_man_obby(self.man_hien_tai)
            self.tai_lai_ban_do()

            if info["is_boss"]:
                QMessageBox.information(
                    self,
                    "YOU ESCAPED THE GLITCH WORLD",
                    "YOU ESCAPED THE GLITCH WORLD!\n\n"
                    "Chúc mừng bạn đã đánh bại Boss Glitch-X Màn 100 và thu thập đủ 10 Glitch Cores để kích hoạt MASTER CORE!\n"
                    "Cánh cổng thời gian mở ra, đưa bạn trở lại thành phố Glitch City bình yên!\n"
                    f"Thưởng +{info['thuong_xp']} Roblox XP và Mở khóa HARD MODE!"
                )
                dlg_cert = HopThoaiChungNhan(
                    parent=self,
                    lop="Lớp 6",
                    chu_de="MASTER CORE CHAMPION - THẦN THOẠI OBBY 100 MÀN",
                    phan_tram_diem=100,
                    diem_so=10.0
                )
                dlg_cert.exec()
                self.man_hien_tai = 1
                self.bat_dau_man_obby()
            elif info["is_checkpoint"]:
                QMessageBox.information(
                    self,
                    "CHẠM CHECKPOINT THÀNH CÔNG",
                    f"XUẤT SẮC! Bạn đã vượt qua {info['ten_man'].upper()} ({info['ten_world'].upper()})!\n"
                    f"Thu thập thành công GLITCH CORE #{info['so_man'] // 10}!\n"
                    f"Đã lưu Checkpoint! Thưởng +{info['thuong_xp']} Roblox XP!"
                )
                self.man_hien_tai += 1
                self.bat_dau_man_obby()
            else:
                QMessageBox.information(
                    self,
                    "VƯỢT MÀN OBBY THÀNH CÔNG",
                    f"XUẤT SẮC! Bạn đã vượt qua {info['ten_man'].upper()}!\nThưởng +{info['thuong_xp']} Roblox XP!"
                )
                self.man_hien_tai += 1
                self.bat_dau_man_obby()
        else:
            QMessageBox.warning(
                self,
                "VƯỢT MÀN THẤT BẠI",
                f"Rất tiếc! Đáp án chưa chính xác. Bạn trượt chân rơi khỏi platform của {info['ten_man']}!\n"
                f"Đáp án đúng là: {dap_an_dung}. Hãy thử lại từ Checkpoint nhé!"
            )
