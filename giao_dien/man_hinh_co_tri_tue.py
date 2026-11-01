# Thu muc: giao_dien
# File: man_hinh_co_tri_tue.py
# Mo ta: Man hinh PyQt6 Dau Tri Ky Thu gom Co Vua va Co Tuong danh cho hoc sinh THCS

import os
import random
from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton,
    QFrame, QMessageBox, QComboBox, QScrollArea
)
from PyQt6.QtCore import Qt
from PyQt6 import uic

from xu_ly_co_tri_tue.quan_ly_co_vua import (
    lay_danh_sach_quan_co_vua, lay_cac_nuoc_di_dac_biet_co_vua,
    lay_khai_cuoc_kinh_dien_co_vua, lay_don_chien_thuat_co_vua,
    lay_danh_nhan_co_vua, lay_kho_cau_do_co_vua
)
from xu_ly_co_tri_tue.quan_ly_co_tuong import (
    lay_danh_sach_quan_co_tuong, lay_dac_diem_ban_co_tuong,
    lay_sat_phap_kinh_dien_co_tuong, lay_the_tran_khai_cuoc_co_tuong,
    lay_danh_thu_co_tuong, lay_kho_cau_do_co_tuong
)
from xu_ly_co_tri_tue.quan_ly_ban_co import (
    lay_danh_sach_the_co_mau, doc_tien_do_co_tri_tue, xu_ly_tra_loi_cau_do
)
from xu_ly_am_thanh.quan_ly_am_thanh import QuanLyAmThanh

