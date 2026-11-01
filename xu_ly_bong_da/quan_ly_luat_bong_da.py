# Thu muc: xu_ly_bong_da
# File: quan_ly_luat_bong_da.py
# Mo ta: Cam nang Luat FIFA va ung dung Khoa hoc - Toan hoc THCS trong mon the thao bong da

def lay_cam_nang_luat_fifa():
    """Tra ve danh sach cac luat bong da FIFA co ban duoc giai thich de hieu nhat cho hoc sinh THCS."""
    return [
        {
            "ten_luat": "Luat Viet Vi (Offside)",
            "tom_tat": "Mot cau thu dung o vi tri viet vi neu ho o gan duong bien ngang san doi phuong hon ca qua bong va cau thu phong ngu cuoi cung thu hai cua doi phuong (thuong la hau ve cuoi sau thu mon) vao thoi diem dong doi chuyen bong cho ho.",
            "luu_y_de_nho": "Khong bi tinh viet vi neu cau thu nhan bong truc tiep tu qua Nem bien, Phat goc hoac Phat bong tu cau mon.",
            "ung_dung_chien_thuat": "Cac hau ve thuong chu dong dang cao de tao 'Bay viet vi' khien tien dao doi ban mat co hoi."
        },
        {
            "ten_luat": "Luat Phat Den (Penalty Kick)",
            "tom_tat": "Duoc ap dung khi cau thu doi phong ngu pham loi truc tiep (nhu can nguoi, chuoi sau hoac de bong cham tay co y) ben trong khu vuc 16m50 cua doi minh.",
            "luu_y_de_nho": "Qua phat duoc thuc hien tu cham 11 met. Chi co nguoi sut va thu mon doi phuong o trong vong cam, thu mon phai giu it nhat 1 chan cham vach voi khung thanh khi bong duoc sut.",
            "ung_dung_chien_thuat": "Ti le thanh cong cua cac cu sut penalty o bong da chuyen nghiep dat khoang 75% den 80%."
        },
        {
            "ten_luat": "Luat The Phat (The Vang va The Do)",
            "tom_tat": "Trong tai su dung The Vang de canh cao cac hanh vi pham loi nguy hiem, cau gio, phan doi trong tai. The Do truc tiep danh cho loi rat nghiem trong nhu danh nguoi, vao bong triet ha hoac dung tay can pha ban thang ro rang.",
            "luu_y_de_nho": "Nhan 2 The Vang trong mot tran tu dong thanh 1 The Do. Cau thu bi the do phai roi san va doi khong duoc thay nguoi (phai choi thieu nguoi).",
            "ung_dung_chien_thuat": "Fair Play - choi dep la gia tri cao nhat cua the thao, ton trong doi thu va phan quyet cua trong tai."
        },
        {
            "ten_luat": "Khu Vuc 16m50 va Khung Thanh Chuan FIFA",
            "tom_tat": "Kich thuoc san bong tieu chuan la chieu dai 100m - 110m va chieu rong 64m - 75m. Khung thanh co chieu rong 7.32m va chieu cao 2.44m.",
            "luu_y_de_nho": "Thu mon chi duoc phep dung tay bat bong trong pham vi vong cam 16m50 cua doi nha.",
            "ung_dung_chien_thuat": "Doi tuyen can tan dung toan bo be ngang cua san de keo gian hang phong ngu doi ban."
        },
        {
            "ten_luat": "Cong Nghe VAR (Video Assistant Referee)",
            "tom_tat": "To tro ly trong tai video su dung he thong camera sieu cham va vach ke viet vi ban tu dong 3D de ho tro trong tai chinh trong 4 truong hop: Ban thang, Phat den, The do truc tiep va Nhan dien sai cau thu.",
            "luu_y_de_nho": "Quyet dinh cuoi cung tren san luon thuoc ve Trong tai chinh sau khi tham khao man hinh ben duong pitch.",
            "ung_dung_chien_thuat": "Giup tran dau cong bang, minh bach va giam thieu sai sot con nguoi toi muc toi da."
        }
    ]

