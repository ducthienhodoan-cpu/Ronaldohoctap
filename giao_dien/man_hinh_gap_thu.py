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

        # Khung danh sach thu bong va ti le
        frame_danh_sach = QFrame()
        frame_danh_sach.setStyleSheet(
            "background-color: #1E293B; border: 1px solid #334155; border-radius: 12px; padding: 12px;"
        )
        layout_ds = QVBoxLayout(frame_danh_sach)
        lbl_ds_tieu_de = QLabel("CƠ CẤU PHẦN THƯỞNG MÁY GẮP THÚ:")
        lbl_ds_tieu_de.setStyleSheet("font-size: 15px; font-weight: bold; color: #F59E0B;")
        layout_ds.addWidget(lbl_ds_tieu_de)

        lbl_mo_ta = QLabel("• Tỉ lệ gắp thành công 70% (khoảng 30% rớt). Trúng ngẫu nhiên 1 trong 3 loại thú:")
        lbl_mo_ta.setStyleSheet("font-size: 14px; font-weight: bold; color: #CBD5E1;")
        layout_ds.addWidget(lbl_mo_ta)

        layout_ds_chi_tiet = QHBoxLayout()
        ds_thu = lay_danh_sach_thu()
        for thu in ds_thu:
            lbl_item = QLabel(f"• {thu['ten']}: +{thu['xp']} XP")
            lbl_item.setStyleSheet("font-size: 14px; font-weight: bold; color: #38BDF8;")
            layout_ds_chi_tiet.addWidget(lbl_item)
        layout_ds.addLayout(layout_ds_chi_tiet)
        layout_chinh.addWidget(frame_danh_sach)

        # Khung mo phong may gap 3D / animation
        self.frame_may_gap = QFrame()
        self.frame_may_gap.setMinimumHeight(180)
        self.frame_may_gap.setStyleSheet(
            "background: linear-gradient(180deg, #1E1B4B 0%, #0F172A 100%); "
            "border: 3px solid #EC4899; border-radius: 16px; padding: 16px;"
        )
        layout_may_gap = QVBoxLayout(self.frame_may_gap)
        layout_may_gap.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.lbl_trang_thai_gap = QLabel("Nhấn nút GẮP THÚ để thử vận may!")
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
        self.lbl_ket_qua.setStyleSheet("font-size: 16px; font-weight: bold; color: #FFFFFF;")
        self.lbl_ket_qua.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout_may_gap.addWidget(self.lbl_ket_qua)

        layout_chinh.addWidget(self.frame_may_gap)

        # Nut bam GẮP THÚ duy nhat
        self.btn_gap_thu = QPushButton("GẮP THÚ")
        self.btn_gap_thu.setStyleSheet(
            "QPushButton { background: linear-gradient(135deg, #EC4899, #A855F7); color: #FFFFFF; font-size: 18px; font-weight: bold; padding: 16px; border-radius: 14px; border: none; }"
            "QPushButton:hover { background: linear-gradient(135deg, #F472B6, #C084FC); }"
            "QPushButton:disabled { background: #475569; color: #94A3B8; }"
        )
        self.btn_gap_thu.clicked.connect(self.bat_dau_gap)
        layout_chinh.addWidget(self.btn_gap_thu)

    def bat_dau_gap(self):
        """Bat dau qua trinh tay gap ha xuong."""
        if self.dang_gap:
            return

        self.dang_gap = True
        self.btn_gap_thu.setEnabled(False)
        self.tien_trinh_gap = 0
        self.progress_bar_gap.setValue(0)
        self.lbl_ket_qua.setText("")

        self.lbl_trang_thai_gap.setText("Tay gắp đang hạ xuống gắp thú bông...")
        self.lbl_trang_thai_gap.setStyleSheet("font-size: 18px; font-weight: bold; color: #F59E0B;")

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
        thanh_cong, xp, thong_bao, thu_info = thuc_hien_gap_thu()

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
            self.lbl_trang_thai_gap.setText("TAY GẮP BỊ RỚT!")
            self.lbl_trang_thai_gap.setStyleSheet("font-size: 18px; font-weight: bold; color: #EF4444;")
            self.lbl_ket_qua.setText(thong_bao)
            self.lbl_ket_qua.setStyleSheet("font-size: 17px; font-weight: bold; color: #EF4444;")

        # Cap nhat thong ke
        self.lbl_luot_choi.setText(f"Tổng lượt gắp: {self.tong_luot_choi}")
        self.lbl_tong_xp.setText(f"Tổng XP gắp được: {self.tong_xp_gap_duoc} XP")

        self.dang_gap = False
        self.btn_gap_thu.setEnabled(True)


