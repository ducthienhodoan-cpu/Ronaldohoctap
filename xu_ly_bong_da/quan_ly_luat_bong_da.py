# Thu muc: xu_ly_bong_da
# File: quan_ly_luat_bong_da.py
# Mo ta: Cam nang Luat FIFA, Ky nang thuc chien, Phong ngua chan thuong va Khoa hoc Toan hoc THCS

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

def lay_cam_nang_ky_nang_va_phong_ngua_chan_thuong():
    """Tra ve cam nang huong dan ky nang ca nhan thuc chien va phong ngua chan thuong the thao cho hoc sinh THCS."""
    return [
        {
            "ten_ky_nang": "Ky thuat Sut mu chinh dien (Knuckleball)",
            "loai": "ky_nang",
            "cach_thuc_hien": "Chay da thang, dat chan tru cach bong 15-20cm, khoa cung co chan, tiep xuc dung tam qua bong bang phan mu giay chinh dien. Sau khi sut khong vung chan qua cao.",
            "hieu_qua": "Trai bong bay thang voi van toc rat cao, it xoay tao ra luc khi dong hoc khien bong lieng bat ngo lam thu mon khong the doan duoc quy dao."
        },
        {
            "ten_ky_nang": "Ky thuat Do buoc mot dinh chan (First Touch)",
            "loai": "ky_nang",
            "cach_thuc_hien": "Ha thap trong tam, mo rong ma trong long ban chan hoi ru ve sau dung khoanh khac bong cham vao chan de triet tieu xung luc cua qua bong.",
            "hieu_qua": "Trai bong nam ngay trong tam kiem soat cua ban, san sang de chuyen, sut hoac re qua nguoi trong nhip tiep theo."
        },
        {
            "ten_ky_nang": "Ky thuat Dao chan qua nguoi (Step-over)",
            "loai": "ky_nang",
            "cach_thuc_hien": "Dua chan vong qua phia truoc qua bong tu trong ra ngoai ma khong cham vao bong, nhac vai danh lua huong di chuyen roi dung mu ngoai chan kia day bong burt toc.",
            "hieu_qua": "Danh lua phan xa cua hau ve doi phuong, lam ho nghieng trong tam sang huong nguoc lai va de lo khoang trong."
        },
        {
            "ten_ky_nang": "Ky thuat Chuyen dai ma trong (Long Pass)",
            "loai": "ky_nang",
            "cach_thuc_hien": "Chan tru chech 45 do, dung phan ma trong tiep xuc nhe vao phan duoi cua trai bong de tao do xoay nguoc (backspin) giup bong bay bong roi roi em xuong chan dong doi.",
            "hieu_qua": "Chuyen doi trang thai tan cong tu san nha sang san doi phuong chi trong 2 giay, xe toang hang tien ve doi ban."
        },
        {
            "ten_ky_nang": "Khoi dong dong phong ngua dut day chang cheo (ACL)",
            "loai": "suc_khoe",
            "cach_thuc_hien": "Thuc hien khoi dong 10-15 phut truoc khi da bong gom: xoay khop co chan, khop goi, chay nang cao dui, chay buoc nho, bat nhay tiep dat bang mui chan voi dau goi hoi chui.",
            "hieu_qua": "Kich hoat cac nhom co quanh dau goi va co dui, giup khop goi vung chac, giam toi 70% nguy co chan thuong day chang cheo o lua tuoi hoc sinh."
        },
        {
            "ten_ky_nang": "Phong ngua lat somi co chan va cang co",
            "loai": "suc_khoe",
            "cach_thuc_hien": "Chon giay da bong vua van co dinh got, buoc day giay chac chan. Khi tranh chap tren khong, luon chu y tiep dat can bang bang ca hai chan, khong giam len chan doi phuong.",
            "hieu_qua": "Bao ve bao khop co chan, tranh bi bong gan hoac lat co chan gay nghi thi dau dai ngay."
        },
        {
            "ten_ky_nang": "Gian co tinh va bu nuoc dien giai sau tran dau",
            "loai": "suc_khoe",
            "cach_thuc_hien": "Sau tran dau khong nen ngoi nghi ngay lap tuc. Hay di bo nhe nhang 3 phut roi ep doc, ep ngang keo gian co dui va bap chan. Uong tung ngum nuoc khoang hoac nuoc dien giai nho.",
            "hieu_qua": "Dao thai axit lactic tich tu trong co bap, tranh bi chuot rut va hoi phuc the luc nhanh chong cho cac buoi hoc hom sau."
        }
    ]