def lay_khoa_hoc_toan_hoc_trong_bong_da():
    """Tra ve cac kien thuc Khoa hoc vat ly va Toan hoc THCS duoc ap dung truc quan trong bong da."""
    return [
        {
            "chu_de": "Hieu ung Magnus - Bi mat cu sut xoay hinh qua chuoi",
            "khoa_hoc": "Khi cau thu sut vao ria ngoai cua trai bong khien no xoay tron trong khi bay, su chanh lech ap suat khong khi o hai ben qua bong tao ra luc Magnus day trai bong uon cong theo quy dao hinh vong cung, danh lua thu mon.",
            "mon_hoc": "Vat Ly 8 (Ap suat va chuyen dong)"
        },
        {
            "chu_de": "Van toc sut bong cua cau thu chuyen nghiep",
            "khoa_hoc": "Mot cu sut manh cua Ronaldo hay Haaland co the dat van toc 120 km/h (tuong duong khoang 33.3 m/s). O khoang cach 20 met, bong chi mat 0.6 giay de vao luoi, nhanh hon toc do phan xa trung binh cua con nguoi (0.2 - 0.3 giay).",
            "mon_hoc": "Toan & Vat Ly 7 (Cong thuc van toc v = s / t)"
        },
        {
            "chu_de": "Ti le kiem soat bong va Thong ke xG (Ban thang ky vong)",
            "khoa_hoc": "Ti le kiem soat bong duoc tinh bang: (Thoi gian doi co bong / Tong thoi gian bong song) x 100%. Chi so xG tinh xac suat ghi ban tu 0 den 1 dua vao vi tri sut, goc sut va so luong hau ve cheng ngang.",
            "mon_hoc": "Toan 7 & 8 (Ti le phan tram va Thong ke xac suat)"
        },
        {
            "chu_de": "Goc sut toi uu va Hinh hoc san co",
            "khoa_hoc": "Khi tien dao tien sat goc bien ngang, goc sut vao khung thanh bi thu hep dan thanh goc nhon rat nho. Khi doi mat thu mon o chinh dien vong 16m50, goc mo rong toi da tren 30 do giup tang ti le ghi ban len gap 4 lan.",
            "mon_hoc": "Hinh Hoc 7 (Cac goc trong tam giac va duong vuong goc)"
        }
    ]

def lay_cau_hoi_luat_va_khoa_hoc():
    """Tra ve bo cau hoi kiem tra kien thuc luat va khoa hoc the thao."""
    return [
        {
            "cau_hoi": "Hieu ung vat ly nao giup qua bong xoay tao quy dao bay uon cong vong cung qua hang rao?",
            "dap_an": ["Hieu ung Magnus", "Hieu ung Doppler", "Dinh luat Van vat hap dan", "Hieu ung Quang dien"],
            "dap_an_dung": "Hieu ung Magnus",
            "giai_thich": "Hieu ung Magnus la hien tuong vat ly xay ra khi mot vat the hinh cau quay tron trong chat luu (khong khi) tao ra luc day vuong goc voi huong chuyen dong."
        },
        {
            "cau_hoi": "Trong tinh huong nao sau day, cau thu se KHONG bao gio bi trong tai thoi phat viet vi?",
            "dap_an": ["Nhan bong truc tiep tu qua Nem bien", "Nhan duong chiec khe cua tien ve", "Nhan qua tat bong tu canh", "Chay cat mat hau ve doi ban"],
            "dap_an_dung": "Nhan bong truc tiep tu qua Nem bien",
            "giai_thich": "Luat FIFA quy dinh khong co loi viet vi trong cac tinh huong: Nem bien, Phat goc va Phat phat bong tu cau mon."
        },
        {
            "cau_hoi": "Mot qua bong duoc sut voi van toc 108 km/h. Doi ra don vi met tren giay (m/s) thi bang bao nhieu?",
            "dap_an": ["30 m/s", "25 m/s", "36 m/s", "20 m/s"],
            "dap_an_dung": "30 m/s",
            "giai_thich": "De doi tu km/h sang m/s, ta chia cho 3.6: 108 : 3.6 = 30 m/s."
        },
        {
            "cau_hoi": "Chieu cao chuan cua khung thanh trong thi dau bong da 11 nguoi quoc te la bao nhieu?",
            "dap_an": ["2.44 met", "2.10 met", "2.80 met", "3.00 met"],
            "dap_an_dung": "2.44 met",
            "giai_thich": "Theo luat FIFA, khung thanh co chieu cao 2.44m (8 feet) va chieu rong 7.32m (8 yards)."
        }
    ]
