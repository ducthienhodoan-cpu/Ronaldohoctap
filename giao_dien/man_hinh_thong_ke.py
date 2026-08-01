# Thu muc: giao_dien
# File: man_hinh_thong_ke.py
# Mo ta: Man hinh thong ke ket qua hoc tap va ve bieu do tien do qua Matplotlib sang Tieng Viet co dau

from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, 
    QPushButton, QFrame
)
from thong_ke.bieu_do_hoc_tap import BieuDoHocTapCanvas

class ManHinhThongKe(QWidget):
    """Màn hình biểu đồ thống kê tiến độ và so sánh kết quả học tập chuẩn Tiếng Việt có dấu."""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(15)

        # Tiêu đề
        title_label = QLabel("THỐNG KÊ KẾT QUẢ HỌC TẬP VÀ TIẾN ĐỘ")
        title_label.setStyleSheet("font-size: 22px; font-weight: bold; color: #2C3E50;")
        main_layout.addWidget(title_label)

        # Thanh chuyển đổi biểu đồ (Ngày / Tuần / Tháng / Môn học)
        filter_layout = QHBoxLayout()
        
        btn_ngay = QPushButton("Điểm theo ngày")
        btn_ngay.setProperty("class", "btn-secondary")
        btn_ngay.clicked.connect(self.xem_diem_ngay)

        btn_tuan = QPushButton("Điểm theo tuần")
        btn_tuan.setProperty("class", "btn-secondary")
        btn_tuan.clicked.connect(self.xem_diem_tuan)

        btn_mon = QPushButton("So sánh theo môn học")
        btn_mon.setProperty("class", "btn-primary")
        btn_mon.clicked.connect(self.xem_diem_mon)

        filter_layout.addWidget(btn_ngay)
        filter_layout.addWidget(btn_tuan)
        filter_layout.addWidget(btn_mon)
        filter_layout.addStretch()

        main_layout.addLayout(filter_layout)

        # Card chứa biểu đồ Matplotlib
        chart_frame = QFrame()
        chart_frame.setProperty("class", "card-widget")
        chart_layout = QVBoxLayout(chart_frame)

        self.canvas_bieu_do = BieuDoHocTapCanvas(self, width=6, height=4)
        chart_layout.addWidget(self.canvas_bieu_do)

        main_layout.addWidget(chart_frame)

    def xem_diem_ngay(self):
        self.canvas_bieu_do.ve_bieu_do_mac_dinh()

    def xem_diem_tuan(self):
        self.canvas_bieu_do.ve_bieu_do_mac_dinh()

    def xem_diem_mon(self):
        mon_list = ["Toán", "Tiếng Việt", "Tiếng Anh", "Tin học", "Khoa học"]
        diem_list = [9.2, 8.8, 9.5, 9.8, 8.5]
        self.canvas_bieu_do.ve_bieu_do_mon_hoc(mon_list, diem_list)
