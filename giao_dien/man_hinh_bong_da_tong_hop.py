# Thu muc: giao_dien
# File: man_hinh_bong_da_tong_hop.py
# Mo ta: Man hinh Giao dien PyQt6 Sieu Sao Bong Da va Doi Hinh Trong Mo

import os
import random
from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton,
    QFrame, QMessageBox, QGridLayout, QComboBox, QScrollArea
)
from PyQt6.QtCore import Qt, QTimer
from PyQt6 import uic

from xu_ly_bong_da.quan_ly_huyen_thoai import lay_danh_sach_huyen_thoai, lay_cau_hoi_tri_thuc_bong_da
from xu_ly_bong_da.quan_ly_luat_bong_da import lay_cam_nang_luat_fifa, lay_cau_hoi_luat_va_khoa_hoc
from xu_ly_bong_da.quan_ly_doi_hinh import (
    lay_danh_sach_so_do, lay_kho_cau_thu_tuyen_chon, doc_doi_hinh_hien_tai,
    luu_doi_hinh_hien_tai, tinh_suc_manh_tong_hop
)
from xu_ly_bong_da.quan_ly_tran_dau import khoi_tao_tran_dau_dinh_cao
from xu_ly_hoc_tap.he_thong_thuong import cong_phan_thuong
from xu_ly_am_thanh.quan_ly_am_thanh import QuanLyAmThanh