class ManHinhCoTriTue(QWidget):
    """Man hinh PyQt6 tich hop toan dien Co Vua va Co Tuong cho hoc sinh."""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.danh_sach_quan_cv = lay_danh_sach_quan_co_vua()
        self.danh_sach_quan_ct = lay_danh_sach_quan_co_tuong()
        self.danh_sach_the_co = lay_danh_sach_the_co_mau()
        self.cau_hoi_hien_tai = None
        self.che_do_cau_do = "tat_ca"

        self.init_ui()
        self.khoi_tao_du_lieu_man_hinh()

    def init_ui(self):
        ui_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "giao_dien_ui", "man_hinh_co_tri_tue.ui"))
        if os.path.exists(ui_path):
            uic.loadUi(ui_path, self)
        else:
            self.tao_giao_dien_du_phong()

        # Ket noi su kien nut bam
        if hasattr(self, "btnChonCoVua"):
            self.btnChonCoVua.clicked.connect(lambda: self.chuyen_che_do_cau_do("co_vua"))
        if hasattr(self, "btnChonCoTuong"):
            self.btnChonCoTuong.clicked.connect(lambda: self.chuyen_che_do_cau_do("co_tuong"))
        if hasattr(self, "btnCauDoTiep"):
            self.btnCauDoTiep.clicked.connect(self.tai_cau_do_ngau_nhien)

        if hasattr(self, "btnOptA"):
            self.btnOptA.clicked.connect(lambda: self.kiem_tra_dap_an_cau_do("A"))
        if hasattr(self, "btnOptB"):
            self.btnOptB.clicked.connect(lambda: self.kiem_tra_dap_an_cau_do("B"))
        if hasattr(self, "btnOptC"):
            self.btnOptC.clicked.connect(lambda: self.kiem_tra_dap_an_cau_do("C"))
        if hasattr(self, "btnOptD"):
            self.btnOptD.clicked.connect(lambda: self.kiem_tra_dap_an_cau_do("D"))

        if hasattr(self, "comboTheCoMau"):
            self.comboTheCoMau.currentIndexChanged.connect(self.thay_doi_the_co_mau)

    def tao_giao_dien_du_phong(self):
        layout = QVBoxLayout(self)
        lbl = QLabel("Dang nap giao dien Dau Tri Co Vua va Co Tuong...")
        lbl.setStyleSheet("color: #FFFFFF; font-size: 16px;")
        layout.addWidget(lbl)

    def khoi_tao_du_lieu_man_hinh(self):
        self.cap_nhat_thong_tin_tien_do()
        self.nap_danh_sach_quan_co_vua()
        self.nap_danh_sach_quan_co_tuong()
        self.nap_danh_sach_the_co_mau()
        self.tai_cau_do_ngau_nhien()

    def cap_nhat_thong_tin_tien_do(self):
        tien_do = doc_tien_do_co_tri_tue()
        danh_hieu = tien_do.get("danh_hieu", "Ky Thu Tap Su")
        exp = tien_do.get("tong_diem_exp", 0)
        if hasattr(self, "lblDanhHieu"):
            self.lblDanhHieu.setText(danh_hieu)
        if hasattr(self, "lblExpCo"):
            self.lblExpCo.setText(f"EXP Co: {exp}")

    def nap_danh_sach_quan_co_vua(self):
        if not hasattr(self, "layoutListQuanCoVua"):
            return

        # Xoa cac widget cu
        while self.layoutListQuanCoVua.count():
            item = self.layoutListQuanCoVua.takeAt(0)
            if item.widget():
                item.widget().deleteLater()

        for q in self.danh_sach_quan_cv:
            btn = QPushButton(f"{q['ten']} (Diem: {q['diem_gia_tri']})")
            btn.setStyleSheet("""
                QPushButton {
                    background-color: #374151; color: #FFFFFF;
                    font-size: 13px; font-weight: bold;
                    text-align: left; padding: 8px 12px;
                    border-radius: 6px; border-left: 4px solid #3B82F6;
                }
                QPushButton:hover { background-color: #4B5563; }
            """)
            btn.clicked.connect(lambda checked, piece=q: self.hien_thi_chi_tiet_co_vua(piece))
            self.layoutListQuanCoVua.addWidget(btn)

        self.layoutListQuanCoVua.addStretch()

        if self.danh_sach_quan_cv:
            self.hien_thi_chi_tiet_co_vua(self.danh_sach_quan_cv[0])

    def hien_thi_chi_tiet_co_vua(self, piece):
        if not hasattr(self, "layoutContentChiTietCoVua"):
            return

        while self.layoutContentChiTietCoVua.count():
            item = self.layoutContentChiTietCoVua.takeAt(0)
            if item.widget():
                item.widget().deleteLater()

        # Tieu de quan co
        lbl_ten = QLabel(f"QUAN CO: {piece['ten'].upper()} - KY HIEU: {piece['ky_hieu']}")
        lbl_ten.setStyleSheet("font-size: 16px; font-weight: bold; color: #60A5FA; margin-bottom: 6px;")
        self.layoutContentChiTietCoVua.addWidget(lbl_ten)

        # Hop thong tin cach di
        box_info = QFrame()
        box_info.setStyleSheet("background-color: #111827; border-radius: 8px; padding: 10px;")
        box_layout = QVBoxLayout(box_info)

        lbl_diem = QLabel(f"Diem gia tri quy doi: {piece['diem_gia_tri']} diem")
        lbl_diem.setStyleSheet("color: #FBBF24; font-weight: bold; font-size: 14px;")
        box_layout.addWidget(lbl_diem)

        lbl_di = QLabel(f"Cach di chuyen: {piece['cach_di']}")
        lbl_di.setWordWrap(True)
        lbl_di.setStyleSheet("color: #E5E7EB; font-size: 13px;")
        box_layout.addWidget(lbl_di)

        lbl_an = QLabel(f"Cach an quan: {piece['cach_an']}")
        lbl_an.setWordWrap(True)
        lbl_an.setStyleSheet("color: #E5E7EB; font-size: 13px;")
        box_layout.addWidget(lbl_an)

        lbl_note = QLabel(f"Luu y chien thuat: {piece['luu_y']}")
        lbl_note.setWordWrap(True)
        lbl_note.setStyleSheet("color: #34D399; font-size: 13px; font-weight: bold;")
        box_layout.addWidget(lbl_note)

        self.layoutContentChiTietCoVua.addWidget(box_info)

        # Khai cuoc kinh dien
        lbl_kc = QLabel("KHAI CUOC KINH DIEN VA LOI THE CHIEN THUAT")
        lbl_kc.setStyleSheet("font-size: 14px; font-weight: bold; color: #F59E0B; margin-top: 10px;")
        self.layoutContentChiTietCoVua.addWidget(lbl_kc)

        for kc in lay_khai_cuoc_kinh_dien_co_vua()[:2]:
            lbl_item = QLabel(f"{kc['ten']} ({kc['nuoc_di']}): {kc['y_nghia']}")
            lbl_item.setWordWrap(True)
            lbl_item.setStyleSheet("background-color: #111827; color: #D1D5DB; padding: 6px; border-radius: 6px; font-size: 12px;")
            self.layoutContentChiTietCoVua.addWidget(lbl_item)

        # Don chien thuat
        lbl_ct = QLabel("DON CHIEN THUAT CAN BAN")
        lbl_ct.setStyleSheet("font-size: 14px; font-weight: bold; color: #F59E0B; margin-top: 10px;")
        self.layoutContentChiTietCoVua.addWidget(lbl_ct)

        for ct in lay_don_chien_thuat_co_vua()[:2]:
            lbl_ct_item = QLabel(f"{ct['ten']}: {ct['mo_ta']}")
            lbl_ct_item.setWordWrap(True)
            lbl_ct_item.setStyleSheet("background-color: #111827; color: #D1D5DB; padding: 6px; border-radius: 6px; font-size: 12px;")
            self.layoutContentChiTietCoVua.addWidget(lbl_ct_item)

        self.layoutContentChiTietCoVua.addStretch()

    def nap_danh_sach_quan_co_tuong(self):
        if not hasattr(self, "layoutListQuanCoTuong"):
            return

        while self.layoutListQuanCoTuong.count():
            item = self.layoutListQuanCoTuong.takeAt(0)
            if item.widget():
                item.widget().deleteLater()

        for q in self.danh_sach_quan_ct:
            btn = QPushButton(f"{q['ten']}")
            btn.setStyleSheet("""
                QPushButton {
                    background-color: #374151; color: #FFFFFF;
                    font-size: 13px; font-weight: bold;
                    text-align: left; padding: 8px 12px;
                    border-radius: 6px; border-left: 4px solid #EF4444;
                }
                QPushButton:hover { background-color: #4B5563; }
            """)
            btn.clicked.connect(lambda checked, piece=q: self.hien_thi_chi_tiet_co_tuong(piece))
            self.layoutListQuanCoTuong.addWidget(btn)

        self.layoutListQuanCoTuong.addStretch()

        if self.danh_sach_quan_ct:
            self.hien_thi_chi_tiet_co_tuong(self.danh_sach_quan_ct[0])

    def hien_thi_chi_tiet_co_tuong(self, piece):
        if not hasattr(self, "layoutContentChiTietCoTuong"):
            return

        while self.layoutContentChiTietCoTuong.count():
            item = self.layoutContentChiTietCoTuong.takeAt(0)
            if item.widget():
                item.widget().deleteLater()

        lbl_ten = QLabel(f"QUAN CO: {piece['ten'].upper()} - KY HIEU: {piece['ky_hieu']}")
        lbl_ten.setStyleSheet("font-size: 16px; font-weight: bold; color: #F87171; margin-bottom: 6px;")
        self.layoutContentChiTietCoTuong.addWidget(lbl_ten)

        box_info = QFrame()
        box_info.setStyleSheet("background-color: #111827; border-radius: 8px; padding: 10px;")
        box_layout = QVBoxLayout(box_info)

        lbl_vt = QLabel(f"Vi tri xuat phat: {piece['vi_tri']}")
        lbl_vt.setStyleSheet("color: #FBBF24; font-weight: bold; font-size: 14px;")
        box_layout.addWidget(lbl_vt)

        lbl_di = QLabel(f"Cach di chuyen: {piece['cach_di']}")
        lbl_di.setWordWrap(True)
        lbl_di.setStyleSheet("color: #E5E7EB; font-size: 13px;")
        box_layout.addWidget(lbl_di)

        lbl_luat = QLabel(f"Quy tac dac biet: {piece['luat_dac_biet']}")
        lbl_luat.setWordWrap(True)
        lbl_luat.setStyleSheet("color: #34D399; font-size: 13px; font-weight: bold;")
        box_layout.addWidget(lbl_luat)

        self.layoutContentChiTietCoTuong.addWidget(box_info)

        # Sat phap kinh dien
        lbl_sp = QLabel("SAT PHAP KINH DIEN CO TUONG")
        lbl_sp.setStyleSheet("font-size: 14px; font-weight: bold; color: #F59E0B; margin-top: 10px;")
        self.layoutContentChiTietCoTuong.addWidget(lbl_sp)

        for sp in lay_sat_phap_kinh_dien_co_tuong()[:2]:
            lbl_sp_item = QLabel(f"{sp['ten']}: {sp['mo_ta']}")
            lbl_sp_item.setWordWrap(True)
            lbl_sp_item.setStyleSheet("background-color: #111827; color: #D1D5DB; padding: 6px; border-radius: 6px; font-size: 12px;")
            self.layoutContentChiTietCoTuong.addWidget(lbl_sp_item)

        # Danh thu
        lbl_dt = QLabel("KY THU TIEU BIEU")
        lbl_dt.setStyleSheet("font-size: 14px; font-weight: bold; color: #F59E0B; margin-top: 10px;")
        self.layoutContentChiTietCoTuong.addWidget(lbl_dt)

        for dt in lay_danh_thu_co_tuong()[:1]:
            lbl_dt_item = QLabel(f"{dt['ten']} ({dt['danh_hieu']}): {dt['loi_khuyen']}")
            lbl_dt_item.setWordWrap(True)
            lbl_dt_item.setStyleSheet("background-color: #111827; color: #D1D5DB; padding: 6px; border-radius: 6px; font-size: 12px;")
            self.layoutContentChiTietCoTuong.addWidget(lbl_dt_item)

        self.layoutContentChiTietCoTuong.addStretch()

    def nap_danh_sach_the_co_mau(self):
        if not hasattr(self, "comboTheCoMau"):
            return

        self.comboTheCoMau.clear()
        for the in self.danh_sach_the_co:
            self.comboTheCoMau.addItem(the["tieu_de"], the)

        if self.danh_sach_the_co:
            self.thay_doi_the_co_mau(0)

    def thay_doi_the_co_mau(self, index):
        if index < 0 or index >= len(self.danh_sach_the_co):
            return
        the = self.danh_sach_the_co[index]
        if hasattr(self, "lblTieuDeTheCo"):
            self.lblTieuDeTheCo.setText(the["tieu_de"].upper())
        if hasattr(self, "lblMoTaTheCo"):
            self.lblMoTaTheCo.setText(f"Mo ta the tran: {the['mo_ta']} (Ben di truoc: {the['ben_di_truoc']})")
        if hasattr(self, "lblNuocTiepTheo"):
            self.lblNuocTiepTheo.setText(f"Nuoc di toi uu: {the['nuoc_tiep_theo']}")
        if hasattr(self, "lblLoiKhuyenTheCo"):
            self.lblLoiKhuyenTheCo.setText(f"Bai hoc chien luoc: {the['loi_khuyen']}")

    def chuyen_che_do_cau_do(self, che_do):
        self.che_do_cau_do = che_do
        self.tai_cau_do_ngau_nhien()

    def tai_cau_do_ngau_nhien(self):
        if self.che_do_cau_do == "co_vua":
            kho = lay_kho_cau_do_co_vua()
        elif self.che_do_cau_do == "co_tuong":
            kho = lay_kho_cau_do_co_tuong()
        else:
            kho = lay_kho_cau_do_co_vua() + lay_kho_cau_do_co_tuong()

        if not kho:
            return

        self.cau_hoi_hien_tai = random.choice(kho)

        if hasattr(self, "lblTheCoMoTa"):
            self.lblTheCoMoTa.setText(f"Tinh huong: {self.cau_hoi_hien_tai.get('the_co', '')}")
        if hasattr(self, "lblCauHoiText"):
            self.lblCauHoiText.setText(self.cau_hoi_hien_tai.get("cau_hoi", ""))

        opts = self.cau_hoi_hien_tai.get("cac_lua_chon", [])
        buttons = [self.btnOptA, self.btnOptB, self.btnOptC, self.btnOptD]
        for idx, btn in enumerate(buttons):
            if idx < len(opts):
                btn.setText(opts[idx])
                btn.setVisible(True)
                btn.setEnabled(True)
                btn.setStyleSheet("background-color: #374151; color: #FFFFFF; font-size: 14px; font-weight: 500; text-align: left; padding: 10px 16px; border-radius: 8px; border: 1px solid #4B5563;")
            else:
                btn.setVisible(False)

        if hasattr(self, "lblKetQuaGiaiThich"):
            self.lblKetQuaGiaiThich.setText("Hay chon dap an chinh xac de nhan +30 XP va +15 Coin!")
            self.lblKetQuaGiaiThich.setStyleSheet("background-color: #111827; color: #34D399; padding: 10px; border-radius: 8px; font-size: 13px; font-weight: bold;")

    def kiem_tra_dap_an_cau_do(self, lua_chon):
        if not self.cau_hoi_hien_tai:
            return

        res = xu_ly_tra_loi_cau_do(self.cau_hoi_hien_tai["id"], lua_chon)
        buttons = {"A": self.btnOptA, "B": self.btnOptB, "C": self.btnOptC, "D": self.btnOptD}

        # Vo hieu hoa sau khi chon
        for btn in buttons.values():
            btn.setEnabled(False)

        if res.get("ket_qua") == "Dung":
            if lua_chon in buttons:
                buttons[lua_chon].setStyleSheet("background-color: #059669; color: #FFFFFF; font-size: 14px; font-weight: bold; text-align: left; padding: 10px 16px; border-radius: 8px; border: 2px solid #10B981;")
            if hasattr(self, "lblKetQuaGiaiThich"):
                self.lblKetQuaGiaiThich.setText(f"CHINH XAC! (+{res['xp_nhan']} XP, +{res['coin_nhan']} Coin)\nGiai thich: {res['giai_thich']}")
                self.lblKetQuaGiaiThich.setStyleSheet("background-color: #064E3B; color: #34D399; padding: 10px; border-radius: 8px; font-size: 13px; font-weight: bold;")
            QuanLyAmThanh.get_instance().phat_am_thanh_tra_loi_dung()
        else:
            if lua_chon in buttons:
                buttons[lua_chon].setStyleSheet("background-color: #DC2626; color: #FFFFFF; font-size: 14px; font-weight: bold; text-align: left; padding: 10px 16px; border-radius: 8px; border: 2px solid #EF4444;")
            dap_an_dung = res.get("dap_an_dung", "")
            if dap_an_dung in buttons:
                buttons[dap_an_dung].setStyleSheet("background-color: #059669; color: #FFFFFF; font-size: 14px; font-weight: bold; text-align: left; padding: 10px 16px; border-radius: 8px; border: 2px solid #10B981;")
            if hasattr(self, "lblKetQuaGiaiThich"):
                self.lblKetQuaGiaiThich.setText(f"CHUA CHINH XAC! (Dap an dung la {dap_an_dung})\nGiai thich: {res['giai_thich']}")
                self.lblKetQuaGiaiThich.setStyleSheet("background-color: #7F1D1D; color: #FCA5A5; padding: 10px; border-radius: 8px; font-size: 13px; font-weight: bold;")
            QuanLyAmThanh.get_instance().phat_am_thanh_tra_loi_sai()

        self.cap_nhat_thong_tin_tien_do()
