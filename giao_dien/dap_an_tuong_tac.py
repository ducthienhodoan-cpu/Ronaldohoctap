# Thu muc: giao_dien
# File: dap_an_tuong_tac.py
# Mo ta: Thanh phan giao dien the dap an tuong tac voi tat ca chu deu mau trang tinh sang ro net

from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, 
    QPushButton, QFrame, QComboBox
)
from PyQt6.QtCore import pyqtSignal, Qt
from xu_ly_am_thanh.quan_ly_am_thanh import QuanLyAmThanh

class TheDapAnButton(QPushButton):
    """Nút bấm dạng thẻ chọn đáp án với chữ màu trắng sáng rõ nét và hỗ trợ đáp án dài không bị che chữ."""

    def __init__(self, key_label, content_text, parent=None):
        super().__init__(parent)
        self.key_label = key_label
        self.content_text = content_text
        self.setText(f"{key_label}. {content_text}")
        self.setCheckable(True)
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        self.setProperty("class", "card-option")
        self.setStyleSheet("color: #FFFFFF; font-weight: bold; font-size: 15px; text-align: left; padding: 10px 14px; background-color: #1E2022; border: 2px solid #393B3D; border-radius: 8px; min-height: 45px;")

    def dat_trang_thai_chon(self, checked):
        self.setChecked(checked)
        if checked:
            self.setProperty("class", "card-option-selected")
            self.setStyleSheet("color: #FFFFFF; font-weight: bold; font-size: 15px; text-align: left; padding: 10px 14px; background-color: #002B4D; border: 2px solid #00A2FF; border-radius: 8px; min-height: 45px;")
        else:
            self.setProperty("class", "card-option")
            self.setStyleSheet("color: #FFFFFF; font-weight: bold; font-size: 15px; text-align: left; padding: 10px 14px; background-color: #1E2022; border: 2px solid #393B3D; border-radius: 8px; min-height: 45px;")
        self.style().unpolish(self)
        self.style().polish(self)



class TheDapAnGroup(QWidget):
    """Nhóm quản lý danh sách các thẻ đáp án trắc nghiệm và đúng sai chữ trắng."""
    
    dap_an_thay_doi = pyqtSignal(str)

    def __init__(self, danh_sach_dap_an, dap_an_hien_tai="", parent=None):
        super().__init__(parent)
        self.danh_sach_dap_an = danh_sach_dap_an
        self.dap_an_da_chon = str(dap_an_hien_tai)
        self.danh_sach_nut = []
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 5, 0, 5)
        layout.setSpacing(10)

        nhan_chu = ["A", "B", "C", "D", "E", "F"]

        for idx, option_text in enumerate(self.danh_sach_dap_an):
            label_prefix = nhan_chu[idx] if idx < len(nhan_chu) else str(idx + 1)
            btn = TheDapAnButton(label_prefix, option_text)
            
            if str(option_text) == self.dap_an_da_chon:
                btn.dat_trang_thai_chon(True)

            btn.clicked.connect(lambda checked, text=option_text, button=btn: self.chon_dap_an(text, button))
            layout.addWidget(btn)
            self.danh_sach_nut.append((btn, option_text))

    def chon_dap_an(self, selected_text, target_button):
        self.dap_an_da_chon = selected_text
        for btn, opt_text in self.danh_sach_nut:
            btn.dat_trang_thai_chon(btn == target_button)
        QuanLyAmThanh.get_instance().phat_hieu_ung_dap_an()
        self.dap_an_thay_doi.emit(selected_text)