class ManHinhBongDaTongHop(QWidget):
    """Man hinh PyQt6 tich hop Bach khoa huyen thoai, Xay dung doi hinh va Tran cau dinh cao."""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.danh_sach_ht = lay_danh_sach_huyen_thoai()
        self.kho_cau_thu = lay_kho_cau_thu_tuyen_chon()
        self.du_lieu_doi_hinh = doc_doi_hinh_hien_tai()
        self.tran_dau_hien_tai = None
        self.tinh_huong_idx = 0
        self.vi_tri_dang_chon = "ST"
        self.cau_hoi_quiz_hien_tai = None

        self.init_ui()
        self.nap_du_lieu_ban_dau()

    def init_ui(self):
        ui_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "giao_dien_ui", "man_hinh_bong_da_tong_hop.ui"))
        if os.path.exists(ui_path):
            uic.loadUi(ui_path, self)
        else:
            self.tao_giao_dien_du_phong()

        # Ket noi su kien Tab 1: Huyen thoai & Quiz
        if hasattr(self, "cboHuyenThoai"):
            self.cboHuyenThoai.currentIndexChanged.connect(self.khi_chon_huyen_thoai)
        if hasattr(self, "btnKhaoSatTriThuc"):
            self.btnKhaoSatTriThuc.clicked.connect(self.khoi_tao_cau_hoi_quiz)

        # Ket noi su kien Tab 2: Doi hinh
        if hasattr(self, "cboSoDo"):
            self.cboSoDo.currentIndexChanged.connect(self.khi_thay_doi_so_do)
        if hasattr(self, "btnLuuDoiHinh"):
            self.btnLuuDoiHinh.clicked.connect(self.luu_doi_hinh)
        if hasattr(self, "btnApDungCauThu"):
            self.btnApDungCauThu.clicked.connect(self.xep_cau_thu_vao_vi_tri)

        # Ket noi su kien Tab 3: Tran dau
        if hasattr(self, "btnKhoiChayTranDau"):
            self.btnKhoiChayTranDau.clicked.connect(self.bat_dau_tran_dau_dinh_cao)

    def nap_du_lieu_ban_dau(self):
        """Nap danh sach lua chon cho cac ComboBox."""
        # 1. ComboBox Huyen Thoai
        if hasattr(self, "cboHuyenThoai"):
            self.cboHuyenThoai.clear()
            for ht in self.danh_sach_ht:
                self.cboHuyenThoai.addItem(f"{ht['ten']} ({ht['biet_danh']})", ht)
            if self.danh_sach_ht:
                self.hien_thi_chi_tiet_huyen_thoai(self.danh_sach_ht[0])

        # 2. ComboBox So do chien thuat
        if hasattr(self, "cboSoDo"):
            self.cboSoDo.clear()
            for sd in lay_danh_sach_so_do():
                self.cboSoDo.addItem(sd["ten"], sd["id"])
            current_sd = self.du_lieu_doi_hinh.get("so_do", "4-3-3")
            idx = self.cboSoDo.findData(current_sd)
            if idx >= 0:
                self.cboSoDo.setCurrentIndex(idx)

        # 3. ComboBox Kho cau thu
        if hasattr(self, "cboKhoCauThu"):
            self.cboKhoCauThu.clear()
            for ct in self.kho_cau_thu:
                self.cboKhoCauThu.addItem(f"{ct['ten']} ({ct['vi_tri_chuan']} - {ct['ovr']} OVR - {ct['quoc_tich']})", ct["id"])

        self.ve_san_co_doi_hinh()
        self.cap_nhat_diem_doi_hinh()

    # --- TAB 1: HUYEN THOAI & TRI THUC BONG DA ---
    def khi_chon_huyen_thoai(self, index):
        if hasattr(self, "cboHuyenThoai") and index >= 0:
            ht = self.cboHuyenThoai.itemData(index)
            if ht:
                self.hien_thi_chi_tiet_huyen_thoai(ht)

    def hien_thi_chi_tiet_huyen_thoai(self, ht):
        if hasattr(self, "lblTenHT"):
            self.lblTenHT.setText(f"{ht['ten']} (Biet danh: {ht['biet_danh']}) - So ao: #{ht['so_ao']}")
        if hasattr(self, "lblThongTinChiTietHT"):
            nd = (
                f"Quoc tich: {ht['quoc_tich']} | Vi tri: {ht['vi_tri']}\n"
                f"Cau lac bo tung thi dau: {ht['cau_lac_bo']}\n"
                f"Ky luc noi bat: {ht['ky_luc']}\n"
                f"Diem doc dao tren san co: {ht['diem_noi_bat']}\n"
                f"Loi khuyen danh cho hoc sinh: \"{ht['loi_khuyen']}\""
            )
            self.lblThongTinChiTietHT.setText(nd)

    def khoi_tao_cau_hoi_quiz(self):
        cau_hoi_list = lay_cau_hoi_tri_thuc_bong_da() + lay_cau_hoi_luat_va_khoa_hoc()
        self.cau_hoi_quiz_hien_tai = random.choice(cau_hoi_list)

        if hasattr(self, "lblCauHoiQuiz"):
            self.lblCauHoiQuiz.setText(f"Cau hoi: {self.cau_hoi_quiz_hien_tai['cau_hoi']}")

        if hasattr(self, "lblKetQuaQuiz"):
            self.lblKetQuaQuiz.setText("")

        if hasattr(self, "gridDapAnQuiz"):
            # Xoa cac button cu
            while self.gridDapAnQuiz.count():
                item = self.gridDapAnQuiz.takeAt(0)
                w = item.widget()
                if w:
                    w.deleteLater()

            # Tao 4 button lua chon
            for idx, opt in enumerate(self.cau_hoi_quiz_hien_tai["dap_an"]):
                btn = QPushButton(opt)
                btn.setStyleSheet(
                    "background-color: #064E3B; color: #FFFFFF; font-weight: bold; font-size: 13.5px; "
                    "padding: 8px 12px; border-radius: 8px; border: 1.5px solid #06B6D4;"
                )
                btn.setCursor(Qt.CursorShape.PointingHandCursor)
                btn.clicked.connect(lambda checked, o=opt: self.kiem_tra_dap_an_quiz(o))
                r = idx // 2
                c = idx % 2
                self.gridDapAnQuiz.addWidget(btn, r, c)

    def kiem_tra_dap_an_quiz(self, lua_chon):
        if not self.cau_hoi_quiz_hien_tai:
            return
        dung = (lua_chon == self.cau_hoi_quiz_hien_tai["dap_an_dung"])
        gt = self.cau_hoi_quiz_hien_tai.get("giai_thich", "")

        if hasattr(self, "lblKetQuaQuiz"):
            if dung:
                self.lblKetQuaQuiz.setText(f"CHINH XAC! Ban da tra loi dung va nhan +30 XP! Giai thich: {gt}")
                self.lblKetQuaQuiz.setStyleSheet("font-size: 13.5px; font-weight: bold; color: #10B981;")
                cong_phan_thuong(xp=30)
                try:
                    QuanLyAmThanh.get_instance().phat_am_thanh_chien_thang()
                except Exception:
                    pass
            else:
                self.lblKetQuaQuiz.setText(f"CHUA CHINH XAC! Dap an dung la: {self.cau_hoi_quiz_hien_tai['dap_an_dung']}. Giai thich: {gt}")
                self.lblKetQuaQuiz.setStyleSheet("font-size: 13.5px; font-weight: bold; color: #EF4444;")

    # --- TAB 2: XAY DUNG DOI HINH 11 SIEU SAO ---
    def khi_thay_doi_so_do(self, index):
        if hasattr(self, "cboSoDo") and index >= 0:
            sd_id = self.cboSoDo.itemData(index)
            self.du_lieu_doi_hinh["so_do"] = sd_id
            self.ve_san_co_doi_hinh()
            self.cap_nhat_diem_doi_hinh()

    def ve_san_co_doi_hinh(self):
        if not hasattr(self, "gridSanCo"):
            return

        # Xoa widgets cu
        while self.gridSanCo.count():
            item = self.gridSanCo.takeAt(0)
            w = item.widget()
            if w:
                w.deleteLater()

        sd_id = self.du_lieu_doi_hinh.get("so_do", "4-3-3")
        da_chinh = self.du_lieu_doi_hinh.get("danh_sach_da_chinh", {})
        kho_dict = {c["id"]: c for c in self.kho_cau_thu}

        # Danh sach vi tri theo so do
        so_do_list = lay_danh_sach_so_do()
        sd_info = next((s for s in so_do_list if s["id"] == sd_id), so_do_list[0])
        cac_vi_tri = sd_info["vi_tri"]

        # Chia 11 vi tri thanh 4 hang tren san (Tien dao, Tien ve, Hau ve, Thu mon)
        hang_map = {
            # Hang 0: Tien dao
            "LW": (0, 0), "ST": (0, 1), "RW": (0, 2), "ST1": (0, 0), "ST2": (0, 2),
            # Hang 1: Tien ve
            "CAM": (1, 1), "CM": (1, 1), "CM1": (1, 0), "CM2": (1, 2), "CDM": (2, 1),
            "LM": (1, 0), "RM": (1, 2), "LWB": (1, 0), "RWB": (1, 2),
            # Hang 2: Hau ve
            "LB": (2, 0), "CB1": (2, 0), "CB2": (2, 1), "CB3": (2, 2), "RB": (2, 2),
            # Hang 3: Thu mon
            "GK": (3, 1)
        }

        row_counts = [0, 0, 0, 0]
        for v in cac_vi_tri:
            cid = da_chinh.get(v, "cauthu_1")
            ct = kho_dict.get(cid, self.kho_cau_thu[0])

            card = QFrame()
            card.setStyleSheet(
                "QFrame { background-color: #064E3B; border: 2px solid #10B981; border-radius: 10px; padding: 6px; } "
                "QFrame:hover { border-color: #F59E0B; background-color: #042F2E; }"
            )
            vbox = QVBoxLayout(card)
            vbox.setContentsMargins(4, 4, 4, 4)
            vbox.setSpacing(2)

            lbl_v = QLabel(v)
            lbl_v.setStyleSheet("font-size: 11px; font-weight: bold; color: #F59E0B;")
            lbl_v.setAlignment(Qt.AlignmentFlag.AlignCenter)
            vbox.addWidget(lbl_v)

            lbl_name = QLabel(ct["ten"])
            lbl_name.setStyleSheet("font-size: 12.5px; font-weight: bold; color: #FFFFFF;")
            lbl_name.setAlignment(Qt.AlignmentFlag.AlignCenter)
            vbox.addWidget(lbl_name)

            lbl_stat = QLabel(f"OVR: {ct['ovr']} | PAC: {ct['pac']} | SHO: {ct['sho']}")
            lbl_stat.setStyleSheet("font-size: 10.5px; color: #6EE7B7;")
            lbl_stat.setAlignment(Qt.AlignmentFlag.AlignCenter)
            vbox.addWidget(lbl_stat)

            btn_sel = QPushButton("Chon vi tri nay")
            btn_sel.setStyleSheet("background-color: #06B6D4; color: #022C22; font-size: 11px; font-weight: bold; border-radius: 4px; padding: 3px;")
            btn_sel.setCursor(Qt.CursorShape.PointingHandCursor)
            btn_sel.clicked.connect(lambda checked, pos=v: self.khi_click_vi_tri(pos))
            vbox.addWidget(btn_sel)

            # Phan phoi len grid
            target_row = 1
            if v == "GK":
                target_row = 3
            elif any(k in v for k in ["CB", "LB", "RB"]):
                target_row = 2
            elif any(k in v for k in ["CM", "CAM", "CDM", "LM", "RM", "LWB", "RWB"]):
                target_row = 1
            else:
                target_row = 0

            target_col = row_counts[target_row]
            row_counts[target_row] += 1
            self.gridSanCo.addWidget(card, target_row, target_col)

    def khi_click_vi_tri(self, vi_tri):
        self.vi_tri_dang_chon = vi_tri
        if hasattr(self, "lblThayViTri"):
            self.lblThayViTri.setText(f"Vi tri dang chon: {vi_tri}")

    def xep_cau_thu_vao_vi_tri(self):
        if not hasattr(self, "cboKhoCauThu"):
            return
        cid = self.cboKhoCauThu.currentData()
        if not cid:
            return

        if "danh_sach_da_chinh" not in self.du_lieu_doi_hinh:
            self.du_lieu_doi_hinh["danh_sach_da_chinh"] = {}

        self.du_lieu_doi_hinh["danh_sach_da_chinh"][self.vi_tri_dang_chon] = cid
        self.ve_san_co_doi_hinh()
        self.cap_nhat_diem_doi_hinh()

    def cap_nhat_diem_doi_hinh(self):
        diem = tinh_suc_manh_tong_hop(self.du_lieu_doi_hinh)
        if hasattr(self, "lblDiemDoiHinh"):
            self.lblDiemDoiHinh.setText(f"Suc Manh Toan Doi: {diem} OVR")

    def luu_doi_hinh(self):
        ok = luu_doi_hinh_hien_tai(self.du_lieu_doi_hinh)
        if ok:
            QMessageBox.information(self, "Thanh Cong", "Da luu doi hinh trong mo 11 sieu sao thanh cong vao he thong!")
        else:
            QMessageBox.warning(self, "Loi", "Khong the luu doi hinh xuong file du lieu.")

    # --- TAB 3: TRAN CAU DINH CAO 90 PHUT ---
    def bat_dau_tran_dau_dinh_cao(self):
        self.tran_dau_hien_tai = khoi_tao_tran_dau_dinh_cao("opp_allstars")
        self.tinh_huong_idx = 0
        self.cap_nhat_giao_dien_tran_dau()

    def cap_nhat_giao_dien_tran_dau(self):
        if not self.tran_dau_hien_tai:
            return

        td = self.tran_dau_hien_tai
        tinh_huong_list = td.get("tinh_huong_list", [])

        if self.tinh_huong_idx >= len(tinh_huong_list):
            # Ket thuc tran dau 90 phut
            ti_so_nha = td["ti_so_nha"]
            ti_so_khach = td["ti_so_khach"]
            msg = f"HET GIO! TRAN DAU KET THUC!\nTi so chung cuoc: Dream Team {ti_so_nha} - {ti_so_khach} {td['doi_thu']['ten']}\n"
            if ti_so_nha > ti_so_khach:
                msg += "Chuc mung ban da dan dat Dream Team chien thang oanh liet! Thuong +100 XP!"
                cong_phan_thuong(xp=100)
                try:
                    QuanLyAmThanh.get_instance().phat_am_thanh_chien_thang()
                except Exception:
                    pass
            elif ti_so_nha == ti_so_khach:
                msg += "Mot tran hoa day kich tinh giua hai doi sieu sao! Thuong +50 XP!"
                cong_phan_thuong(xp=50)
            else:
                msg += "Doi ban da that bai sat nut, hay tiep tuc ren luyen chien thuat nhe! Thuong +20 XP!"
                cong_phan_thuong(xp=20)

            QMessageBox.information(self, "Ket Thuc Tran Dau", msg)
            if hasattr(self, "lblThoiGianTranDau"):
                self.lblThoiGianTranDau.setText("Phut: 90' HET GIO")
            return

        th = tinh_huong_list[self.tinh_huong_idx]

        if hasattr(self, "lblTiSo"):
            self.lblTiSo.setText(f"{td['ti_so_nha']} - {td['ti_so_khach']}")
        if hasattr(self, "lblThoiGianTranDau"):
            self.lblThoiGianTranDau.setText(f"Phut: {th['phut']}'")
        if hasattr(self, "lblTieuDeTinhHuong"):
            self.lblTieuDeTinhHuong.setText(f"Phut {th['phut']}: {th['tieu_de']}")
        if hasattr(self, "lblMoTaTinhHuong"):
            self.lblMoTaTinhHuong.setText(th["mo_ta_tinh_huong"])
        if hasattr(self, "lblCauHoiChienThuat"):
            self.lblCauHoiChienThuat.setText(f"Thu thach chien thuat: {th['cau_hoi']}")

        # Hien thi cac nut lua chon
        if hasattr(self, "layoutOptionsTranDau"):
            while self.layoutOptionsTranDau.count():
                item = self.layoutOptionsTranDau.takeAt(0)
                w = item.widget()
                if w:
                    w.deleteLater()

            for opt in th["cac_lua_chon"]:
                btn = QPushButton(opt["phuong_an"])
                btn.setStyleSheet(
                    "background-color: #064E3B; color: #FFFFFF; font-weight: bold; font-size: 14px; "
                    "padding: 10px 14px; border-radius: 8px; border: 1.5px solid #06B6D4; text-align: left;"
                )
                btn.setCursor(Qt.CursorShape.PointingHandCursor)
                btn.clicked.connect(lambda checked, o=opt, t=th: self.xu_ly_lua_chon_tinh_huong(o, t))
                self.layoutOptionsTranDau.addWidget(btn)

    def xu_ly_lua_chon_tinh_huong(self, opt, th):
        la_dung = opt.get("dung", False)
        td = self.tran_dau_hien_tai

        # Quy tac: 30% chac chan vao, 30% chac chan khong vao, 40% do ban quyet dinh
        r = random.random()
        if r < 0.30:
            la_ban_thang = True
            ly_do = " (30% sieu pham may man chac chan vao)"
        elif r < 0.60:
            la_ban_thang = False
            ly_do = " (30% bong dap cot doc xa ngang)"
        else:
            la_ban_thang = bool(la_dung)
            ly_do = " (40% do ban quyet dinh chinh xac)" if la_ban_thang else " (40% do phan doan chua dung)"

        if la_ban_thang:
            td["ti_so_nha"] += 1
            bl = f"{th['binh_luan_dung']}{ly_do}"
            cong_phan_thuong(xp=25)
            try:
                QuanLyAmThanh.get_instance().phat_am_thanh_chien_thang()
            except Exception:
                pass
        else:
            if random.random() < 0.6:
                td["ti_so_khach"] += 1
            bl = f"{th['binh_luan_sai']}{ly_do}"

        if hasattr(self, "lblBinhLuanVien"):
            self.lblBinhLuanVien.setText(f"Binh luan vien: {bl}")

        self.tinh_huong_idx += 1
        self.cap_nhat_giao_dien_tran_dau()

    def tao_giao_dien_du_phong(self):
        """Dung giao dien thu cong neu file .ui chua duoc tim thay."""
        layout = QVBoxLayout(self)
        lbl = QLabel("Giao dien Sieu Sao Bong Da dang duoc khoi tao...")
        lbl.setStyleSheet("color: #FFFFFF; font-size: 16px;")
        layout.addWidget(lbl)
