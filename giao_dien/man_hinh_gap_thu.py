# Thu muc: giao_dien
# File: man_hinh_gap_thu.py
# Mo ta: Man hinh tro choi Gap Thu tich luy XP cho ung dung PyQt6 giao dien ruc ro khong dung icon/emoji

from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel,
    QPushButton, QFrame, QProgressBar, QMessageBox
)
from PyQt6.QtCore import QTimer, Qt
from PyQt6.QtGui import QFont

from xu_ly_tro_choi.quan_ly_gap_thu import thuc_hien_gap_thu, lay_danh_sach_thu
from xu_ly_hoc_tap.he_thong_thuong import cong_phan_thuong

class ManHinhGapThu(QWidget):
    """Màn hình Trò chơi Gắp Thú May Mắn tích lũy XP trong PyQt6."""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.tong_luot_choi = 0
        self.tong_xp_gap_duoc = 0
        self.dang_gap = False
        self.loai_thu_dang_gap = "thuong"
        
        # Timer mo phong hoat anh tay gap
        self.timer_gap = QTimer(self)
        self.timer_gap.timeout.connect(self.xu_ly_tien_trinh_gap)
        self.tien_trinh_gap = 0

        self.init_ui()

    def init_ui(self):
        layout_chinh = QVBoxLayout(self)
        layout_chinh.setContentsMargins(20, 20, 20, 20)
        layout_chinh.setSpacing(16)

        # Thanh tieu de
        tieu_de = QLabel("TRÒ CHƠI GẮP THÚ MAY MẮN - TÍCH LŨY XP")
        tieu_de.setStyleSheet("font-size: 22px; font-weight: bold; color: #06B6D4; background: transparent;")
        tieu_de.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout_chinh.addWidget(tieu_de)

        # Khung thong ke luot va XP
        frame_stats = QFrame()
        frame_stats.setStyleSheet(
            "background-color: rgba(15, 23, 42, 0.85); "
            "border: 2px solid #06B6D4; border-radius: 12px; padding: 10px;"
        )
        layout_stats = QHBoxLayout(frame_stats)
        
        self.lbl_luot_choi = QLabel("Tổng lượt gắp: 0")
        self.lbl_luot_choi.setStyleSheet("font-size: 16px; font-weight: bold; color: #FFFFFF;")
        
        self.lbl_tong_xp = QLabel("Tổng XP gắp được: 0 XP")
        self.lbl_tong_xp.setStyleSheet("font-size: 16px; font-weight: bold; color: #10B981;")

        layout_stats.addWidget(self.lbl_luot_choi)
        layout_stats.addStretch()
        layout_stats.addWidget(self.lbl_tong_xp)
        layout_chinh.addWidget(frame_stats)

        # Khung mo phong may gap 3D / animation
        self.frame_may_gap = QFrame()
        self.frame_may_gap.setMinimumHeight(200)
        self.frame_may_gap.setStyleSheet(
            "background: linear-gradient(180deg, #1E1B4B 0%, #0F172A 100%); "
            "border: 3px solid #EC4899; border-radius: 16px; padding: 16px;"
        )
        layout_may_gap = QVBoxLayout(self.frame_may_gap)
        layout_may_gap.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.lbl_trang_thai_gap = QLabel("Vui lòng chọn loại thú bông để bắt đầu gắp!")
        self.lbl_trang_thai_gap.setStyleSheet("font-size: 18px; font-weight: bold; color: #F59E0B;")
        self.lbl_trang_thai_gap.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout_may_gap.addWidget(self.lbl_trang_thai_gap)

        # Thanh tien trinh tay gap ha xuong va keo len
        self.progress_bar_gap = QProgressBar()
        self.progress_bar_gap.setRange(0, 100)
        self.progress_bar_gap.setValue(0)
        self.progress_bar_gap.setTextVisible(False)
        self.progress_bar_gap.setStyleSheet(
            "QProgressBar { border: 2px solid #A855F7; border-radius: 8px; background-color: #020617; height: 20px; }"
            "QProgressBar::chunk { background: linear-gradient(90deg, #06B6D4, #EC4899); border-radius: 6px; }"
        )
        layout_may_gap.addWidget(self.progress_bar_gap)

        self.lbl_ket_qua = QLabel("")
        self.lbl_ket_qua.setStyleSheet("font-size: 17px; font-weight: bold; color: #FFFFFF;")
        self.lbl_ket_qua.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout_may_gap.addWidget(self.lbl_ket_qua)

        layout_chinh.addWidget(self.frame_may_gap)

        # Khung 3 nut bam lua chon 3 cap do gap thu
        lbl_huong_dan = QLabel("CHỌN CẤP ĐỘ GẮP THÚ:")
        lbl_huong_dan.setStyleSheet("font-size: 16px; font-weight: bold; color: #FFFFFF;")
        layout_chinh.addWidget(lbl_huong_dan)

        layout_nut = QHBoxLayout()
        layout_nut.setSpacing(12)

        # Nut Gắp Thường (75% - 50XP)
        self.btn_thuong = QPushButton("Gắp Gấu Bông Thường\nTỉ lệ: 75% | Thưởng: 50 XP")
        self.btn_thuong.setStyleSheet(
            "QPushButton { background: linear-gradient(135deg, #06B6D4, #0891B2); color: #FFFFFF; font-size: 14px; font-weight: bold; padding: 14px; border-radius: 12px; border: none; }"
            "QPushButton:hover { background: linear-gradient(135deg, #22D3EE, #06B6D4); }"
            "QPushButton:disabled { background: #475569; color: #94A3B8; }"
        )
        self.btn_thuong.clicked.connect(lambda: self.bat_dau_gap("thuong"))

        # Nut Gắp Hiếm (50% - 200XP)
        self.btn_hiem = QPushButton("Gắp Thỏ Bông Hiếm\nTỉ lệ: 50% | Thưởng: 200 XP")
        self.btn_hiem.setStyleSheet(
            "QPushButton { background: linear-gradient(135deg, #F59E0B, #D97706); color: #FFFFFF; font-size: 14px; font-weight: bold; padding: 14px; border-radius: 12px; border: none; }"
            "QPushButton:hover { background: linear-gradient(135deg, #FBBF24, #F59E0B); }"
            "QPushButton:disabled { background: #475569; color: #94A3B8; }"
        )
        self.btn_hiem.clicked.connect(lambda: self.bat_dau_gap("hiem"))

        # Nut Gắp Huyền Thoại (25% - 500XP)
        self.btn_huyen_thoai = QPushButton("Gắp Rồng Bông Huyền Thoại\nTỉ lệ: 25% | Thưởng: 500 XP")
        self.btn_huyen_thoai.setStyleSheet(
            "QPushButton { background: linear-gradient(135deg, #EC4899, #BE185D); color: #FFFFFF; font-size: 14px; font-weight: bold; padding: 14px; border-radius: 12px; border: none; }"
            "QPushButton:hover { background: linear-gradient(135deg, #F472B6, #EC4899); }"
            "QPushButton:disabled { background: #475569; color: #94A3B8; }"
        )
        self.btn_huyen_thoai.clicked.connect(lambda: self.bat_dau_gap("huyen_thoai"))

        layout_nut.addWidget(self.btn_thuong)
        layout_nut.addWidget(self.btn_hiem)
        layout_nut.addWidget(self.btn_huyen_thoai)

        layout_chinh.addLayout(layout_nut)

    def bat_dau_gap(self, loai_id):
        """Bat dau qua trinh gap thu bong hoat anh."""
        if self.dang_gap:
            return

        self.dang_gap = True
        self.loai_thu_dang_gap = loai_id
        self.set_nut_enabled(False)
        self.tien_trinh_gap = 0
        self.progress_bar_gap.setValue(0)
        self.lbl_ket_qua.setText("")

        if loai_id == "thuong":
            self.lbl_trang_thai_gap.setText("Tay gắp đang hạ xuống gắp Gấu Bông Thường (75%)...")
        elif loai_id == "hiem":
            self.lbl_trang_thai_gap.setText("Tay gắp đang hạ xuống gắp Thỏ Bông Hiếm (50%)...")
        else:
            self.lbl_trang_thai_gap.setText("Tay gắp đang hạ xuống gắp Rồng Bông Huyền Thoại (25%)...")

        # Chay timer hoat anh 40ms 1 lan (tong cong ~2 giay)
        self.timer_gap.start(40)

    def xu_ly_tien_trinh_gap(self):
        """Cap nhat thanh tien trinh hoat anh tay gap."""
        self.tien_trinh_gap += 5
        self.progress_bar_gap.setValue(self.tien_trinh_gap)

        if self.tien_trinh_gap >= 100:
            self.timer_gap.stop()
            self.hoan_thanh_gap()

    def hoan_thanh_gap(self):
        """Tinh ket qua gap va cong XP khi hoan thanh hoat anh."""
        self.tong_luot_choi += 1
        thanh_cong, xp, thong_bao = thuc_hien_gap_thu(self.loai_thu_dang_gap)

        if thanh_cong:
            self.tong_xp_gap_duoc += xp
            self.lbl_trang_thai_gap.setText("GẮP THÀNH CÔNG!")
            self.lbl_trang_thai_gap.setStyleSheet("font-size: 18px; font-weight: bold; color: #10B981;")
            self.lbl_ket_qua.setText(thong_bao)
            self.lbl_ket_qua.setStyleSheet("font-size: 17px; font-weight: bold; color: #10B981;")
            
            # Cong XP vao he thong thuong hoc tap
            try:
                cong_phan_thuong(xp, f"Thắng trò chơi Gắp Thú ({xp} XP)")
            except Exception:
                pass
        else:
            self.lbl_trang_thai_gap.setText("GẮP TRƯỢT MẤT RỒI!")
            self.lbl_trang_thai_gap.setStyleSheet("font-size: 18px; font-weight: bold; color: #EF4444;")
            self.lbl_ket_qua.setText(thong_bao)
            self.lbl_ket_qua.setStyleSheet("font-size: 17px; font-weight: bold; color: #EF4444;")

        # Cap nhat thong ke
        self.lbl_luot_choi.setText(f"Tổng lượt gắp: {self.tong_luot_choi}")
        self.lbl_tong_xp.setText(f"Tổng XP gắp được: {self.tong_xp_gap_duoc} XP")

        self.dang_gap = False
        self.set_nut_enabled(True)

    def set_nut_enabled(self, state):
        """Bat hoac tat cac nut bam trong khi dang gap."""
        self.btn_thuong.setEnabled(state)
        self.btn_hiem.setEnabled(state)
        self.btn_huyen_thoai.setEnabled(state)