def lay_khoa_hoc_toan_hoc_trong_bong_da():
    """Tra ve cac kien thuc Khoa hoc vat ly va Toan hoc THCS duoc ap dung truc quan trong bong da."""
    return [
        {
            "chu_de": "Hieu ung Magnus - Bi mat cu sut xoay hinh qua chuoi",
            "khoa_hoc": "Khi cau thu sut vao ria ngoai cua trai bong khien no xoay tron trong khi bay, su chanh lech ap suat khong khi o hai ben qua bong tao ra luc Magnus day trai bong uon cong theo quy dao hinh vong cung, danh lua thu mon.",
            "mon_hoc": "Vat Ly 8 (Ap suat va chuyen dong cua chat luu)"
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
    """Tra ve bo 8 cau hoi kiem tra kien thuc luat, the thao va khoa hoc the thao."""
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
        },
        {
            "cau_hoi": "De phong ngua hieu qua nhat nguy co dut day chang cheo truoc (ACL) khi da bong, hoc sinh can lam gi?",
            "dap_an": ["Khoi dong dong 10-15 phut va luyen ky thuat tiep dat bang mui chan", "Ngoi yen nghi ngoi truoc khi vao san", "Uong that nhieu nuoc co ga truoc tran", "Da that manh ngay tu phut dau tien"],
            "dap_an_dung": "Khoi dong dong 10-15 phut va luyen ky thuat tiep dat bang mui chan",
            "giai_thich": "Khoi dong dong giup lam am cac nhom co quanh khop goi, luyen tiep dat giam chan dong va giam toi 70% nguy co chan thuong day chang cheo."
        },
        {
            "cau_hoi": "Khi sut phat theo ky thuat Knuckleball (bong lieng khong xoay), cau thu tiep xuc vao phan nao cua qua bong?",
            "dap_an": ["Chinh giua tam qua bong bang phan mu giay chinh dien", "Vao ria ngoai mep bong", "Vao phan day duoi cua qua bong", "Dung mui giay choc cheo"],
            "dap_an_dung": "Chinh giua tam qua bong bang phan mu giay chinh dien",
            "giai_thich": "Tiep xuc chinh tam qua bong giup triet tieu do xoay, qua do khien luong khong khi quanh bong tao ra luc lieng bat ngo."
        },
        {
            "cau_hoi": "Theo luat FIFA, trong truong hop nao to tro ly VAR duoc quyen can thiep vao tran dau?",
            "dap_an": ["Ban thang, Phat den, The do truc tiep va Nhan dien sai cau thu", "Tat ca cac qua phat goc tren san", "Tat ca cac qua nem bien", "Khi cau thu phan doi trong tai"],
            "dap_an_dung": "Ban thang, Phat den, The do truc tiep va Nhan dien sai cau thu",
            "giai_thich": "Cong nghe VAR chi can thiep vao 4 truong hop buoc ngoat then chot nhat tran dau de tranh lam gian doan nhip do tran."
        },
        {
            "cau_hoi": "Sau tran dau bong da, hanh dong nao duoi day giup co bap dao thai axit lactic va giam dau moi tot nhat?",
            "dap_an": ["Di bo nhe nhang va thuc hien cac dong tac gian co tinh", "Ngoi bet xuong dat nghi ngay lap tuc", "Tam nuoc da lanh ngay tuc thi", "Nhay day lien tuc 30 phut"],
            "dap_an_dung": "Di bo nhe nhang va thuc hien cac dong tac gian co tinh",
            "giai_thich": "Di bo nhe va gian co tinh giup tuan hoan mau dua luong oxy den co bap, giup co dan ra va dao thai axit lactic tich tu."
        }
    ]
