# Thu muc: xu_ly_bong_da
# File: quan_ly_tran_dau.py
# Mo ta: Mo phong Tran Cau Dinh Cao 90 phut voi 8 tinh huong chien thuat, chien thuat tran va co che sut 30% vao, 30% khong vao, 40% do ban quyet dinh

import random

def lay_danh_sach_doi_thu():
    """Tra ve danh sach cac doi thu sieu manh de nguoi choi thach dau."""
    return [
        {
            "id": "opp_allstars",
            "ten": "Sieu Sao The Gioi All-Stars",
            "suc_manh": 94,
            "huan_luyen_vien": "Pep Guardiola",
            "loi_choi": "Tiki-taka kiem soat bong vuot troi va ban bat ngan"
        },
        {
            "id": "opp_europe",
            "ten": "Lien Quan Chau Au UEFA Legends",
            "suc_manh": 92,
            "huan_luyen_vien": "Carlo Ancelotti",
            "loi_choi": "Chuyen trang thai chong mat va phan cong sac ben"
        },
        {
            "id": "opp_vietnam",
            "ten": "The He Vang Viet Nam All-Stars",
            "suc_manh": 89,
            "huan_luyen_vien": "Park Hang-seo",
            "loi_choi": "Phong ngu ky luat thep va tinh than kien cuong khong bao gio bo cuoc"
        },
        {
            "id": "opp_southamerica",
            "ten": "Con Mua Samba Nam My CONMEBOL",
            "suc_manh": 93,
            "huan_luyen_vien": "Lionel Scaloni",
            "loi_choi": "Ky thuat ca nhan ma thuat va nhung pha dot pha tao dot bien"
        }
    ]

def lay_danh_sach_chien_thuat_tran():
    """Tra ve 3 che do dieu chinh chien thuat trong tran dau."""
    return [
        {
            "id": "pressing",
            "ten": "Pressing Tam Cao",
            "mo_ta": "Don toan luc sang phan san doi phuong, ap sat lien tuc de gianh lai quyen kiem soat",
            "hieu_qua": "Tang kha nang tao ra co hoi dut diem them 20% nhung ton the luc ve cuoi tran"
        },
        {
            "id": "tikitaka",
            "ten": "Kiem Soat Tiki-taka",
            "mo_ta": "Chuyen bong lien tuc voi cu ly ngan, keo gian doi hinh doi phuong va giu nhiem nhip do tran dau",
            "hieu_qua": "Giam ti le doi phuong tan cong, bao toan the luc cho toan doi"
        },
        {
            "id": "counter",
            "ten": "Phong Ngu Phan Cong Bien",
            "mo_ta": "Keo thap doi hinh phong ngu chu dong, cho doi sai lam cua doi thu de phat dong phan cong chop nhoang",
            "hieu_qua": "Cuc ky loi hai khi doi phuong dang qua cao, phu hop khi dang dan ban"
        }
    ]

def tinh_xac_suat_sut_bong(nguoi_choi_chon_dung):
    """
    Quy tac xac suat nghiem ngat:
    - 30% vao luoi tuyet doi (bat chap dung hay sai)
    - 30% khong vao (bat chap dung hay sai)
    - 40% con lai hoan toan do quyet dinh cua nguoi choi (dung = vao, sai = khong vao)
    """
    ti_le = random.random()
    if ti_le < 0.30:
        vao = True
        ly_do = "Cu sut qua hiem hoc khien thu mon khong the can pha!"
    elif ti_le < 0.60:
        vao = False
        ly_do = "Thu mon da bay nguoi xuat than hoac bong cham xa ngang cot doc bat ra!"
    else:
        vao = bool(nguoi_choi_chon_dung)
        if vao:
            ly_do = "Quyet dinh chien thuat chinh xac da giup cau thu dut diem hoan hao!"
        else:
            ly_do = "Quyet dinh chien thuat chua dung khien pha dut diem bi lo nhip."
    
    return {
        "vao": vao,
        "ly_do": ly_do,
        "xac_suat_nhom": "30% vao" if ti_le < 0.30 else ("30% khong vao" if ti_le < 0.60 else "40% do ban quyet dinh")
    }

