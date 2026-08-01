# Thu muc: giao_dien
# File: man_hinh_cai_dat.py
# Mo ta: Man hinh cai dat tai khoan phong cach Roblox Avatar Customization Tat ca chu mau trang sang ro net

import os
from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, 
    QLineEdit, QPushButton, QFrame, QMessageBox, QSlider, QComboBox
)
from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtGui import QPixmap

from giao_dien.phoi_mau_qss import lay_qss_giao_dien
from xu_ly_hoc_tap.quan_ly_nguoi_dung import lay_ten_nguoi_dung, cap_nhat_ten_nguoi_dung, lay_thong_tin_nguoi_dung
from xu_ly_hoc_tap.he_thong_thuong import lay_thong_tin_thuong
from xu_ly_hoc_tap.quan_ly_tien_do import lay_du_lieu_tien_do
from xu_ly_am_thanh.quan_ly_am_thanh import QuanLyAmThanh
from xu_ly_cai_dat.quan_ly_diem_mong_muon import lay_cai_dat_diem_mong_muon, luu_cai_dat_diem_mong_muon


class ManHinhCaiDat(QWidget):
    """Màn hình Cài đặt tài khoản phong cách Roblox Avatar Customization với TẤT CẢ CHỮ LÀ CHỮ TRẮNG SÁNG."""

    # Tín hiệu thông báo khi tên thay đổi để cập nhật Header bar
    ten_da_thay_doi = pyqtSignal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.roblox_avatar_3d_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "hinh_anh_3d", "roblox_anh_dai_dien_3d.png"))
        self.init_ui()

    def init_ui(self):
        layout_chinh = QVBoxLayout(self)
        layout_chinh.setContentsMargins(20, 20, 20, 20)
        layout_chinh.setSpacing(20)

        # 1. Card thông tin hồ sơ Roblox Avatar
        card_ho_so = QFrame()
        card_ho_so.setProperty("class", "card-widget")
        layout_ho_so_tong = QHBoxLayout(card_ho_so)
        layout_ho_so_tong.setContentsMargins(20, 20, 20, 20)
        layout_ho_so_tong.setSpacing(20)

        # Hiển thị Roblox Avatar 3D
        if os.path.exists(self.roblox_avatar_3d_path):
            pixmap_avatar = QPixmap(self.roblox_avatar_3d_path).scaled(120, 120, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
            lbl_avatar = QLabel()
            lbl_avatar.setPixmap(pixmap_avatar)
            lbl_avatar.setAlignment(Qt.AlignmentFlag.AlignCenter)
            layout_ho_so_tong.addWidget(lbl_avatar)

        # Khung văn bản thông số Roblox Avatar chữ trắng
        layout_ho_so = QVBoxLayout()
        layout_ho_so.setSpacing(8)

        lbl_tieu_de_ho_so = QLabel("HỒ SƠ NHÂN VẬT ROBLOX AVATAR")
        lbl_tieu_de_ho_so.setStyleSheet("font-size: 18px; font-weight: bold; color: #FFFFFF;")
        layout_ho_so.addWidget(lbl_tieu_de_ho_so)

        self.lbl_ten_hien_tai = QLabel()
        self.lbl_ten_hien_tai.setStyleSheet("font-size: 16px; font-weight: bold; color: #FFFFFF;")
        
        self.lbl_cap_do = QLabel()
        self.lbl_cap_do.setStyleSheet("font-size: 15px; color: #FFFFFF; font-weight: bold;")
        
        self.lbl_streak = QLabel()
        self.lbl_streak.setStyleSheet("font-size: 15px; color: #FFFFFF; font-weight: bold;")

        layout_ho_so.addWidget(self.lbl_ten_hien_tai)
        layout_ho_so.addWidget(self.lbl_cap_do)
        layout_ho_so.addWidget(self.lbl_streak)

        layout_ho_so_tong.addLayout(layout_ho_so, 1)

        layout_chinh.addWidget(card_ho_so)

        # 2. Card đổi tên Roblox Avatar
        card_doi_ten = QFrame()
        card_doi_ten.setProperty("class", "card-widget")
        layout_doi_ten = QVBoxLayout(card_doi_ten)
        layout_doi_ten.setContentsMargins(20, 20, 20, 20)
        layout_doi_ten.setSpacing(14)

        lbl_tieu_de_doi_ten = QLabel("CÀI ĐẶT & THAY ĐỔI TÊN ROBLOX AVATAR")
        lbl_tieu_de_doi_ten.setStyleSheet("font-size: 18px; font-weight: bold; color: #FFFFFF;")
        layout_doi_ten.addWidget(lbl_tieu_de_doi_ten)

        lbl_huong_dan = QLabel("Nhập họ tên mới của em để đồng bộ dữ liệu nhân vật Roblox:")
        lbl_huong_dan.setStyleSheet("font-size: 15px; color: #FFFFFF;")
        layout_doi_ten.addWidget(lbl_huong_dan)

        # Form nhập tên mới chữ trắng
        form_layout = QHBoxLayout()
        self.txt_ten_moi = QLineEdit()
        self.txt_ten_moi.setPlaceholderText("Nhập họ tên mới...")
        self.txt_ten_moi.setStyleSheet("font-size: 15px; padding: 10px; color: #FFFFFF; font-weight: bold;")
        self.txt_ten_moi.returnPressed.connect(self.luu_ten_moi)

        btn_luu = QPushButton("Lưu thay đổi Roblox Avatar")
        btn_luu.setProperty("class", "btn-primary")
        btn_luu.setStyleSheet("color: #FFFFFF; font-weight: bold;")
        btn_luu.setCursor(Qt.CursorShape.PointingHandCursor)
        btn_luu.clicked.connect(self.luu_ten_moi)

        form_layout.addWidget(self.txt_ten_moi, 3)
        form_layout.addWidget(btn_luu, 1)

        layout_doi_ten.addLayout(form_layout)

        # Nhãn thông báo kết quả chữ trắng
        self.lbl_thong_bao = QLabel("")
        self.lbl_thong_bao.setStyleSheet("font-weight: bold; font-size: 14px; color: #FFFFFF;")
        layout_doi_ten.addWidget(self.lbl_thong_bao)

        layout_chinh.addWidget(card_doi_ten)

        # 3. Card Điều chỉnh âm lượng nhạc nền & hiệu ứng
        card_am_luong = QFrame()
        card_am_luong.setProperty("class", "card-widget")
        layout_am_luong = QVBoxLayout(card_am_luong)
        layout_am_luong.setContentsMargins(20, 20, 20, 20)
        layout_am_luong.setSpacing(14)

        lbl_tieu_de_am_luong = QLabel("ĐIỀU CHỈNH ÂM LƯỢNG NHẠC NỀN & HIỆU ỨNG")
        lbl_tieu_de_am_luong.setStyleSheet("font-size: 18px; font-weight: bold; color: #FFFFFF;")
        layout_am_luong.addWidget(lbl_tieu_de_am_luong)

        layout_ctrl = QHBoxLayout()
        self.btn_toggle_am_luong = QPushButton("Bật / Tắt Nhạc Nền")
        self.btn_toggle_am_luong.setProperty("class", "btn-primary")
        self.btn_toggle_am_luong.setStyleSheet("color: #FFFFFF; font-weight: bold; background-color: #00A2FF;")
        self.btn_toggle_am_luong.setCursor(Qt.CursorShape.PointingHandCursor)
        self.btn_toggle_am_luong.clicked.connect(self.bat_tat_nhac_nen)

        lbl_vol_title = QLabel("Âm lượng:")
        lbl_vol_title.setStyleSheet("font-size: 15px; color: #FFFFFF; font-weight: bold;")

        self.slider_am_luong = QSlider(Qt.Orientation.Horizontal)
        self.slider_am_luong.setRange(0, 100)
        self.slider_am_luong.setValue(QuanLyAmThanh.get_instance().lay_am_luong_nhac_nen())
        self.slider_am_luong.setStyleSheet("height: 25px;")
        self.slider_am_luong.valueChanged.connect(self.thay_doi_am_luong)

        self.lbl_phan_tram_vol = QLabel(f"{QuanLyAmThanh.get_instance().lay_am_luong_nhac_nen()}%")
        self.lbl_phan_tram_vol.setStyleSheet("font-size: 16px; color: #FFFFFF; font-weight: bold; min-width: 45px;")

        layout_ctrl.addWidget(self.btn_toggle_am_luong)
        layout_ctrl.addSpacing(15)
        layout_ctrl.addWidget(lbl_vol_title)
        layout_ctrl.addWidget(self.slider_am_luong, 1)
        layout_ctrl.addWidget(self.lbl_phan_tram_vol)

        layout_am_luong.addLayout(layout_ctrl)
        layout_chinh.addWidget(card_am_luong)

        # 4. Card Cấu hình điểm mong muốn & Target Band IELTS
        card_target = QFrame()
        card_target.setProperty("class", "card-widget")
        layout_target = QVBoxLayout(card_target)
        layout_target.setContentsMargins(20, 20, 20, 20)
        layout_target.setSpacing(14)

        lbl_tieu_de_target = QLabel("CÀI ĐẶT ĐIỂM SỐ & BAND IELTS MONG MUỐN")
        lbl_tieu_de_target.setStyleSheet("font-size: 18px; font-weight: bold; color: #FFFFFF;")
        layout_target.addWidget(lbl_tieu_de_target)

        # Hàng chọn điểm môn học mong muốn
        row_diem = QHBoxLayout()
        lbl_diem = QLabel("Điểm thi môn học mong muốn (Target Grade):")
        lbl_diem.setStyleSheet("font-size: 15px; color: #FFFFFF; font-weight: bold;")
        self.cbo_diem_target = QComboBox()
        self.cbo_diem_target.setStyleSheet("color: #FFFFFF; font-weight: bold; font-size: 14px;")
        self.cbo_diem_target.addItems([
            "9.0 - 10.0 điểm (Xuất sắc)",
            "8.0 - 8.9 điểm (Giỏi)",
            "7.0 - 7.9 điểm (Khá)",
            "6.0 - 6.9 điểm (Trung bình khá)"
        ])
        row_diem.addWidget(lbl_diem)
        row_diem.addWidget(self.cbo_diem_target, 1)
        layout_target.addLayout(row_diem)

        # Hàng chọn Target Band IELTS
        row_band = QHBoxLayout()
        lbl_band_t = QLabel("Band IELTS mong muốn (Target Band):")
        lbl_band_t.setStyleSheet("font-size: 15px; color: #FFFFFF; font-weight: bold;")
        self.cbo_band_target = QComboBox()
        self.cbo_band_target.setStyleSheet("color: #FFFFFF; font-weight: bold; font-size: 14px;")
        self.cbo_band_target.addItems([
            "Band 7.5 - 8.5+ (Xuất sắc)",
            "Band 6.5 - 7.0 (Nâng cao)",
            "Band 5.5 - 6.0 (Trung cấp)",
            "Band 4.5 - 5.0 (Cơ bản)"
        ])
        row_band.addWidget(lbl_band_t)
        row_band.addWidget(self.cbo_band_target, 1)
        layout_target.addLayout(row_band)

        # Hàng chọn thời gian học mỗi ngày
        row_time = QHBoxLayout()
        lbl_time_t = QLabel("Mục tiêu thời gian luyện tập mỗi ngày:")
        lbl_time_t.setStyleSheet("font-size: 15px; color: #FFFFFF; font-weight: bold;")
        self.cbo_thoi_gian_target = QComboBox()
        self.cbo_thoi_gian_target.setStyleSheet("color: #FFFFFF; font-weight: bold; font-size: 14px;")
        self.cbo_thoi_gian_target.addItems([
            "30 Phút / Ngày",
            "45 Phút / Ngày",
            "60 Phút / Ngày",
            "90 Phút / Ngày"
        ])
        row_time.addWidget(lbl_time_t)
        row_time.addWidget(self.cbo_thoi_gian_target, 1)
        layout_target.addLayout(row_time)

        # Nút Lưu Cài Đặt Điểm Mong Muốn
        btn_luu_target = QPushButton("Lưu Cấu Hình Điểm Mong Muốn")
        btn_luu_target.setProperty("class", "btn-primary")
        btn_luu_target.setStyleSheet("color: #FFFFFF; font-weight: bold; font-size: 14px; padding: 10px;")
        btn_luu_target.setCursor(Qt.CursorShape.PointingHandCursor)
        btn_luu_target.clicked.connect(self.luu_cai_dat_diem_target)
        layout_target.addWidget(btn_luu_target)

        layout_chinh.addWidget(card_target)

        layout_chinh.addStretch()


        # Nạp dữ liệu ban đầu
        self.tai_lai_thong_tin()

    def tai_lai_thong_tin(self):
        """Tải lại và hiển thị thông tin học sinh mới nhất."""
        ten = lay_ten_nguoi_dung()
        thuong = lay_thong_tin_thuong()
        tien_do = lay_du_lieu_tien_do()
        cai_dat_target = lay_cai_dat_diem_mong_muon()

        self.lbl_ten_hien_tai.setText(f"Tên Avatar: {ten}")
        self.lbl_cap_do.setText(
            f"Roblox Level: Level {thuong.get('level', 1)} | Danh hiệu: {thuong.get('danh_hieu', 'Học sinh Tích cực')} | XP: {thuong.get('xp', 0)}"
        )
        self.lbl_streak.setText(f"Chuỗi ngày học (Streak): {tien_do.get('streak', 1)} ngày liên tiếp")
        self.txt_ten_moi.setText(ten)

        # Cập nhật các ô chọn Cài đặt điểm mong muốn
        if cai_dat_target.get("diem_mong_muon"):
            self.cbo_diem_target.setCurrentText(cai_dat_target["diem_mong_muon"])
        if cai_dat_target.get("band_ielts_mong_muon"):
            self.cbo_band_target.setCurrentText(cai_dat_target["band_ielts_mong_muon"])
        if cai_dat_target.get("thoi_gian_hoc_ngay"):
            self.cbo_thoi_gian_target.setCurrentText(cai_dat_target["thoi_gian_hoc_ngay"])

        # Cập nhật slider âm lượng
        val = QuanLyAmThanh.get_instance().lay_am_luong_nhac_nen()
        self.slider_am_luong.setValue(val)
        self.lbl_phan_tram_vol.setText(f"{val}%")

    def luu_cai_dat_diem_target(self):
        """Lưu các thông số Cài đặt điểm mong muốn của học sinh."""
        data_target = {
            "diem_mong_muon": self.cbo_diem_target.currentText(),
            "band_ielts_mong_muon": self.cbo_band_target.currentText(),
            "thoi_gian_hoc_ngay": self.cbo_thoi_gian_target.currentText()
        }
        if luu_cai_dat_diem_mong_muon(data_target):
            QMessageBox.information(self, "Cài đặt thành công", f"Đã lưu thành công cấu hình Mục tiêu học tập:\n- Điểm mong muốn: {data_target['diem_mong_muon']}\n- Band IELTS Target: {data_target['band_ielts_mong_muon']}\n- Thời gian học mỗi ngày: {data_target['thoi_gian_hoc_ngay']}")
        else:
            QMessageBox.warning(self, "Lỗi", "Không thể lưu cài đặt điểm mong muốn. Vui lòng thử lại!")


    def bat_tat_nhac_nen(self):
        """Bật hoặc tắt nhạc nền hệ thống."""
        QuanLyAmThanh.get_instance().bat_tat_nhac_nen()
        self.tai_lai_thong_tin()

    def thay_doi_am_luong(self, val):
        """Cập nhật giá trị âm lượng khi kéo thanh trượt Slider."""
        QuanLyAmThanh.get_instance().dat_am_luong_nhac_nen(val)
        self.lbl_phan_tram_vol.setText(f"{val}%")

    def luu_ten_moi(self):
        """Xử lý sự kiện lưu tên mới."""
        ten_moi = self.txt_ten_moi.text().strip()
        if not ten_moi:
            self.lbl_thong_bao.setStyleSheet("color: #FFFFFF; font-weight: bold;")
            self.lbl_thong_bao.setText("Tên không được để trống!")
            return

        if cap_nhat_ten_nguoi_dung(ten_moi):
            self.lbl_thong_bao.setStyleSheet("color: #FFFFFF; font-weight: bold;")
            self.lbl_thong_bao.setText(f"Đã cập nhật tên Roblox Avatar thành công: {ten_moi}")
            self.tai_lai_thong_tin()
            # Phát tín hiệu để CuaSoChinh cập nhật Header
            self.ten_da_thay_doi.emit(ten_moi)
        else:
            self.lbl_thong_bao.setStyleSheet("color: #FFFFFF; font-weight: bold;")
            self.lbl_thong_bao.setText("Lỗi khi lưu tên mới. Vui lòng thử lại!")
