# Thu muc: giao_dien
# File: man_hinh_champions_league.py
# Mo ta: Man hinh Giai dau Champions League Tong hop kien thuc 1 Chu de cua 1 Mon hoc voi Cup Tai Voi 3D sang Tieng Viet co dau

import os
import random
from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, 
    QPushButton, QFrame, QMessageBox, QScrollArea, QGridLayout,
    QComboBox, QProgressBar
)
from PyQt6.QtCore import QTimer, Qt, QDate
from PyQt6.QtGui import QPixmap

from du_lieu.kho_noi_dung_hoc import (
    lay_danh_sach_lop, lay_danh_sach_mon_hoc, lay_chu_de_theo_lop_va_mon
)
from xu_ly_tro_choi.quan_ly_champions_league import (
    lay_danh_sach_clb_champions_league, lay_vong_dau_champions_league,
    sinh_tran_dau_champions_league
)
from xu_ly_hoc_tap.he_thong_thuong import cong_phan_thuong
from giao_dien.dap_an_tuong_tac import TheDapAnGroup
from giao_dien.hop_thoai_chung_nhan import HopThoaiChungNhan

class ManHinhChampionsLeague(QWidget):
    """Màn hình Giải đấu UEFA Champions League Tổng hợp kiến thức 1 Chủ đề của 1 Môn học với TẤT CẢ VĂN BẢN ĐỀU LÀ CHỮ TRẮNG SÁNG."""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.danh_sach_clb = lay_danh_sach_clb_champions_league()
        self.clb_user = self.danh_sach_clb[0]
        self.vong_idx = 0
        self.cau_idx = 0
        self.so_ban_thang = 0
        self.cau_hoi_cl = []
        self.dap_an_user = {}
        self.last_played_date = ""
        self.so_luot_hom_nay = 0

        self.thoi_gian_con_lai = 300
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.cap_nhat_dong_ho)

        # Asset path 3D Cúp Tai Voi Champions League
        self.path_trophy_3d = r"C:\Users\Admin\.gemini\antigravity-ide\brain\fcb0a507-c860-48bb-bc03-3398a0afb7bf\champions_league_trophy_3d_1785126400921.png"
        self.path_mascot_3d = r"C:\Users\Admin\.gemini\antigravity-ide\brain\fcb0a507-c860-48bb-bc03-3398a0afb7bf\world_cup_player_3d_mascot_1785124545093.png"

        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(15, 15, 15, 15)
        main_layout.setSpacing(12)

        # 1. Tiêu đề Cúp C1 Champions League chữ trắng
        title_label = QLabel("GIẢI ĐẤU CHAMPIONS LEAGUE - TỔNG HỢP KIẾN THỨC 1 CHỦ ĐỀ CỦA 1 MÔN")
        title_label.setStyleSheet("font-size: 22px; font-weight: bold; color: #FFFFFF;")
        main_layout.addWidget(title_label)

        # 2. Khung Chọn CLB, Chọn Lớp, Môn và 1 Chủ đề tổng hợp chữ trắng
        header_frame = QFrame()
        header_frame.setStyleSheet(
            "QFrame { "
            "   background-color: #111214; "
            "   border: 2px solid #00A2FF; "
            "   border-radius: 12px; "
            "   padding: 10px; "
            "}"
        )
        header_layout = QHBoxLayout(header_frame)
        header_layout.setSpacing(15)

        # Ảnh Mascot 3D Cầu thủ
        self.lbl_img_mascot = QLabel()
        self.lbl_img_mascot.setFixedSize(105, 105)
        self.lbl_img_mascot.setScaledContents(True)
        if os.path.exists(self.path_mascot_3d):
            self.lbl_img_mascot.setPixmap(QPixmap(self.path_mascot_3d))
        header_layout.addWidget(self.lbl_img_mascot)

        # Bộ lọc Chọn CLB, Lớp, Môn và 5 Chủ đề
        info_vbox = QVBoxLayout()
        lbl_select_title = QLabel("Cấu hình Cúp C1 (Chọn CLB Châu Âu, Môn học & 1 Chủ đề - 3 lượt chơi/ngày):")
        lbl_select_title.setStyleSheet("font-size: 15px; font-weight: bold; color: #FFFFFF;")
        info_vbox.addWidget(lbl_select_title)

        row_sel = QHBoxLayout()
        lbl_clb = QLabel("CLB Châu Âu:")
        lbl_clb.setStyleSheet("color: #FFFFFF; font-weight: bold;")
        self.cbo_clb = QComboBox()
        self.cbo_clb.setStyleSheet("color: #FFFFFF; font-weight: bold; font-size: 14px;")
        for c in self.danh_sach_clb:
            self.cbo_clb.addItem(f"CLB {c['ten']}")
        self.cbo_clb.currentIndexChanged.connect(self.thay_doi_clb)

        lbl_lop = QLabel("Lớp:")
        lbl_lop.setStyleSheet("color: #FFFFFF; font-weight: bold;")
        self.cbo_lop = QComboBox()
        self.cbo_lop.setStyleSheet("color: #FFFFFF; font-weight: bold; font-size: 14px;")
        self.cbo_lop.addItems(lay_danh_sach_lop())
        self.cbo_lop.setCurrentText("Lớp 6")
        self.cbo_lop.currentTextChanged.connect(self.thay_doi_lop)

        lbl_mon = QLabel("Môn:")
        lbl_mon.setStyleSheet("color: #FFFFFF; font-weight: bold;")
        self.cbo_mon = QComboBox()
        self.cbo_mon.setStyleSheet("color: #FFFFFF; font-weight: bold; font-size: 14px;")
        self.cbo_mon.currentTextChanged.connect(self.thay_doi_mon)

        lbl_chu_de = QLabel("1 Chủ đề:")
        lbl_chu_de.setStyleSheet("color: #FFFFFF; font-weight: bold;")
        self.cbo_chu_de = QComboBox()
        self.cbo_chu_de.setStyleSheet("color: #FFFFFF; font-weight: bold; font-size: 14px;")

        btn_start_cl = QPushButton("BẮT ĐẦU TRANH CÚP C1")
        btn_start_cl.setProperty("class", "btn-primary")
        btn_start_cl.setStyleSheet("color: #FFFFFF; font-weight: bold; font-size: 14px; padding: 8px 16px;")
        btn_start_cl.clicked.connect(self.bat_dau_giai_dau)

        row_sel.addWidget(lbl_clb)
        row_sel.addWidget(self.cbo_clb)
        row_sel.addWidget(lbl_lop)
        row_sel.addWidget(self.cbo_lop)
        row_sel.addWidget(lbl_mon)
        row_sel.addWidget(self.cbo_mon)
        row_sel.addWidget(lbl_chu_de)
        row_sel.addWidget(self.cbo_chu_de, 2)
        row_sel.addWidget(btn_start_cl)

        info_vbox.addLayout(row_sel)
        header_layout.addLayout(info_vbox, 2)

        # Ảnh 3D Cúp Tai Voi Champions League
        self.lbl_img_trophy = QLabel()
        self.lbl_img_trophy.setFixedSize(105, 105)
        self.lbl_img_trophy.setScaledContents(True)
        if os.path.exists(self.path_trophy_3d):
            self.lbl_img_trophy.setPixmap(QPixmap(self.path_trophy_3d))
        header_layout.addWidget(self.lbl_img_trophy)

        main_layout.addWidget(header_frame)

        # 3. Khung Bảng điểm Trận đấu Cúp C1
        match_status_frame = QFrame()
        match_status_frame.setProperty("class", "card-widget")
        match_layout = QHBoxLayout(match_status_frame)

        self.lbl_match_title = QLabel("TRẬN ĐẤU CÚP C1 CHAMPIONS LEAGUE")
        self.lbl_match_title.setStyleSheet("font-size: 16px; font-weight: bold; color: #FFFFFF;")

        self.lbl_score_board = QLabel("Tỷ số Penalty: 0 - 0 | Tổng Bàn Thắng Cúp C1: 0")
        self.lbl_score_board.setStyleSheet("font-size: 16px; font-weight: bold; color: #FFFFFF; background-color: #002B4D; padding: 6px 16px; border-radius: 12px; border: 2px solid #00A2FF;")

        self.lbl_timer_cl = QLabel("Thời gian trận đấu: 05:00")
        self.lbl_timer_cl.setStyleSheet("font-size: 16px; font-weight: bold; color: #FFFFFF; background-color: #002B4D; padding: 6px 16px; border-radius: 12px; border: 2px solid #00A2FF;")

        match_layout.addWidget(self.lbl_match_title)
        match_layout.addStretch()
        match_layout.addWidget(self.lbl_score_board)
        match_layout.addWidget(self.lbl_timer_cl)

        main_layout.addWidget(match_status_frame)

        # 4. Vùng thi đấu sút Penalty tri thức (QScrollArea)
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setStyleSheet("QScrollArea { border: none; background-color: transparent; }")

        self.stadium_frame = QFrame()
        self.stadium_frame.setProperty("class", "card-widget")
        stadium_layout = QVBoxLayout(self.stadium_frame)
        stadium_layout.setContentsMargins(15, 15, 15, 15)

        self.lbl_question_no = QLabel("Cú sút Penalty 1 / 5:")
        self.lbl_question_no.setStyleSheet("font-size: 16px; font-weight: bold; color: #FFFFFF;")
        stadium_layout.addWidget(self.lbl_question_no)

        self.lbl_question_text = QLabel("Chọn Lớp, Môn học, 1 Chủ đề và bấm 'BẮT ĐẦU TRANH CÚP C1' để tham gia thi đấu!")
        self.lbl_question_text.setStyleSheet("font-size: 17px; font-weight: bold; color: #FFFFFF; background-color: #111214; padding: 14px; border-radius: 10px; border: 2px solid #00A2FF;")
        self.lbl_question_text.setWordWrap(True)
        stadium_layout.addWidget(self.lbl_question_text)

        # Vùng chứa góc sút Penalty (Thẻ đáp án)
        self.vung_options_container = QWidget()
        self.vung_options_layout = QVBoxLayout(self.vung_options_container)
        stadium_layout.addWidget(self.vung_options_container)

        # Lời giải chi tiết
        self.lbl_giai_thich = QLabel("")
        self.lbl_giai_thich.setWordWrap(True)
        self.lbl_giai_thich.setStyleSheet("background-color: #002B4D; padding: 12px; border-radius: 8px; color: #FFFFFF; font-size: 15px; font-weight: bold; margin-top: 10px; border: 2px solid #0084FF;")
        self.lbl_giai_thich.hide()
        stadium_layout.addWidget(self.lbl_giai_thich)

        self.scroll_area.setWidget(self.stadium_frame)
        main_layout.addWidget(self.scroll_area)

        # 5. Thanh điều hướng sút bóng & Qua vòng đấu Champions League
        nav_layout = QHBoxLayout()
        self.btn_truoc = QPushButton("Lượt sút trước")
        self.btn_truoc.setProperty("class", "btn-secondary")
        self.btn_truoc.setStyleSheet("color: #FFFFFF; font-weight: bold;")
        self.btn_truoc.clicked.connect(self.luot_sut_truoc)

        self.btn_sau = QPushButton("Lượt sút tiếp theo")
        self.btn_sau.setProperty("class", "btn-secondary")
        self.btn_sau.setStyleSheet("color: #FFFFFF; font-weight: bold;")
        self.btn_sau.clicked.connect(self.luot_sut_sau)

        self.btn_giai_thich = QPushButton("Xem lời giải góc sút")
        self.btn_giai_thich.setProperty("class", "btn-secondary")
        self.btn_giai_thich.setStyleSheet("color: #FFFFFF; font-weight: bold;")
        self.btn_giai_thich.clicked.connect(self.hien_loi_giai)

        self.btn_submit_match = QPushButton("Nộp bài & Tổng kết trận Cúp C1")
        self.btn_submit_match.setProperty("class", "btn-success")
        self.btn_submit_match.setStyleSheet("color: #FFFFFF; font-weight: bold; font-size: 15px; padding: 10px 20px;")
        self.btn_submit_match.clicked.connect(self.tong_ket_tran_dau)

        nav_layout.addWidget(self.btn_truoc)
        nav_layout.addWidget(self.btn_sau)
        nav_layout.addWidget(self.btn_giai_thich)
        nav_layout.addStretch()
        nav_layout.addWidget(self.btn_submit_match)

        main_layout.addLayout(nav_layout)

        # Load Lớp và Môn học ban đầu
        self.thay_doi_lop(self.cbo_lop.currentText())

    def thay_doi_clb(self, index):
        if 0 <= index < len(self.danh_sach_clb):
            self.clb_user = self.danh_sach_clb[index]
            if hasattr(self, 'vong_info') and self.vong_info:
                clb_ten = self.clb_user["ten"]
                doi_thu = self.vong_info.get("doi_thu", "Đối thủ")
                ten_chu_de = self.cbo_chu_de.currentText() if self.cbo_chu_de.currentText() else "Chủ đề 1"
                self.lbl_match_title.setText(f"{self.vong_info['ten'].upper()}: {clb_ten.upper()} VS {doi_thu.upper()} (CHỦ ĐỀ: {ten_chu_de.upper()})")

    def thay_doi_lop(self, ten_lop):
        """Cập nhật danh sách môn học khi chọn Lớp."""
        self.cbo_mon.blockSignals(True)
        self.cbo_mon.clear()
        danh_sach_mon = lay_danh_sach_mon_hoc(ten_lop)
        self.cbo_mon.addItems(danh_sach_mon)
        self.cbo_mon.blockSignals(False)
        if danh_sach_mon:
            self.thay_doi_mon(danh_sach_mon[0])

    def thay_doi_mon(self, ten_mon):
        """Cập nhật 5 CHỦ ĐỀ tổng hợp khi chọn Môn học."""
        if not ten_mon:
            return
        ten_lop = self.cbo_lop.currentText()
        danh_sach_5_chu_de = lay_chu_de_theo_lop_va_mon(ten_lop, ten_mon)
        
        self.cbo_chu_de.blockSignals(True)
        self.cbo_chu_de.clear()
        self.cbo_chu_de.addItems(danh_sach_5_chu_de)
        self.cbo_chu_de.blockSignals(False)

    def bat_dau_giai_dau(self):
        """Khởi động trận đấu Champions League mới cho 1 Chủ đề được chọn (Kiểm tra giới hạn 3 lượt/ngày)."""
        hom_nay = QDate.currentDate().toString("yyyy-MM-dd")
        if self.last_played_date != hom_nay:
            self.last_played_date = hom_nay
            self.so_luot_hom_nay = 0

        if self.vong_idx == 0:
            if self.so_luot_hom_nay >= 3:
                QMessageBox.warning(
                    self, 
                    "Giới hạn lượt chơi Cúp C1", 
                    f"Mỗi ngày chỉ có tối đa 3 lượt tham gia Giải đấu Cúp C1 Champions League! Em đã sử dụng hết {self.so_luot_hom_nay}/3 lượt chơi hôm nay, hãy quay lại vào ngày mai nhé!"
                )
                return
            self.so_luot_hom_nay += 1

        ten_lop = self.cbo_lop.currentText()
        ten_mon = self.cbo_mon.currentText()
        ten_chu_de = self.cbo_chu_de.currentText() if self.cbo_chu_de.currentText() else "Chủ đề 1"

        tran_data = sinh_tran_dau_champions_league(self.vong_idx, ten_lop, ten_mon, ten_chu_de, self.clb_user["ten"])
        self.vong_info = tran_data["vong_info"]
        self.cau_hoi_cl = tran_data["cau_hoi"]

        self.cau_idx = 0
        self.dap_an_user = {}
        self.lbl_giai_thich.hide()

        clb_ten = self.clb_user["ten"]
        doi_thu = self.vong_info["doi_thu"]
        self.lbl_match_title.setText(f"{self.vong_info['ten'].upper()}: {clb_ten.upper()} VS {doi_thu.upper()} (CHỦ ĐỀ: {ten_chu_de.upper()})")
        self.lbl_score_board.setText(f"Tỷ số Penalty: 0 - 0 | Tổng Bàn Thắng Cúp C1: {self.so_ban_thang}")

        self.thoi_gian_con_lai = 300
        self.timer.start(1000)
        self.hien_thi_cau_hoi()

    def cap_nhat_dong_ho(self):
        if self.thoi_gian_con_lai > 0:
            self.thoi_gian_con_lai -= 1
            m = self.thoi_gian_con_lai // 60
            s = self.thoi_gian_con_lai % 60
            self.lbl_timer_cl.setText(f"Thời gian trận đấu: {m:02d}:{s:02d}")
        else:
            self.timer.stop()
            QMessageBox.warning(self, "Hết giờ thi đấu", "Hết thời gian trận đấu Cúp C1! Hệ thống tự động tổng kết tỷ số Penalty.")
            self.tong_ket_tran_dau()

    def hien_thi_cau_hoi(self):
        if not self.cau_hoi_cl:
            return

        cau_current = self.cau_hoi_cl[self.cau_idx]
        self.lbl_question_no.setText(f"Cú sút Penalty {self.cau_idx + 1} / {len(self.cau_hoi_cl)} (Chọn góc sút đúng kiến thức):")
        self.lbl_question_text.setText(cau_current["cau_hoi"])

        # Clear options
        for i in reversed(range(self.vung_options_layout.count())):
            widget = self.vung_options_layout.itemAt(i).widget()
            if widget:
                widget.setParent(None)

        dap_an_da_luu = self.dap_an_user.get(self.cau_idx, "")
        widget_options = TheDapAnGroup(cau_current["dap_an"], dap_an_hien_tai=dap_an_da_luu)
        widget_options.dap_an_thay_doi.connect(self.luu_dap_an)
        self.vung_options_layout.addWidget(widget_options)

    def luu_dap_an(self, text):
        self.dap_an_user[self.cau_idx] = text

    def luot_sut_truoc(self):
        if self.cau_idx > 0:
            self.cau_idx -= 1
            self.hien_thi_cau_hoi()

    def luot_sut_sau(self):
        if self.cau_idx < len(self.cau_hoi_cl) - 1:
            self.cau_idx += 1
            self.hien_thi_cau_hoi()

    def hien_loi_giai(self):
        if not self.cau_hoi_cl:
            return
        cau_current = self.cau_hoi_cl[self.cau_idx]
        self.lbl_giai_thich.setText(f"Góc sút đúng để ghi bàn: {cau_current.get('dap_an_dung')}\nPhân tích chiến thuật Cúp C1: {cau_current.get('giai_thich')}")
        if self.lbl_giai_thich.isHidden():
            self.lbl_giai_thich.show()
        else:
            self.lbl_giai_thich.hide()

    def tong_ket_tran_dau(self):
        self.timer.stop()
        if not self.cau_hoi_cl:
            return

        # Luu ngay choi hôm nay
        hom_nay = QDate.currentDate().toString("yyyy-MM-dd")
        self.last_played_date = hom_nay

        ban_thang_tran = 0
        for idx, cau in enumerate(self.cau_hoi_cl):
            ans = self.dap_an_user.get(idx, "")
            if str(ans).strip() == str(cau["dap_an_dung"]).strip():
                ban_thang_tran += 1

        clb_ten = self.clb_user["ten"]
        doi_thu = self.vong_info["doi_thu"]
        ten_chu_de = self.cbo_chu_de.currentText()
        ban_thang_doi_thu = random.randint(0, max(0, len(self.cau_hoi_cl) - 2))

        # Truong hop Hoa -> Penalty loai truc tiep!
        if ban_thang_tran == ban_thang_doi_thu:
            sut_user = random.randint(1, 5)
            sut_opp = random.randint(1, 5)
            while sut_user == sut_opp:
                sut_opp = random.randint(1, 5)
            if sut_user > sut_opp:
                ban_thang_tran += 1
                QMessageBox.information(self, "Penalty Loạt Sút Sinh Tử", f"HÒA TRẬN ĐẤU! Bước vào sút phạt Penalty loại trực tiếp: Câu lạc bộ {clb_ten} sút thắng {sut_user} - {sut_opp} {doi_thu}!")
            else:
                ban_thang_doi_thu += 1
                QMessageBox.warning(self, "Penalty Loạt Sút Sinh Tử", f"HÒA TRẬN ĐẤU! Bước vào sút phạt Penalty loại trực tiếp: Câu lạc bộ {clb_ten} sút thua {sut_user} - {sut_opp} {doi_thu}!")

        self.so_ban_thang += ban_thang_tran
        self.lbl_score_board.setText(f"Tỷ số Penalty: {clb_ten} {ban_thang_tran} - {ban_thang_doi_thu} {doi_thu} | Tổng Bàn Thắng Cúp C1: {self.so_ban_thang}")

        if ban_thang_tran > ban_thang_doi_thu:
            cong_phan_thuong(10.0, ban_thang_tran)
            if self.vong_idx < len(lay_vong_dau_champions_league()) - 1:
                QMessageBox.information(
                    self, 
                    "VICTORY", 
                    f"VICTORY!\n"
                    f"Xuất sắc! Câu lạc bộ {clb_ten} đã đánh bại {doi_thu} với tỷ số Penalty {ban_thang_tran} - {ban_thang_doi_thu}!\n"
                    f"Em đã giúp đội bóng tiến vào VÒNG TIẾP THEO CÚP C1 CHAMPIONS LEAGUE!\n"
                    f"Chủ đề chinh phục: {ten_chu_de}\nThưởng +{ban_thang_tran * 20} XP!"
                )
                self.vong_idx += 1
                self.bat_dau_giai_dau()
            else:
                # VO DICH CHUNG KET CUP C1!
                QMessageBox.information(
                    self, 
                    "CHAMMMMMMMMMMMMPION", 
                    f"CHAMMMMMMMMMMMMPION!\n"
                    f"CHÚC MỪNG NHÀ VÔ ĐỊCH CÚP C1 CHAMPIONS LEAGUE!\n"
                    f"Câu lạc bộ {clb_ten} đã xuất sắc nâng cao CÚP TAI VOI BẠC CHAMPIONS LEAGUE!\n"
                    f"Chủ đề đã làm chủ hoàn toàn: {ten_chu_de}\n"
                    f"Tổng bàn thắng Cúp C1: {self.so_ban_thang} Bàn Thắng!\nThưởng +500 XP và Cúp Tai Voi 3D!"
                )
                dlg_cert = HopThoaiChungNhan(
                    parent=self, 
                    lop=self.cbo_lop.currentText(), 
                    chu_de=f"NHÀ VÔ ĐỊCH CÚP C1 - {ten_chu_de}", 
                    phan_tram_diem=100, 
                    diem_so=10.0
                )
                dlg_cert.exec()
                self.vong_idx = 0
        else:
            QMessageBox.warning(
                self, 
                "DEFEAT", 
                f"DEFEAT!\n"
                f"Trận đấu kết thúc với tỷ số: {clb_ten} {ban_thang_tran} - {ban_thang_doi_thu} {doi_thu}.\n"
                f"Chủ đề {ten_chu_de} rất hấp dẫn, hãy tiếp tục rèn luyện và thử sức lại nhé!"
            )