def khoi_tao_tran_dau_dinh_cao(doi_thu_id="opp_allstars"):
    """Khoi tao mot tran dau 90 phut voi 8 tinh huong chien thuat kich tinh theo tung giai doan tran dau."""
    doi_thu_map = {d["id"]: d for d in lay_danh_sach_doi_thu()}
    doi_thu = doi_thu_map.get(doi_thu_id, lay_danh_sach_doi_thu()[0])
    
    tinh_huong = [
        {
            "phut": 12,
            "tieu_de": "Mo man: Dot pha canh va chuyen bong xuyen tuyen",
            "mo_ta_tinh_huong": "Tien dao canh doi nha cam bong dot pha ben hanh lang trai, hai hau ve doi ban dang lao ra ap sat. Ban se chi dao xu ly nhu the nao?",
            "cau_hoi": "De qua bong di cuon xoay vong cung ra sau lung hang phong ngu doi ban vao cho tien dao cam bang vao, cau thu nen tiep xuc vao phan nao cua trai bong?",
            "cac_lua_chon": [
                {"phuong_an": "Sut vao ma trong mu ban chan de tao hieu ung Magnus cuon xoay", "dung": True},
                {"phuong_an": "Sut bang mui giay thang truc dien", "dung": False},
                {"phuong_an": "Sut bang got chan tu duoi len", "dung": False}
            ],
            "binh_luan_dung": "VAOOOO! Mot pha cat bong sieu hang tao hieu ung xoay Magnus hoan hao, tien dao cam bang vao dem bong tung luoi mo ti so!",
            "binh_luan_sai": "Rat tiec, pha tiep xuc bong thieu chinh xac da khien qua bong di nhe va nam gon trong tay thu mon doi ban."
        },
        {
            "phut": 26,
            "tieu_de": "Da phat truc tiep hang rao cu ly 22 met",
            "mo_ta_tinh_huong": "Doi nha duoc huong qua phat sat vong cam. Hang rao doi ban gom 5 nguoi cao to bat nhay.",
            "cau_hoi": "Khoang cach tu qua bong den hang rao doi phuong theo luat FIFA quy dinh toi thieu la bao nhieu met?",
            "cac_lua_chon": [
                {"phuong_an": "9.15 met (tuong duong 10 yards)", "dung": True},
                {"phuong_an": "5.5 met", "dung": False},
                {"phuong_an": "11 met", "dung": False}
            ],
            "binh_luan_dung": "SIUUUU! Cu sut phat theo phong cach Knuckleball hinh la vang roi cam thang vao goc chu A! Khong the can pha!",
            "binh_luan_sai": "Bong cham dung dau mot cau thu tren hang rao va di chech cot doc ra ngoai duong bien ngang."
        },
        {
            "phut": 38,
            "tieu_de": "Canh giac: Bay viet vi cua doi thu",
            "mo_ta_tinh_huong": "Tien ve dang chuan bi chot khe. Cac hau ve doi ban bat ngo dong loat buoc len 2 nhip tao bay viet vi.",
            "cau_hoi": "Tien dao doi nha can lam gi vao thoi diem tien ve bat dau tiep xuc bong de khong bi vi pham luat viet vi?",
            "cac_lua_chon": [
                {"phuong_an": "Dung tren hoac ngang hang voi hau ve cuoi thu hai cua doi ban roi moi burt toc", "dung": True},
                {"phuong_an": "Chay truoc xuong sat thu mon de doi bong", "dung": False},
                {"phuong_an": "Dung sau lung thu mon doi phuong", "dung": False}
            ],
            "binh_luan_dung": "DI CHUYEN THONG MINH! Tien dao da pha bay viet vi ngoan muc, thoat xuong tung cu sut cheo goc hiem hoc!",
            "binh_luan_sai": "Tieng coi vang len! Tien dao doi nha da dung o vi tri viet vi truoc khi bong roi chan dong doi."
        },
        {
            "phut": 52,
            "tieu_de": "Hiep hai: Phan cong chop nhoang 3 danh 2",
            "mo_ta_tinh_huong": "Doi ban dang dang cao doi hinh thi mat bong. Doi nha to chuc phan cong sieu toc voi bo 3 tan cong.",
            "cau_hoi": "Neu qua bong bay voi van toc 90 km/h vuot qua quang duong 45 met toi vi tri tien dao, thi thoi gian bong bay la bao nhieu giay?",
            "cac_lua_chon": [
                {"phuong_an": "1.8 giay (vi 90 km/h = 25 m/s, thoi gian t = 45 / 25 = 1.8s)", "dung": True},
                {"phuong_an": "3.5 giay", "dung": False},
                {"phuong_an": "0.5 giay", "dung": False}
            ],
            "binh_luan_dung": "TUYET VOI! Duong chuyen vuot tuyen chuan xac tung mi-li-met, tien dao nhan bong tung cu sut cheo goc nhan doi cach biet!",
            "binh_luan_sai": "Do tinh toan sai thoi diem buoc chay nen tien dao da khong the don duoc duong chuyen."
        },
        {
            "phut": 65,
            "tieu_de": "Phong ngu can pha: Doi mat thu mon trong vong 16m50",
            "mo_ta_tinh_huong": "Tien dao doi ban thoat xuong doi mat voi thu mon doi nha trong vong cam.",
            "cau_hoi": "De thu hep goc sut cua tien dao doi phuong, thu mon doi nha can thuc hien dong tac nao sau day?",
            "cac_lua_chon": [
                {"phuong_an": "Chu dong lao ra rut ngan khoang cach va giang rong hai tay ha thap trong tam", "dung": True},
                {"phuong_an": "Dung yen tren vach voi khung thanh cho doi", "dung": False},
                {"phuong_an": "Nhay sang mot ben goc som", "dung": False}
            ],
            "binh_luan_dung": "CAN PHA XUAT THAN! Thu mon da bang ra rat nhanh khep goc sut khien cu sut cua doi ban dap trung nguoi doi ra ngoai!",
            "binh_luan_sai": "Tien dao doi ban da kheo leo danh lua va ghi ban rut ngan ti so tran dau."
        },
        {
            "phut": 76,
            "tieu_de": "Khong chien: Pha phat goc phut 76",
            "mo_ta_tinh_huong": "Doi nha duoc huong qua phat goc. Cac trung ve cao to da dang len tham gia khong chien.",
            "cau_hoi": "Khi mot cau thu bat cao danh dau, de qua bong di cam hiem hoc xuong goc luoi, diem tiep xuc tot nhat tren qua bong la gi?",
            "cac_lua_chon": [
                {"phuong_an": "Dung tran tiep xuc vao nua tren cua qua bong kem theo gap co nhe", "dung": True},
                {"phuong_an": "Dung dinh dau tiep xuc vao day duoi qua bong", "dung": False},
                {"phuong_an": "Dung tai de danh dau", "dung": False}
            ],
            "binh_luan_dung": "DANH DAU HOAN HAO! Cu danh dau cam xuong dat khien thu mon phai bo tay nhin bong bay vao luoi!",
            "binh_luan_sai": "Pha danh dau bi loi nhip, bong bay vot xa ngang len khan dai."
        },
        {
            "phut": 85,
            "tieu_de": "Thu thach the luc: Chong phan cong cuoi tran",
            "mo_ta_tinh_huong": "Phut 85, cau thu hai ben da bat dau co dau hieu xuong suc. Doi ban dang co gang don ep.",
            "cau_hoi": "Sau 80 phut thi dau cuong do cao, hien tuong chuot rut (co cung co bap) o cau thu thuong do nguyen nhan chu yeu nao?",
            "cac_lua_chon": [
                {"phuong_an": "Mat nuoc, thieu hut chat dien giai (Natri, Kali) va tich tu axit lactic trong co bap", "dung": True},
                {"phuong_an": "Uong qua nhieu nuoc loc", "dung": False},
                {"phuong_an": "Ngu qua nhieu vao ban dem", "dung": False}
            ],
            "binh_luan_dung": "BAN LINH KHOA HOC! Nho bo sung nuoc dien giai kip thoi, doi nha van duy tri cu ly doi hinh kin ke be gay moi pha tan cong!",
            "binh_luan_sai": "Doi nha de lo khoang trong vi xuong suc, doi ban co co hoi nguy hiem."
        },
        {
            "phut": 90,
            "tieu_de": "Phut bu gio 90+2: Qua phat den Penalty dinh doat tran dau",
            "mo_ta_tinh_huong": "Phut bu gio cuoi cung 90+2, doi nha duoc huong qua phat den penalty sau mot pha truy can trai phep trong vong cam.",
            "cau_hoi": "Khi thuc hien qua phat den Penalty tu cham 11m, luat FIFA quy dinh thu mon doi phuong phai giu vi tri nhu the nao truoc khi bong duoc da?",
            "cac_lua_chon": [
                {"phuong_an": "It nhat mot phan cua ban chan phai cham hoac o tren vach voi cau mon", "dung": True},
                {"phuong_an": "Duoc phep buoc len phia truoc 2 met de gay ap luc", "dung": False},
                {"phuong_an": "Phai ngoi xuong san", "dung": False}
            ],
            "binh_luan_dung": "BAN THANG QUYET DINH! Cu sut quyet doan vao goc cao khung thanh an dinh chien thang ve vang cho doi nha!",
            "binh_luan_sai": "Cu sut di qua cao so voi xa ngang, tieng coi ket thuc tran dau vang len."
        }
    ]
    
    return {
        "doi_thu": doi_thu,
        "ti_so_nha": 0,
        "ti_so_khach": 0,
        "tinh_huong_list": tinh_huong,
        "chien_thuat": lay_danh_sach_chien_thuat_tran()
    }
