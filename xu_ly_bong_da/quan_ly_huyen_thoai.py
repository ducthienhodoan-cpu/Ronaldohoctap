# Thu muc: xu_ly_bong_da
# File: quan_ly_huyen_thoai.py
# Mo ta: Quan ly danh sach huyen thoai bong da va bo cau hoi do vui tri thuc bong da danh cho hoc sinh THCS

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
            "ky_luc": "Hon 900 ban thang chinh thuc trong su nghiep, 5 Qua Bong Vang",
            "diem_noi_bat": "Ky luat the thao phi thuong, y chi vuot kho va kha nang bat cao danh dau ky luc",
            "loi_khuyen": "Thanh cong khong phai su ngau nhien, do la su cham chi, kien tri va tinh than khong bao gio bo cuoc"
        },
        {
            "id": "messi",
            "ten": "Lionel Messi",
            "biet_danh": "El Pulga",
            "quoc_tich": "Argentina",
            "vi_tri": "Tien dao / Tien ve tan cong",
            "so_ao": 10,
            "cau_lac_bo": "Inter Miami, FC Barcelona, PSG",
            "ky_luc": "8 Qua Bong Vang, Vo dich World Cup 2022, hon 800 ban thang",
            "diem_noi_bat": "Ky thuat re bong dinh cao, tam nhin chien thuat sieu hang va kha nang sut phat hang sao",
            "loi_khuyen": "Hay luon tin tuong vao ban than ngay ca khi nguoi khac nghi ngo chieu cao hay the hinh cua ban"
        },
        {
            "id": "pele",
            "ten": "Pele (Edson Arantes do Nascimento)",
            "biet_danh": "Vua Bong Da",
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
            "biet_danh": "Cau Be Vang",
            "quoc_tich": "Argentina",
            "vi_tri": "Tien ve tan cong",
            "so_ao": 10,
            "cau_lac_bo": "Napoli, FC Barcelona, Boca Juniors",
            "ky_luc": "Vo dich World Cup 1986 voi ban thang the ky re qua 5 cau thu Anh",
            "diem_noi_bat": "Kha nang cam bong ma thuat bang chan trai va tinh than thu linh bat diet",
            "loi_khuyen": "Niem dam me chay bong voi qua bong tron co the lam thay doi ca the gioi"
        },
        {
            "id": "mbappe",
            "ten": "Kylian Mbappe",
            "biet_danh": "Ninja Rua",
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
            "ky_luc": "Gianh Qua Bong Vang 2018, dua Croatia vao Chung ket World Cup 2018 va Hang 3 World Cup 2022",
            "diem_noi_bat": "Chuyen bong tri ma bang mu ngoai chan phai va kha nang dieu tiet nhip do tran dau",
            "loi_khuyen": "Kien nhan, tinh than dong doi va su thong minh chien thuat quy gia hon bat ky the luc co bap nao"
        },
        {
            "id": "quanghai",
            "ten": "Nguyen Quang Hai",
            "biet_danh": "Hai Con",
            "quoc_tich": "Viet Nam",
            "vi_tri": "Tien ve tan cong",
            "so_ao": 19,
            "cau_lac_bo": "Cong An Ha Noi, Ha Noi FC",
            "ky_luc": "Sieu pham Cau vong tuyet Thuong Chau 2018, Vo dich AFF Cup 2018, Qua Bong Vang Viet Nam",
            "diem_noi_bat": "Chan trai cuc ky kheo leo, nhung qua sut phat dinh chop khien thu mon bat luc",
            "loi_khuyen": "Tu hao mau co sac ao Viet Nam, khong ngai doi dau voi cac doi thu manh chau luc"
        },
        {
            "id": "huynhnhu",
            "ten": "Huynh Nhu",
            "biet_danh": "Nu Cuoi Vang",
            "quoc_tich": "Viet Nam",
            "vi_tri": "Tien dao",
            "so_ao": 9,
            "cau_lac_bo": "TP Ho Chi Minh, Lank FC (Bo Dao Nha)",
            "ky_luc": "5 Qua Bong Vang nu Viet Nam ky luc, dan dat doi tuyen nu du World Cup 2023",
            "diem_noi_bat": "Ky thuat xu ly bong tinh te, ban linh thi dau tai chau Au va tinh than dong doi tuyet voi",
            "loi_khuyen": "Con gai cung co the choi bong da xuat sac va vuon ra bien lon the gioi"
        }
    ]

