# Thu muc: xu_ly_bong_da
# File: quan_ly_huyen_thoai.py
# Mo ta: Quan ly danh sach 14 huyen thoai bong da the gioi va bo cau hoi tri thuc the thao cho hoc sinh THCS

def lay_danh_sach_huyen_thoai():
    """Tra ve danh sach cac huyen thoai bong da the gioi va Viet Nam voi day du thong tin chi tiet."""
    return [
        {
            "id": "cr7",
            "ten": "Cristiano Ronaldo",
            "biet_danh": "CR7",
            "quoc_tich": "Bo Dao Nha",
            "vi_tri": "Tien dao",
            "so_ao": 7,
            "cau_lac_bo": "Al Nassr, Real Madrid, Manchester United",
            "ky_luc": "Hon 900 ban thang chinh thuc trong su nghiep, 5 Qua Bong Vang, 5 Champions League",
            "diem_noi_bat": "Ky luat the thao phi thuong, y chi vuot kho va kha nang bat cao danh dau ky luc 2.93m",
            "loi_khuyen": "Thanh cong khong phai su ngau nhien, do la su cham chi, kien tri va tinh than khong bao gio bo cuoc"
        },
        {
            "id": "messi",
            "ten": "Lionel Messi",
            "biet_danh": "El Pulga (Bo Chet Nguyen Tu)",
            "quoc_tich": "Argentina",
            "vi_tri": "Tien dao / Tien ve tan cong",
            "so_ao": 10,
            "cau_lac_bo": "Inter Miami, FC Barcelona, PSG",
            "ky_luc": "8 Qua Bong Vang lich su, Vo dich World Cup 2022, hon 800 ban thang",
            "diem_noi_bat": "Ky thuat re bong dinh cao, tam nhin chien thuat sieu hang va kha nang sut phat hang sao",
            "loi_khuyen": "Hay luon tin tuong vao ban than ngay ca khi nguoi khac nghi ngo chieu cao hay the hinh cua ban"
        },
        {
            "id": "pele",
            "ten": "Pele (Edson Arantes do Nascimento)",
            "biet_danh": "Vua Bong Da (The King)",
            "quoc_tich": "Brazil",
            "vi_tri": "Tien dao",
            "so_ao": 10,
            "cau_lac_bo": "Santos FC, New York Cosmos",
            "ky_luc": "Cau thu duy nhat lich su gianh 3 chuc vo dich World Cup (1958, 1962, 1970)",
            "diem_noi_bat": "Su toan dien tuyet doi ve ca hai chan, toc do va kha nang kien tao",
            "loi_khuyen": "Nhiem vu cua mot cau thu lon la truyen cam hung cho hang trieu tre em yeu thich the thao"
        },
        {
            "id": "maradona",
            "ten": "Diego Maradona",
            "biet_danh": "Cau Be Vang (El Pibe de Oro)",
            "quoc_tich": "Argentina",
            "vi_tri": "Tien ve tan cong",
            "so_ao": 10,
            "cau_lac_bo": "Napoli, FC Barcelona, Boca Juniors",
            "ky_luc": "Vo dich World Cup 1986 voi ban thang the ky re qua 5 cau thu Anh",
            "diem_noi_bat": "Kha nang cam bong ma thuat bang chan trai va tinh than thu linh bat diet",
            "loi_khuyen": "Niem dam me chay bong voi qua bong tron co the lam thay doi ca the gioi"
        },
        {
            "id": "ronaldo_r9",
            "ten": "Ronaldo de Lima",
            "biet_danh": "Nguoi Ngoai Hanh Tinh (Il Fenomeno)",
            "quoc_tich": "Brazil",
            "vi_tri": "Tien dao cam",
            "so_ao": 9,
            "cau_lac_bo": "Real Madrid, Inter Milan, FC Barcelona, AC Milan",
            "ky_luc": "2 lan vo dich World Cup (1994, 2002), Vua pha luoi World Cup 2002 voi 8 ban thang",
            "diem_noi_bat": "Ky thuat dao chan buoc cheo (step-over) o toc do sieu thanh vuot qua thu mon nhu mot con loc",
            "loi_khuyen": "Nhung chan thuong dau don nhat cung khong the dap tat khao khat tro lai san co"
        },
        {
            "id": "ronaldinho",
            "ten": "Ronaldinho Gaucho",
            "biet_danh": "Ao Thuat Gia San Co",
            "quoc_tich": "Brazil",
            "vi_tri": "Tien ve canh / Ho cong",
            "so_ao": 10,
            "cau_lac_bo": "FC Barcelona, AC Milan, PSG",
            "ky_luc": "Qua Bong Vang 2005, Vo dich World Cup 2002, Champions League 2006",
            "diem_noi_bat": "Luon no nu cuoi tren moi khi thi dau, sang tao ra cu elastico (lac bong bang mu ngoai roi ma trong) kinh dien",
            "loi_khuyen": "Bong da la niem vui. Khi ban choi bong voi tinh yeu thuan khiet, dieu ky dieu se tu den"
        },
        {
            "id": "zidane",
            "ten": "Zinedine Zidane",
            "biet_danh": "Zizou - Nhac Truong Hao Hoa",
            "quoc_tich": "Phap",
            "vi_tri": "Tien ve tan cong",
            "so_ao": 10,
            "cau_lac_bo": "Real Madrid, Juventus, Bordeaux",
            "ky_luc": "Cu dup ban thang Chung ket World Cup 1998, Cu vo-le the ky Chung ket Champions League 2002, 3 lan HLV vo dich C1 lien tiep",
            "diem_noi_bat": "Cu xoay compa roulette 360 do hoan hao va su binh tinh tuyet doi truoc moi vong vay",
            "loi_khuyen": "Su hao hoa khong chi o dong tac dep mat, ma o kha nang dua ra quyet dinh dung dan nhat trong tich tac"
        },
        {
            "id": "cruyff",
            "ten": "Johan Cruyff",
            "biet_danh": "Thanh Johan - Bo Oc Bong Da Tong Luc",
            "quoc_tich": "Ha Lan",
            "vi_tri": "Tien dao / Tien ve",
            "so_ao": 14,
            "cau_lac_bo": "Ajax Amsterdam, FC Barcelona",
            "ky_luc": "3 Qua Bong Vang Chau Au, dat nen mong cho triet ly Tiki-taka hien dai",
            "diem_noi_bat": "Dong tac danh lua Cruyff Turn ngoac bong sau chan tru lam bat ngo moi hau ve",
            "loi_khuyen": "Choi bong bang cai dau truoc khi choi bang doi chan. Don gian chinh la dinh cao cua su tinh te"
        },
        {
            "id": "beckenbauer",
            "ten": "Franz Beckenbauer",
            "biet_danh": "Hoang De Bong Da (Der Kaiser)",
            "quoc_tich": "Duc",
            "vi_tri": "Hau ve thong linh (Libero)",
            "so_ao": 5,
            "cau_lac_bo": "Bayern Munich, New York Cosmos",
            "ky_luc": "Vo dich World Cup ca tren tu cach cau thu (1974) va HLV truong (1990), 2 Qua Bong Vang",
            "diem_noi_bat": "Phat minh ra vi tri hau ve quet tan cong (Libero), phat dong tan cong tu tuyen duoi cuc ky lich lam",
            "loi_khuyen": "Nguoi chi huy thuc thu la nguoi truyen duoc su tu tin va diem tinh cho toan doi"
        },
        {
            "id": "mbappe",
            "ten": "Kylian Mbappe",
            "biet_danh": "Toc Do Sieu Am",
            "quoc_tich": "Phap",
            "vi_tri": "Tien dao",
            "so_ao": 9,
            "cau_lac_bo": "Real Madrid, PSG, AS Monaco",
            "ky_luc": "Lap hat-trick trong tran chung ket World Cup 2022, Vo dich World Cup 2018 khi 19 tuoi",
            "diem_noi_bat": "Toc do buoc chay 38 km/h va kha nang dut diem lanh lung vao goc xa",
            "loi_khuyen": "Tuoi tre khong phai la rao can, hay dam mo uoc lon va chung minh ban than tren san co"
        },
        {
            "id": "haaland",
            "ten": "Erling Haaland",
            "biet_danh": "Co May Ghi Ban",
            "quoc_tich": "Na Uy",
            "vi_tri": "Tien dao cam",
            "so_ao": 9,
            "cau_lac_bo": "Manchester City, Borussia Dortmund",
            "ky_luc": "Ky luc ghi 36 ban trong 1 mua giai Ngoai Hang Anh, cu an ba lich su",
            "diem_noi_bat": "Suc can luot phi thuong, chon vi tri hoan hao va ban nang san ban sac ben",
            "loi_khuyen": "Tap trung cao do vao tung co hoi va luon giu cho minh khat khao hoc hoi them moi ngay"
        },
        {
            "id": "modric",
            "ten": "Luka Modric",
            "biet_danh": "Nhac Truong",
            "quoc_tich": "Croatia",
            "vi_tri": "Tien ve trung tam",
            "so_ao": 10,
            "cau_lac_bo": "Real Madrid",
            "ky_luc": "Gianh Qua Bong Vang 2018, 6 lan vo dich Champions League",
            "diem_noi_bat": "Chuyen bong tri ma bang mu ngoai chan phai va kha nang dieu tiet nhip do tran dau",
            "loi_khuyen": "Kien nhan, tinh than dong doi va su thong minh chien thuat quy gia hon bat ky the luc co bap nao"
        },
        {
            "id": "quanghai",
            "ten": "Nguyen Quang Hai",
            "biet_danh": "Hai Con - Keo Trai Ma Thuat",
            "quoc_tich": "Viet Nam",
            "vi_tri": "Tien ve tan cong",
            "so_ao": 19,
            "cau_lac_bo": "Cong An Ha Noi, Ha Noi FC, Pau FC",
            "ky_luc": "Sieu pham Cau vong tuyet Thuong Chau 2018, Vo dich AFF Cup 2018, Qua Bong Vang Viet Nam",
            "diem_noi_bat": "Cac cu sut phat hang rao hinh vong cung sieu dep va kha nang tao dot bien trong khoanh khac",
            "loi_khuyen": "Hay luon no luc tap luyen vi mau co sac ao va niem tu hao cua que huong Viet Nam"
        },
        {
            "id": "huynhnhu",
            "ten": "Huynh Nhu",
            "biet_danh": "Nu Tuong San Co",
            "quoc_tich": "Viet Nam",
            "vi_tri": "Tien dao",
            "so_ao": 9,
            "cau_lac_bo": "Lank FC (Bo Dao Nha), CLB TP Ho Chi Minh",
            "ky_luc": "5 Qua Bong Vang Nu Viet Nam, doi truong dua doi tuyen nu du World Cup 2023",
            "diem_noi_bat": "Ky thuat xu ly bong tinh te, ban linh thi dau tai chau Au va su thong minh trong chay cho",
            "loi_khuyen": "Phu nu Viet Nam co the lam nen nhung dieu ky dieu neu luon kien tri voi uoc mo cua minh"
        }
    ]

