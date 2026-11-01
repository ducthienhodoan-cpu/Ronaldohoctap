# Thu muc: xu_ly_bong_da
# File: quan_ly_tran_dau.py
# Mo ta: Mo phong Tran Cau Dinh Cao 90 phut voi cac tinh huong chien thuat gay can va binh luan truc tiep

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
        }
    ]

def khoi_tao_tran_dau_dinh_cao(doi_thu_id="opp_allstars"):
    """Khoi tao mot tran dau 90 phut voi 5 tinh huong chien thuat then chot."""
    doi_thu_map = {d["id"]: d for d in lay_danh_sach_doi_thu()}
    doi_thu = doi_thu_map.get(doi_thu_id, lay_danh_sach_doi_thu()[0])
    
    tinh_huong = [
        {
            "phut": 18,
            "tieu_de": "Dot pha canh va chuyen bong xuyen tuyen",
            "mo_ta_tinh_huong": "Tien dao canh cua doi ban dang cam bong dot pha ben hanh lang trai, hai hau ve doi nha dang lao ra ap sat. Ban se chi dao xu ly nhu the nao?",
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
            "phut": 36,
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
            "phut": 55,
            "tieu_de": "Phan cong chop nhoang 3 danh 2",
            "mo_ta_tinh_huong": "Doi ban dang dang cao doi hinh thi mat bong. Doi nha to chuc phan cong sieu toc voi bo 3 tan cong.",
            "cau_hoi": "Neu qua bong bay voi van toc 90 km/h vuot qua quang duong 45 met toi vi tri tien dao, thi thoi gian bong bay la bao nhieu giay?",
            "cac_lua_chon": [
                {"phuong_an": "1.8 giay (vi 90 km/h = 25 m/s, thoi gian t = 45 / 25 = 1.8s)", "dung": True},
                {"phuong_an": "3.5 giay", "dung": False},
                {"phuong_an": "0.5 giay", "dung": False}
            ],
            "binh_luan_dung": "TUYET VOI! Duong chuyen vuot tuyen chuan xac tung mi-li-met, tien dao nhan bong tung cu sut cheo goc nhan doi cach biet!",
            "binh_luan_sai": "Do tinh toan sai thoi diem buoc chay nen tien dao da bi bat loi viet vi boi trong tai bien."
        },
        {
            "phut": 72,
            "tieu_de": "Phong ngu can pha pha doi mat nguy hiem",
            "mo_ta_tinh_huong": "Tien dao doi ban thoat xuong doi mat voi thu mon doi nha trong vong cam 16m50.",
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
            "phut": 90,
            "tieu_de": "Cu sut phat den Penalty an dinh tran dau",
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
        "tinh_huong_list": tinh_huong
    }
