# Thu muc: giao_dien
# File: man_hinh_obby.py
# Mo ta: Man hinh Dau truong Obby 100 Man Parkour Vuot Chuong Ngoai Vat Glitch World sang Tieng Viet co dau

import os
import random
from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, 
    QPushButton, QFrame, QMessageBox, QScrollArea, QGridLayout,
    QComboBox, QProgressBar, QInputDialog
)
from PyQt6.QtCore import QTimer, Qt
from PyQt6.QtGui import QPixmap

from xu_ly_tro_choi.quan_ly_obby import (
    lay_danh_sach_10_world, lay_thong_tin_man_obby,
    doc_tien_do_obby, luu_hoan_thanh_man_obby
)
from xu_ly_tro_choi.quan_ly_checkpoint import tinh_man_checkpoint_gan_nhat
from xu_ly_tro_choi.quan_ly_luot_choi import lay_so_luot_choi_obby, su_dung_luot_choi_obby
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
        self.obby_mang = 3 # 3 Mang choi trong 1 luot
        self.dang_choi = False
        self.da_tam_dung = False

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
        
        self.lbl_luot_obby = QLabel("Số lượt chơi Obby khả dụng: 1 lượt (Hoàn thành 1 bài luyện tập để nhận +1 lượt)")
        self.lbl_luot_obby.setStyleSheet("font-size: 15px; font-weight: bold; color: #00FFCC;")

        info_vbox.addWidget(self.lbl_core_progress)
        info_vbox.addWidget(self.lbl_luot_obby)

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

        # 5. Thanh Nút Bấm Thao Tác Chạy Nhảy, Dừng Lại & Nộp Bài
        nav_layout = QHBoxLayout()
        self.btn_action_jump = QPushButton("BẮT ĐẦU VƯỢT MÀN OBBY")
        self.btn_action_jump.setProperty("class", "btn-primary")
        self.btn_action_jump.setStyleSheet("color: #FFFFFF; font-weight: bold; font-size: 15px; padding: 10px 24px; background: linear-gradient(135deg, #EC4899, #A855F7); border-radius: 8px;")
        self.btn_action_jump.setCursor(Qt.CursorShape.PointingHandCursor)
        self.btn_action_jump.clicked.connect(self.xu_ly_nut_chinh_obby)

        self.btn_dung_obby = QPushButton("DỪNG / TẠM DỪNG THỬ THÁCH")
        self.btn_dung_obby.setProperty("class", "btn-secondary")
        self.btn_dung_obby.setStyleSheet("color: #FFFFFF; font-weight: bold; font-size: 14px; padding: 10px 20px; background-color: #DC2626; border-radius: 8px;")
        self.btn_dung_obby.setCursor(Qt.CursorShape.PointingHandCursor)
        self.btn_dung_obby.clicked.connect(self.xu_ly_dung_thu_thach_parkour)

        self.btn_choi_lai = QPushButton("CHƠI LẠI TỪ ĐẦU MÀN")
        self.btn_choi_lai.setProperty("class", "btn-secondary")
        self.btn_choi_lai.setStyleSheet("color: #FFFFFF; font-weight: bold; font-size: 14px; padding: 10px 18px; background-color: #475569; border-radius: 8px;")
        self.btn_choi_lai.setCursor(Qt.CursorShape.PointingHandCursor)
        self.btn_choi_lai.clicked.connect(self.choi_lai_man_tu_dau)
        self.btn_choi_lai.hide()

        self.btn_submit_obby = QPushButton("NỘP BÀI & CHẠM CHECKPOINT")
        self.btn_submit_obby.setProperty("class", "btn-success")
        self.btn_submit_obby.setStyleSheet("color: #FFFFFF; font-weight: bold; font-size: 15px; padding: 10px 24px; border-radius: 8px;")
        self.btn_submit_obby.setCursor(Qt.CursorShape.PointingHandCursor)
        self.btn_submit_obby.clicked.connect(self.tong_ket_man_obby)

        nav_layout.addWidget(self.btn_action_jump)
        nav_layout.addWidget(self.btn_dung_obby)
        nav_layout.addWidget(self.btn_choi_lai)
        nav_layout.addStretch()
        nav_layout.addWidget(self.btn_submit_obby)

        main_layout.addLayout(nav_layout)

        # Tai du lieu ban dau
        self.tai_lai_ban_do()

    def tai_lai_ban_do(self):
        """Cập nhật giao diện thanh Glitch Cores, số lượt chơi Obby và lưới 10 Nút Màn chơi."""
        self.tien_do = doc_tien_do_obby()
        cores = self.tien_do.get("cores_da_lay", [])
        man_max = self.tien_do.get("man_cao_nhat", 1)
        self.lbl_core_progress.setText(f"Số Glitch Cores đã thu thập: {len(cores)} / 10 Cores | Checkpoint cao nhất mở khóa: Màn {man_max}")

        luot_con_lai = lay_so_luot_choi_obby()
        self.lbl_luot_obby.setText(f"Số lượt chơi Obby khả dụng: {luot_con_lai} lượt (Hoàn thành 1 bài luyện tập để nhận thêm +1 lượt)")

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
        self.da_tam_dung = False
        self.man_hien_tai = lvl
        self.cap_nhat_luoi_man_choi()
        self.bat_dau_man_obby()

    def xu_ly_nut_chinh_obby(self):
        """Bấm nút chính: Bắt đầu màn mới hoặc Tiếp tục màn chơi đã tạm dừng."""
        if getattr(self, 'da_tam_dung', False):
            self.tiep_tuc_man_obby()
        else:
            self.bat_dau_man_obby()

    def tiep_tuc_man_obby(self):
        """Tiếp tục màn chơi Obby với thời gian và vị trí Cục Parkour đã lưu."""
        self.dang_choi = True
        self.da_tam_dung = False
        self.btn_action_jump.setText("BẮT ĐẦU VƯỢT MÀN OBBY")
        self.btn_dung_obby.setText("DỪNG / TẠM DỪNG THỬ THÁCH")
        self.btn_choi_lai.hide()
        self.btn_submit_obby.setEnabled(True)
        self.lbl_timer_obby.setStyleSheet("font-size: 15px; font-weight: bold; color: #FFFFFF; background-color: #002B4D; padding: 6px 14px; border-radius: 10px; border: 2px solid #00A2FF;")
        
        m = self.thoi_gian_con_lai // 60
        s = self.thoi_gian_con_lai % 60
        self.lbl_timer_obby.setText(f"Thời gian vượt màn còn lại: {m:02d}:{s:02d}")
        self.hien_thi_cau_hoi_cuc_parkour()
        self.timer.start(1000)

    def choi_lai_man_tu_dau(self):
        """Chơi lại từ đầu màn hiện tại (Cục Parkour 1 và đặt lại thời gian đầy đủ)."""
        self.da_tam_dung = False
        self.btn_action_jump.setText("BẮT ĐẦU VƯỢT MÀN OBBY")
        self.btn_dung_obby.setText("DỪNG / TẠM DỪNG THỬ THÁCH")
        self.btn_choi_lai.hide()
        self.btn_submit_obby.setEnabled(True)
        self.bat_dau_man_obby()

    def bat_dau_man_obby(self):
        """Bắt đầu màn chơi Obby hiện tại với cơ chế 6 Cục Parkour (6 Câu hỏi) - Chỉ trừ lượt khi trả lời câu hỏi."""
        if getattr(self, 'da_tam_dung', False):
            self.tiep_tuc_man_obby()
            return

        if lay_so_luot_choi_obby() <= 0:
            QMessageBox.warning(
                self,
                "HẾT LƯỢT CHƠI OBBY",
                "Em đã dùng hết lượt chơi Đấu trường Obby!\n\n"
                "Hãy qua mục 'Luyện tập Roblox' hoặc 'Nội dung học tập' và hoàn thành 1 bài luyện tập để nhận ngay +1 LƯỢT CHƠI OBBY nhé!"
            )
            self.lbl_luot_obby.setText("Số lượt chơi Obby khả dụng: 0 lượt (Hoàn thành 1 bài luyện tập để nhận thêm +1 lượt)")
            return

        self.dang_choi = True
        self.da_tam_dung = False
        self.da_tinh_luot_obby_man_nay = False
        luot_con_lai = lay_so_luot_choi_obby()
        self.lbl_luot_obby.setText(f"Số lượt chơi Obby khả dụng: {luot_con_lai} lượt (Hoàn thành 1 bài luyện tập để nhận thêm +1 lượt)")

        self.btn_action_jump.setText("BẮT ĐẦU VƯỢT MÀN OBBY")
        self.btn_dung_obby.setText("DỪNG / TẠM DỪNG THỬ THÁCH")
        self.btn_choi_lai.hide()
        self.btn_submit_obby.setEnabled(True)
        self.lbl_timer_obby.setStyleSheet("font-size: 15px; font-weight: bold; color: #FFFFFF; background-color: #002B4D; padding: 6px 14px; border-radius: 10px; border: 2px solid #00A2FF;")

        self.obby_step = 0
        info = lay_thong_tin_man_obby(self.man_hien_tai)
        self.lbl_level_title.setText(f"{info['ten_man'].upper()} - {info['ten_world'].upper()}")
        self.lbl_mechanic_desc.setText(f"Cơ chế: Vượt qua 6 Cục Parkour (6 Câu hỏi). Thời gian: {info['thoi_gian_lim']} giây. Thưởng: +{info['thuong_xp']} Roblox XP!")

        # Sinh 6 câu hỏi thử thách cho 6 Cục Parkour
        cau_hoi_list = chay_javascript_sinh_de("Lớp 6", "Toán", f"Obby {info['ten_world']}", 6)
        if cau_hoi_list and len(cau_hoi_list) >= 6:
            self.danh_sach_6_cau_hoi = cau_hoi_list[:6]
        else:
            self.danh_sach_6_cau_hoi = [
                {"cau_hoi": f"CụC PARKOUR 1/6 (Màn {self.man_hien_tai}): Phân số tối giản là phân số nào?", "dap_an": ["Không thể rút gọn thêm", "Có tử bằng 0", "Có mẫu bằng 1"], "dap_an_dung": "Không thể rút gọn thêm"},
                {"cau_hoi": f"CụC PARKOUR 2/6 (Màn {self.man_hien_tai}): Công thức diện tích hình vuông là gì?", "dap_an": ["cạnh x cạnh", "cạnh x 4", "cạnh + cạnh"], "dap_an_dung": "cạnh x cạnh"},
                {"cau_hoi": f"CụC PARKOUR 3/6 (Màn {self.man_hien_tai}): Tam giác đều có đặc điểm gì?", "dap_an": ["3 cạnh bằng nhau", "2 cạnh bằng nhau", "3 góc vuông"], "dap_an_dung": "3 cạnh bằng nhau"},
                {"cau_hoi": f"CụC PARKOUR 4/6 (Màn {self.man_hien_tai}): Số nguyên tố nhỏ nhất là số nào?", "dap_an": ["Số 2", "Số 1", "Số 0"], "dap_an_dung": "Số 2"},
                {"cau_hoi": f"CụC PARKOUR 5/6 (Màn {self.man_hien_tai}): Công thức chu vi hình vuông?", "dap_an": ["cạnh x 4", "cạnh x 2", "cạnh x cạnh"], "dap_an_dung": "cạnh x 4"},
                {"cau_hoi": f"CụC PARKOUR 6/6 - ĐÍCH ĐẾN (Màn {self.man_hien_tai}): 1 mét bằng bao nhiêu xentimét?", "dap_an": ["100 xentimét", "10 xentimét", "1000 xentimét"], "dap_an_dung": "100 xentimét"}
            ]

        self.hien_thi_cau_hoi_cuc_parkour()
        self.thoi_gian_con_lai = info["thoi_gian_lim"]
        self.timer.start(1000)

    def tru_luot_choi_obby_neu_can(self):
        """Trừ lượt chơi Obby khi học sinh chọn đáp án cho Cục Parkour đầu tiên."""
        if not getattr(self, 'da_tinh_luot_obby_man_nay', False):
            if su_dung_luot_choi_obby():
                self.da_tinh_luot_obby_man_nay = True
                luot_con_lai = lay_so_luot_choi_obby()
                self.lbl_luot_obby.setText(f"Số lượt chơi Obby khả dụng: {luot_con_lai} lượt (Hoàn thành 1 bài luyện tập để nhận thêm +1 lượt)")

    def dung_hoat_dong(self):
        """Dừng đồng hồ đếm ngược và bảo lưu trạng thái để học sinh có thể tiếp tục khi quay lại."""
        if hasattr(self, 'timer') and self.timer.isActive():
            self.timer.stop()
        
        if getattr(self, 'dang_choi', False):
            # Lưu tiến độ đang chơi dở dang
            self.da_tam_dung = True
            self.dang_choi = False
            m = self.thoi_gian_con_lai // 60
            s = self.thoi_gian_con_lai % 60
            if hasattr(self, 'lbl_timer_obby'):
                self.lbl_timer_obby.setText(f"Thời gian vượt màn: ĐÃ TẠM DỪNG (Còn lại: {m:02d}:{s:02d})")
                self.lbl_timer_obby.setStyleSheet("font-size: 15px; font-weight: bold; color: #FFFFFF; background-color: #B45309; padding: 6px 14px; border-radius: 10px; border: 2px solid #F59E0B;")
            if hasattr(self, 'lbl_question_text'):
                self.lbl_question_text.setText(f"Đã tạm dừng thử thách tại Cục Parkour {self.obby_step + 1}/6. Bấm 'TIẾP TỤC VƯỢT MÀN' để nhảy tiếp hoặc 'CHƠI LẠI TỪ ĐẦU MÀN'!")
            if hasattr(self, 'btn_action_jump'):
                self.btn_action_jump.setText("TIẾP TỤC VƯỢT MÀN")
            if hasattr(self, 'btn_dung_obby'):
                self.btn_dung_obby.setText("THOÁT HẲN MÀN CHƠI")
            if hasattr(self, 'btn_choi_lai'):
                self.btn_choi_lai.show()
            if hasattr(self, 'btn_submit_obby'):
                self.btn_submit_obby.setEnabled(False)
        else:
            if not getattr(self, 'da_tam_dung', False):
                self.dang_choi = False
                self.thoi_gian_con_lai = 0
                if hasattr(self, 'lbl_timer_obby'):
                    self.lbl_timer_obby.setText("Thời gian vượt màn: Đã dừng (Chưa bắt đầu)")
                    self.lbl_timer_obby.setStyleSheet("font-size: 15px; font-weight: bold; color: #FFFFFF; background-color: #002B4D; padding: 6px 14px; border-radius: 10px; border: 2px solid #00A2FF;")
                if hasattr(self, 'lbl_question_text'):
                    self.lbl_question_text.setText("Thử thách Parkour đã dừng. Bấm 'BẮT ĐẦU VƯỢT MÀN OBBY' để nhận thử thách Parkour!")
                if hasattr(self, 'btn_action_jump'):
                    self.btn_action_jump.setText("BẮT ĐẦU VƯỢT MÀN OBBY")
                if hasattr(self, 'btn_dung_obby'):
                    self.btn_dung_obby.setText("DỪNG / TẠM DỪNG THỬ THÁCH")
                if hasattr(self, 'btn_choi_lai'):
                    self.btn_choi_lai.hide()
                if hasattr(self, 'btn_submit_obby'):
                    self.btn_submit_obby.setEnabled(True)
                
                # Xóa các thẻ phương án nếu thoát hẳn
                if hasattr(self, 'vung_options_layout'):
                    for i in reversed(range(self.vung_options_layout.count())):
                        w = self.vung_options_layout.itemAt(i).widget()
                        if w:
                            w.setParent(None)
                self.cau_hoi_current = None
                self.dap_an_user = ""

    def xu_ly_dung_thu_thach_parkour(self):
        """Học sinh chủ động bấm Dừng / Tạm dừng màn chơi Parkour hiện tại."""
        if getattr(self, 'dang_choi', False):
            self.dung_hoat_dong()
            m = self.thoi_gian_con_lai // 60
            s = self.thoi_gian_con_lai % 60
            QMessageBox.information(
                self,
                "ĐÃ TẠM DỪNG THỬ THÁCH",
                f"Đã dừng đồng hồ đếm ngược và tạm dừng màn Parkour {self.man_hien_tai}!\n\n"
                f"Tiến độ tại Cục Parkour {self.obby_step + 1}/6 và thời gian còn lại ({m:02d}:{s:02d}) được lưu an toàn.\n"
                f"Em có thể bấm 'TIẾP TỤC VƯỢT MÀN' bất cứ lúc nào!"
            )
        elif getattr(self, 'da_tam_dung', False):
            # Nếu đang tạm dừng mà bấm tiếp nút thoát -> Thoát hẳn màn chơi
            self.da_tam_dung = False
            self.dung_hoat_dong()
            QMessageBox.information(
                self,
                "ĐÃ THOÁT MÀN CHƠI",
                "Đã thoát khỏi màn chơi hiện tại. Khi sẵn sàng, em có thể bấm 'BẮT ĐẦU VƯỢT MÀN OBBY' để thử sức lại từ đầu!"
            )
        else:
            self.dung_hoat_dong()

    def hien_thi_cau_hoi_cuc_parkour(self):
        if not hasattr(self, 'danh_sach_6_cau_hoi') or self.obby_step >= len(self.danh_sach_6_cau_hoi):
            return

        self.cau_hoi_current = self.danh_sach_6_cau_hoi[self.obby_step]
        self.lbl_question_text.setText(f"[CỤC PARKOUR {self.obby_step + 1} / 6] - Màn {self.man_hien_tai}: {self.cau_hoi_current['cau_hoi']}")

        # Clear vung options
        for i in reversed(range(self.vung_options_layout.count())):
            w = self.vung_options_layout.itemAt(i).widget()
            if w:
                w.setParent(None)

        widget_options = TheDapAnGroup(self.cau_hoi_current["dap_an"], dap_an_hien_tai="")
        widget_options.dap_an_thay_doi.connect(self.luu_dap_an_va_nhay)
        self.vung_options_layout.addWidget(widget_options)

    def luu_dap_an_va_nhay(self, text):
        if not getattr(self, 'dang_choi', False):
            return
        self.dap_an_user = text
        if text and str(text).strip():
            self.tru_luot_choi_obby_neu_can()
        self.tong_ket_man_obby()

    def cap_nhat_dong_ho(self):
        if not getattr(self, 'dang_choi', False):
            self.timer.stop()
            return

        if self.thoi_gian_con_lai > 0:
            self.thoi_gian_con_lai -= 1
            m = self.thoi_gian_con_lai // 60
            s = self.thoi_gian_con_lai % 60
            self.lbl_timer_obby.setText(f"Thời gian vượt màn còn lại: {m:02d}:{s:02d}")
        else:
            self.timer.stop()
            self.dang_choi = False
            man_checkpoint = tinh_man_checkpoint_gan_nhat(self.man_hien_tai)
            QMessageBox.warning(
                self,
                "HẾT THỜI GIAN VƯỢT MÀN",
                f"Hết thời gian vượt Màn {self.man_hien_tai}!\n"
                f"Quy tắc game: Cứ 5 màn có 1 điểm Checkpoint.\n"
                f"Bạn sẽ xuất phát lại từ Điểm Checkpoint gần nhất (Màn {man_checkpoint})."
            )
            self.man_hien_tai = man_checkpoint
            self.obby_mang = 3
            self.cap_nhat_luoi_man_choi()
            self.bat_dau_man_obby()

    def tong_ket_man_obby(self):
        if not getattr(self, 'dang_choi', False):
            return
        if not self.cau_hoi_current:
            return

        info = lay_thong_tin_man_obby(self.man_hien_tai)
        dap_an_dung = str(self.cau_hoi_current.get("dap_an_dung", "")).strip()
        dap_an_user_str = str(self.dap_an_user).strip()

        if dap_an_user_str == dap_an_dung:
            self.obby_step += 1
            if self.obby_step < 6:
                self.hien_thi_cau_hoi_cuc_parkour()
            else:
                self.timer.stop()
                self.dang_choi = False
                cong_phan_thuong(10.0, 1)
                luu_hoan_thanh_man_obby(self.man_hien_tai)
                self.tai_lai_ban_do()

                if info["is_boss"]:
                    QMessageBox.information(
                        self,
                        "YOU ESCAPED THE GLITCH WORLD",
                        "YOU ESCAPED THE GLITCH WORLD!\n\n"
                        "Chúc mừng bạn đã hoàn thành 6 Cục Parkour Màn 100, đánh bại Boss Glitch-X và thu thập đủ 10 Glitch Cores để kích hoạt MASTER CORE!\n"
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
                        "CHẠM CHECKPOINT 5 MÀN THÀNH CÔNG",
                        f"XUẤT SẮC! Bạn đã vượt qua {info['ten_man'].upper()} ({info['ten_world'].upper()})!\n"
                        f"Đã kích hoạt ĐIỂM CHECKPOINT 5 MÀN (Màn {self.man_hien_tai + 1})!\n"
                        f"Thưởng +{info['thuong_xp']} Roblox XP!"
                    )
                    self.man_hien_tai += 1
                    self.bat_dau_man_obby()
                else:
                    QMessageBox.information(
                        self,
                        "VƯỢT MÀN OBBY THÀNH CÔNG",
                        f"XUẤT SẮC! Bạn đã vượt qua 6 Cục Parkour Màn {info['ten_man'].upper()}!\nThưởng +{info['thuong_xp']} Roblox XP!"
                    )
                    self.man_hien_tai += 1
                    self.bat_dau_man_obby()
        else:
            self.obby_mang -= 1
            if self.obby_mang > 0:
                QMessageBox.warning(
                    self,
                    "ĐÁP ÁN CHƯA CHÍNH XÁC",
                    f"Rất tiếc! Đáp án chưa chính xác. Bạn bị trừ 1 mạng chơi (Còn {self.obby_mang}/3 mạng).\n"
                    f"Hãy thử lại câu hỏi tại Cục Parkour {self.obby_step + 1}!"
                )
            else:
                self.timer.stop()
                self.dang_choi = False
                man_checkpoint = tinh_man_checkpoint_gan_nhat(self.man_hien_tai)
                QMessageBox.warning(
                    self,
                    "BẠN ĐÃ HẾT MẠNG CHƠI",
                    f"Bạn đã hết mạng chơi tại Màn {info['ten_man']}!\n"
                    f"Theo quy tắc Checkpoint (5 màn có 1 điểm Checkpoint), bạn sẽ xuất phát lại từ Màn {man_checkpoint}."
                )
                self.man_hien_tai = man_checkpoint
                self.obby_mang = 3
                self.cap_nhat_luoi_man_choi()
                self.bat_dau_man_obby()

    def hideEvent(self, event):
        """Khi chuyển sang màn hình khác hoặc thoát khỏi phần Parkour, dừng ngay đồng hồ và dừng hoạt động."""
        self.dung_hoat_dong()
        super().hideEvent(event)