def lay_cau_hoi_tri_thuc_bong_da():
    """Tra ve 10 cau hoi do vui tri thuc ve cac huyen thoai va giai dau bong da the gioi."""
    return [
        {
            "cau_hoi": "Cau thu duy nhat trong lich su bong da the gioi tung 3 lan vo dich FIFA World Cup la ai?",
            "dap_an": ["Pele", "Diego Maradona", "Cristiano Ronaldo", "Zinedine Zidane"],
            "dap_an_dung": "Pele",
            "giai_thich": "Pele (Brazil) da cung doi tuyen vo dich vao cac nam 1958 (khi moi 17 tuoi), 1962 va 1970."
        },
        {
            "cau_hoi": "Ban thang mang ten 'Cau vong tuyet' noi tieng cua Nguyen Quang Hai duoc ghi vao luoi doi tuyen nao?",
            "dap_an": ["U23 Uzbekistan", "U23 Qatar", "U23 Iraq", "U23 Han Quoc"],
            "dap_an_dung": "U23 Uzbekistan",
            "giai_thich": "Quang Hai ghi sieu pham da phat hinh vong cung trong tran chung ket U23 Chau A 2018 tai Thuong Chau giua troi tuyet trang."
        },
        {
            "cau_hoi": "Cristiano Ronaldo da ghi duoc hon bao nhieu ban thang chinh thuc trong su nghiep thi dau chuyen nghiep?",
            "dap_an": ["Hon 900 ban thang", "Hon 600 ban thang", "Hon 700 ban thang", "Hon 500 ban thang"],
            "dap_an_dung": "Hon 900 ban thang",
            "giai_thich": "Cristiano Ronaldo la cau thu dau tien trong lich su bong da hien dai vuot qua cot moc 900 ban thang chinh thuc."
        },
        {
            "cau_hoi": "Dong tac lua bong 360 do 'Roulette' xoay compa noi tieng the gioi duoc gan lien voi ten tuoi cua danh thu nao?",
            "dap_an": ["Zinedine Zidane", "Luka Modric", "Kylian Mbappe", "Erling Haaland"],
            "dap_an_dung": "Zinedine Zidane",
            "giai_thich": "Zidane da bien cu xoay Marseille Roulette thanh mot tac pham nghe thuat hoan hao khong the sao chep tren san co."
        },
        {
            "cau_hoi": "Cau thu nao dang giu ky luc gianh duoc nhieu Qua Bong Vang (Ballon d'Or) nhat trong lich su voi 8 danh hieu?",
            "dap_an": ["Lionel Messi", "Cristiano Ronaldo", "Johan Cruyff", "Michel Platini"],
            "dap_an_dung": "Lionel Messi",
            "giai_thich": "Lionel Messi da gianh tong cong 8 Qua Bong Vang vao cac nam 2009, 2010, 2011, 2012, 2015, 2019, 2021 va 2023."
        },
        {
            "cau_hoi": "Danh thu Ronaldo de Lima (R9) duoc nguoi ham mo the gioi dat cho biet danh noi tieng nao?",
            "dap_an": ["Nguoi Ngoai Hanh Tinh (Il Fenomeno)", "Vua Bong Da", "Cau Be Vang", "Ao Thuat Gia"],
            "dap_an_dung": "Nguoi Ngoai Hanh Tinh (Il Fenomeno)",
            "giai_thich": "Kha nang re bong qua thu mon o van toc sieu thanh cua R9 khien bao gioi thoi do ca ngoi anh den tu mot hanh tinh khac."
        },
        {
            "cau_hoi": "Ai la nguoi sang tao ra vi tri 'Libero' (Hau ve quet chi huy tan cong tu tuyen duoi) trong lich su bong da?",
            "dap_an": ["Franz Beckenbauer", "Franco Baresi", "Paolo Maldini", "Virgil van Dijk"],
            "dap_an_dung": "Franz Beckenbauer",
            "giai_thich": "Hoang de Beckenbauer da cach mang hoa nghe thuat phong ngu bang cach bien hau ve cuoi cung thanh nguoi phat dong tan cong."
        },
        {
            "cau_hoi": "Huyen thoai Johan Cruyff gan lien voi triet ly bong da noi tieng nao cua doi tuyen Ha Lan va Barcelona?",
            "dap_an": ["Bong da tong luc (Total Football)", "Do be tong Catenaccio", "Tat canh danh dau Kick and Rush", "Phong ngu khu vuc"],
            "dap_an_dung": "Bong da tong luc (Total Football)",
            "giai_thich": "Johan Cruyff la linh hon cua truong phai Bong da tong luc, noi moi cau thu deu co the hoan doi vi tri va tham gia tan cong cung nhu phong ngu."
        },
        {
            "cau_hoi": "Nu cau thu Viet Nam dau tien xuat ngoai thi dau thanh cong cho CLB Lank FC tai Bo Dao Nha la ai?",
            "dap_an": ["Huynh Nhu", "Tuyet Dung", "Chuong Thi Kieu", "Hai Yen"],
            "dap_an_dung": "Huynh Nhu",
            "giai_thich": "Huynh Nhu da thi dau xuat sac tai giai vo dich quoc gia Bo Dao Nha va giup nang tam hinh anh bong da nu Viet Nam."
        },
        {
            "cau_hoi": "Trong tran chung ket World Cup 2022 giua Phap va Argentina, cau thu nao da lap duoc mot cu Hat-trick (3 ban thang)?",
            "dap_an": ["Kylian Mbappe", "Lionel Messi", "Angel Di Maria", "Julian Alvarez"],
            "dap_an_dung": "Kylian Mbappe",
            "giai_thich": "Kylian Mbappe da ghi 3 ban thang vo cung ngoan muc giup Phap go hoa 3-3 sau 120 phut thi dau kich tinh."
        }
    ]