class KhungGhepCap(QWidget):
    """Giao diện tương tác ghép cặp với tất cả chữ màu trắng sáng."""

    dap_an_thay_doi = pyqtSignal(str)

    def __init__(self, dict_ghep_cap, dap_an_hien_tai="", parent=None):
        super().__init__(parent)
        self.dict_ghep_cap = dict_ghep_cap
        self.combo_boxes = {}
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 5, 0, 5)
        layout.setSpacing(10)

        danh_sach_y_b = list(self.dict_ghep_cap.values())

        for cot_a, cot_b_dung in self.dict_ghep_cap.items():
            row_frame = QFrame()
            row_frame.setProperty("class", "card-widget")
            row_layout = QHBoxLayout(row_frame)

            lbl_a = QLabel(cot_a)
            lbl_a.setStyleSheet("font-weight: bold; font-size: 15px; color: #FFFFFF;")

            lbl_ghep = QLabel("ghép với: ")
            lbl_ghep.setStyleSheet("color: #FFFFFF; font-size: 15px;")

            cbo = QComboBox()
            cbo.setStyleSheet("color: #FFFFFF; font-weight: bold; font-size: 15px;")
            cbo.addItem("-- Chọn ý phù hợp --")
            cbo.addItems(danh_sach_y_b)
            cbo.currentTextChanged.connect(self.cap_nhat_ghep_cap)

            row_layout.addWidget(lbl_a, 1)
            row_layout.addWidget(lbl_ghep)
            row_layout.addWidget(cbo, 2)

            layout.addWidget(row_frame)
            self.combo_boxes[cot_a] = cbo

    def cap_nhat_ghep_cap(self):
        ket_qua = []
        for cot_a, cbo in self.combo_boxes.items():
            val = cbo.currentText()
            if val and not val.startswith("--"):
                ket_qua.append(f"{cot_a} -> {val}")
        
        self.dap_an_thay_doi.emit(" | ".join(ket_qua))


class KhungSapXep(QWidget):
    """Giao diện tương tác sắp xếp thứ tự chữ trắng."""

    dap_an_thay_doi = pyqtSignal(str)

    def __init__(self, danh_sach_buoc, dap_an_hien_tai="", parent=None):
        super().__init__(parent)
        self.danh_sach_buoc = list(danh_sach_buoc)
        self.init_ui()

    def init_ui(self):
        self.layout_chinh = QVBoxLayout(self)
        self.layout_chinh.setContentsMargins(0, 5, 0, 5)
        self.layout_chinh.setSpacing(8)
        self.tai_lai_giao_dien()

    def tai_lai_giao_dien(self):
        for i in reversed(range(self.layout_chinh.count())):
            item = self.layout_chinh.itemAt(i)
            if item.widget():
                item.widget().setParent(None)

        for idx, text in enumerate(self.danh_sach_buoc):
            card = QFrame()
            card.setProperty("class", "card-widget")
            card_layout = QHBoxLayout(card)

            lbl_stt = QLabel(f"Bước {idx + 1}:")
            lbl_stt.setStyleSheet("font-weight: bold; color: #FFFFFF; font-size: 15px;")

            lbl_text = QLabel(text)
            lbl_text.setStyleSheet("font-size: 15px; color: #FFFFFF; font-weight: bold;")

            btn_up = QPushButton("Lên")
            btn_up.setProperty("class", "btn-secondary")
            btn_up.setStyleSheet("color: #FFFFFF; font-weight: bold;")
            btn_up.setEnabled(idx > 0)
            btn_up.clicked.connect(lambda checked, i=idx: self.di_chuyen(i, -1))

            btn_down = QPushButton("Xuống")
            btn_down.setProperty("class", "btn-secondary")
            btn_down.setStyleSheet("color: #FFFFFF; font-weight: bold;")
            btn_down.setEnabled(idx < len(self.danh_sach_buoc) - 1)
            btn_down.clicked.connect(lambda checked, i=idx: self.di_chuyen(i, 1))

            card_layout.addWidget(lbl_stt)
            card_layout.addWidget(lbl_text, 1)
            card_layout.addWidget(btn_up)
            card_layout.addWidget(btn_down)

            self.layout_chinh.addWidget(card)

        self.cap_nhat_dap_an()

    def di_chuyen(self, index, huong):
        target = index + huong
        if 0 <= target < len(self.danh_sach_buoc):
            self.danh_sach_buoc[index], self.danh_sach_buoc[target] = self.danh_sach_buoc[target], self.danh_sach_buoc[index]
            self.tai_lai_giao_dien()

    def cap_nhat_dap_an(self):
        chuoi_ket_qua = " -> ".join(self.danh_sach_buoc)
        self.dap_an_thay_doi.emit(chuoi_ket_qua)