def lay_cau_hoi_tri_thuc_bong_da():
    """Tra ve danh sach cac cau hoi trac nghiem do vui ve bong da phu hop voi hoc sinh THCS."""
    return [
        {
            "cau_hoi": "Cau thu nao trong lich su bong da the gioi da gianh duoc 8 Qua Bong Vang danh gia?",
            "dap_an": ["Lionel Messi", "Cristiano Ronaldo", "Pele", "Zinedine Zidane"],
            "dap_an_dung": "Lionel Messi",
            "giai_thich": "Lionel Messi lap ky luc vo tien khoang hau voi 8 Qua Bong Vang sau chuc vo dich World Cup 2022."
        },
        {
            "cau_hoi": "Cau thu duy nhat trong lich su gianh duoc 3 chuc vo dich World Cup cung doi tuyen quoc gia la ai?",
            "dap_an": ["Pele", "Diego Maradona", "Ronaldo de Lima", "Franz Beckenbauer"],
            "dap_an_dung": "Pele",
            "giai_thich": "Huyen thoai Pele cua Brazil da vo dich World Cup vao cac nam 1958, 1962 va 1970."
        },
        {
            "cau_hoi": "Bao nhieu phut la thoi gian thi dau chinh thuc cua mot tran dau bong da 11 nguoi?",
            "dap_an": ["90 phut", "80 phut", "100 phut", "60 phut"],
            "dap_an_dung": "90 phut",
            "giai_thich": "Tran dau tieu chuan gom 2 hiep, moi hiep 45 phut khong ke thoi gian bu gio."
        },
        {
            "cau_hoi": "Khoang cach tu cham sut phat den (Penalty) den vach voi khung thanh la bao nhieu met?",
            "dap_an": ["11 met", "9.15 met", "16.5 met", "12 met"],
            "dap_an_dung": "11 met",
            "giai_thich": "Cham phat den cach chinh giua khung thanh dung 11 met (tuong duong 12 yards)."
        },
        {
            "cau_hoi": "Doi tuyen Quoc gia nao dang giu ky luc vo dich World Cup nhieu lan nhat the gioi voi 5 ngoi sao?",
            "dap_an": ["Brazil", "Duc", "Y", "Argentina"],
            "dap_an_dung": "Brazil",
            "giai_thich": "Doi tuyen Brazil da 5 lan vo dich World Cup vao cac nam 1958, 1962, 1970, 1994 va 2002."
        },
        {
            "cau_hoi": "Ban thang mang ten 'Cau vong trong tuyet' cua Nguyen Quang Hai duoc ghi vao luoi doi tuyen nao?",
            "dap_an": ["Uzbekistan", "Qatar", "Iraq", "Nhat Ban"],
            "dap_an_dung": "Uzbekistan",
            "giai_thich": "Sieu pham sut phat dep mat duoc thuc hien trong tran chung ket U23 Chau A 2018 tai Thuong Chau gap Uzbekistan."
        },
        {
            "cau_hoi": "Khi mot cau thu nhan du 2 the vang trong mot tran dau thi se phai chiu hinh phat gi?",
            "dap_an": ["The do gian tiep va bi truat quyen thi dau", "Phat tien mat", "Ngoi ghe du bi 10 phut", "Doi phai chiu phat den"],
            "dap_an_dung": "The do gian tiep va bi truat quyen thi dau",
            "giai_thich": "Theo luat FIFA, 2 the vang trong cung mot tran dau se tuong duong 1 the do, cau thu phai roi san ngay."
        },
        {
            "cau_hoi": "So luong cau thu chinh thuc cua moi doi tren san trong mot tran bong da tieu chuan la bao nhieu?",
            "dap_an": ["11 cau thu", "10 cau thu", "12 cau thu", "9 cau thu"],
            "dap_an_dung": "11 cau thu",
            "giai_thich": "Moi doi co 11 cau thu tren san, trong do bat buoc phai co 1 thu mon."
        }
    ]
