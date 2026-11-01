# Thu muc: xu_ly_co_tri_tue
# File: quan_ly_co_vua.py
# Mo ta: Quan ly tri thuc co vua, luat choi, gia tri quan co, khai cuoc, don chien thuat va cau do THCS

def lay_danh_sach_quan_co_vua():
    """
    Tra ve danh sach 6 loai quan co vua, gia tri quy doi diem so va cach di chuyen.
    Thich hop cho hoc sinh THCS hieu ro ve gia tri quan de khong doi quan thiet.
    """
    return [
        {
            "id": "tot",
            "ten": "Tot (Pawn)",
            "ky_hieu": "P",
            "diem_gia_tri": 1,
            "cach_di": "Di thang 1 o moi nuoc (o nuoc dau tien duoc phep di 2 o). Khong duoc di lui.",
            "cach_an": "An cheo 1 o ve phia truoc.",
            "luu_y": "Tuy diem thap nhat nhung co kha nang phong cap thanh Hau khi xuong toi hang cuoi cung."
        },
        {
            "id": "ma",
            "ten": "Ma (Knight)",
            "ky_hieu": "N",
            "diem_gia_tri": 3,
            "cach_di": "Di theo hinh chu L (2 o mot huong va 1 o vuong goc).",
            "cach_an": "An quan tai o dich den cua hinh chu L.",
            "luu_y": "La quan co duy nhat co the nhay qua dau cac quan khac, rat nguy hiem khi danh don chia doi."
        },
        {
            "id": "tuong",
            "ten": "Tuong (Bishop)",
            "ky_hieu": "B",
            "diem_gia_tri": 3,
            "cach_di": "Di cheo theo cac o cung mau (o sang hoac o toi) khong gioi han so o neu khong bi chan.",
            "cach_an": "An quan tren duong cheo cua minh.",
            "luu_y": "Moi ky thu co 1 Tuong o sang va 1 Tuong o toi, can phoi hop cap Tuong de kiem soat toan ban co."
        },
        {
            "id": "xe",
            "ten": "Xe (Rook)",
            "ky_hieu": "R",
            "diem_gia_tri": 5,
            "cach_di": "Di ngang hoac doc theo cac hang va cot khong gioi han so o neu khong bi chan.",
            "cach_an": "An quan tren duong ngang hoac doc cua minh.",
            "luu_y": "Quan co nang manh me o giai doan trung cuoc va tan cuoc, tham gia vao nuoc Nhap thanh."
        },
        {
            "id": "hau",
            "ten": "Hau (Queen)",
            "ky_hieu": "Q",
            "diem_gia_tri": 9,
            "cach_di": "Ket hop suc manh cua ca Xe va Tuong: di ngang, doc hoac cheo khong gioi han so o.",
            "cach_an": "An quan tren moi duong di cua minh.",
            "luu_y": "Quan co manh nhat ban co, can tranh dua Hau ra tran qua som de khoi bi quan nhe doi thu tan cong."
        },
        {
            "id": "vua",
            "ten": "Vua (King)",
            "ky_hieu": "K",
            "diem_gia_tri": 999,
            "cach_di": "Di 1 o theo bat ky huong nao (ngang, doc, cheo) vao o khong bi chieu.",
            "cach_an": "An quan o bat ky o ke ben khong duoc quan doi phuong bao ve.",
            "luu_y": "Quan co quan trong nhat, mat Vua la thua cuoc (chieu het). Giai doan cuoi tran Vua tro thanh quan tan cong tich cuc."
        }
    ]

def lay_cac_nuoc_di_dac_biet_co_vua():
    """Tra ve danh sach cac quy tac dac biet trong co vua ma hoc sinh can biet."""
    return [
        {
            "ten": "Nhap thanh (Castling)",
            "dieu_kien": "Vua chua tung di chuyen va Xe chua tung di chuyen. Khong co quan nao o giua Vua va Xe. Vua khong dang bi chieu va khong di qua o bi doi thu kiem soat.",
            "cach_thuc_hien": "Nhap thanh gan (Canh Vua): Vua di 2 o sang phia Xe, Xe nhay qua Vua sang o ke ben. Nhap thanh xa (Canh Hau): Vua di 2 o sang phia Hau, Xe nhay qua Vua.",
            "muc_dich": "Dua Vua vao vi tri an toan phia goc ban co va nhanh chong dua Xe ra trung tam hoat dong."
        },
        {
            "ten": "Bat tot qua duong (En Passant)",
            "dieu_kien": "Khi Tot doi phuong di 2 o tu vi tri xuat phat va dung ngay ben canh Tot cua ban o hang ngang 5 (voi quan Trang) hoac hang ngang 4 (voi quan Den).",
            "cach_thuc_hien": "Ban co quyen an Tot do bang cach di cheo ra phia sau quan Tot do giong nhu no chi di 1 o.",
            "muc_dich": "Ngan chan viec Tot di 2 o de vuot qua vung kiem soat cua Tot doi phuong mot cach de dang. Chi duoc thuc hien ngay o nuoc di lien sau."
        },
        {
            "ten": "Phong cap (Pawn Promotion)",
            "dieu_kien": "Khi mot quan Tot tien toi hang cuoi cung cua ban co (hang 8 voi Trang, hang 1 voi Den).",
            "cach_thuc_hien": "Ngay lap tuc doi quan Tot do thanh mot quan Hau, Xe, Tuong hoac Ma tuy chon (thuong chon Hau).",
            "muc_dich": "Tao buoc ngoat lon trong tran dau, bien quan co yeu nhat thanh quan co manh nhat."
        },
        {
            "ten": "Chieu het va Co hoa (Checkmate & Stalemate)",
            "dieu_kien": "Chieu het xay ra khi Vua bi tan cong va khong con nuoc di nao hop le de thoat khoi the chieu. Co hoa xay ra khi den luot di nhung khong bi chieu va khong con nuoc di hop le nao.",
            "cach_thuc_hien": "Phan biet ro giua Chieu het (chien thang) va Het nuoc di - The hoa Pat (chia diem 0.5 - 0.5).",
            "muc_dich": "Giup hoc sinh tinh toan can than luc dang dan truoc, tranh de bi roi vao the co hoa dang tiec."
        }
    ]

def lay_khai_cuoc_kinh_dien_co_vua():
    """Tra ve cac he thong khai cuoc co dien va loi the chien thuat."""
    return [
        {
            "ten": "Khai cuoc Y (Italian Game)",
            "nuoc_di": "1. e4 e5 2. Nf3 Nc6 3. Bc4",
            "y_nghia": "Nhanh chong phat trien Ma va Tuong, kiem soat o trung tam d4 va gay ap luc truc tiep len diem yeu f7 cua quan Den.",
            "danh_cho": "Rat thich hop cho hoc sinh moi bat dau hoc co vi tinh truc dien va de nhap thanh som."
        },
        {
            "ten": "Phong thu Sicilia (Sicilian Defense)",
            "nuoc_di": "1. e4 c5",
            "y_nghia": "Quan Den phan cong bat doi xung ngay tu nuoc dau tien, tao the tran phuc tap o canh hau va danh tranh the chu dong cua Trang.",
            "danh_cho": "Danh cho ky thu thich phong cach tan cong sac ben va quyet liet."
        },
        {
            "ten": "Gambit Hau (Queen's Gambit)",
            "nuoc_di": "1. d4 d5 2. c4",
            "y_nghia": "Trang chu dong thi sinh quan Tot c4 de keo Tot doi phuong ra khoi trung tam, qua do gianh toan quyen kiem soat cac o trung tam then chot.",
            "danh_cho": "He thong khai cuoc chien luoc vung chac duoc rat nhieu Dai kien tuong the gioi su dung."
        },
        {
            "ten": "Khai cuoc Tay Ban Nha (Ruy Lopez)",
            "nuoc_di": "1. e4 e5 2. Nf3 Nc6 3. Bb5",
            "y_nghia": "Dua Tuong len b5 tan cong quan Ma dang bao ve o trung tam e5 cua Den, dat nen mong cho the tran kiem soat lau dai.",
            "danh_cho": "Mot trong nhung khai cuoc co dien va phong phu nhat trong lich su co vua quoc te."
        }
    ]

def lay_don_chien_thuat_co_vua():
    """Tra ve cac don chien thuat can ban giup hoc sinh rinh bat quan doi thu."""
    return [
        {
            "ten": "Don chia doi (Fork)",
            "mo_ta": "Mot quan co (dac biet la Ma hoac Tot) tan cong cung mot luc hai hoac nhieu quan cua doi phuong. Doi thu chi co the cuu 1 quan va phai bo quan con lai.",
            "vi_du": "Quan Ma nhay vao o c7 chieu Vua dong thoi tan cong quan Xe o a8."
        },
        {
            "ten": "Don ghim quan (Pin)",
            "mo_ta": "Tan cong mot quan co ma phia sau no la mot quan co gia tri cao hon (nhu Vua hoac Hau). Quan bi ghim khong the hoac khong nen di chuyen.",
            "vi_du": "Tuong dung tren duong cheo chieu quan Ma, phia sau quan Ma la Vua, quan Ma hoan toan bi te liet."
        },
        {
            "ten": "Don xien (Skewer)",
            "mo_ta": "Nguoc lai voi don ghim: quan co gia tri cao hon dung o phia truoc va bi tan cong truc dien, khi no phai bo chay se de lo quan gia tri phia sau bi bat.",
            "vi_du": "Xe chieu Vua tren hang ngang, Vua phai chay va Xe an tiep quan Hau dung phia sau."
        },
        {
            "ten": "Don chieu mo (Discovered Attack)",
            "mo_ta": "Khi ban di chuyen mot quan co cua minh, hanh dong do mo ra duong tan cong cho mot quan co khac phia sau len doi phuong.",
            "vi_du": "Ma nhay di mo duong cho Tuong chieu Vua doi thu, tao nen the tan cong kep vo cung nguy hiem."
        }
    ]

def lay_danh_nhan_co_vua():
    """Tra ve danh sach cac Dai kien tuong tieu bieu the gioi va Viet Nam."""
    return [
        {
            "ten": "Le Quang Liem",
            "quoc_tich": "Viet Nam",
            "danh_hieu": "Sieu Dai kien tuong quoc te (Super GM)",
            "thanh_tich": "Vo dich Co chop the gioi nam 2013, Elo cao nhat vuot moc 2740, HLV truong doi tuyen co vua DH Webster (My).",
            "loi_khuyen": "Moi nuoc co giong nhu mot quyet dinh trong cuoc song. Tinh toan can than va khong so sai lam la chia khoa tien bo."
        },
        {
            "ten": "Magnus Carlsen",
            "quoc_tich": "Na Uy",
            "danh_hieu": "Ky thu vi dai thoi hien dai (World Champion 2013 - 2023)",
            "thanh_tich": "Diem Elo ky luc lich su 2882, vo dich the gioi tat ca the thuc: Co tieu chuan, Co nhanh, Co chop.",
            "loi_khuyen": "Dung cho doi may man tren ban co, hay tao ra suc ep lien tuc cho den khi doi thu boc lo so ho."
        },
        {
            "ten": "Garry Kasparov",
            "quoc_tich": "Nga",
            "danh_hieu": "Vua co huyen thoai the ky 20",
            "thanh_tich": "Giu ngoi vo dich the gioi 15 nam lien tiep (1985 - 2000), tham gia tran dau the ky voi sieu may tinh Deep Blue.",
            "loi_khuyen": "Co vua la nghe thuat cua su phan tich. Khi hieu ro vi sao minh di mot nuoc co, ban da vuot len doi thu."
        }
    ]

def lay_kho_cau_do_co_vua():
    """Tra ve danh sach cac cau hoi the co va cau do chien thuat cho hoc sinh THCS."""
    return [
        {
            "id": "cv_1",
            "the_co": "Trang co Vua o g1, Xe o e1, Hau o d1. Den co Vua o e8 dang o giua ban co, chua nhap thanh va bi Xe kiem soat cot e.",
            "cau_hoi": "Trong co vua, quan co nao la quan duy nhat co the nhay qua dau cac quan co khac tren ban co?",
            "cac_lua_chon": [
                "A. Quan Tuong",
                "B. Quan Ma",
                "C. Quan Xe",
                "D. Quan Hau"
            ],
            "dap_an_dung": "B",
            "giai_thich": "Quan Ma co cach di hinh chu L va la quan co duy nhat tren ban co duoc phep nhay qua dau bat ky quan nao (ca quan minh va quan doi phuong)."
        },
        {
            "id": "cv_2",
            "the_co": "Den vua di quan Tot tu d7 len d5 (di 2 o). Trang dang co quan Tot dung o o e5 ngay ben canh.",
            "cau_hoi": "Trang co the su dung luat dac biet nao ngay lap tuc de bat quan Tot d5 cua Den?",
            "cac_lua_chon": [
                "A. Luat Phong cap",
                "B. Luat Nhap thanh xa",
                "C. Luat Bat tot qua duong (En Passant)",
                "D. Luat Chieu het nhanh"
            ],
            "dap_an_dung": "C",
            "giai_thich": "Luat Bat tot qua duong (En Passant) cho phep Tot Trang o hang 5 an Tot Den vua di 2 o ben canh bang cach di cheo xuong o d6 nhu the Tot Den chi di 1 o."
        },
        {
            "id": "cv_3",
            "the_co": "Quan Ma Trang nhay vao o e7 chieu Vua Den o g8, dong thoi tan cong quan Hau Den dang dung o c8.",
            "cau_hoi": "Don chien thuat ma quan Ma Trang vua thuc hien duoc goi la don gi?",
            "cac_lua_chon": [
                "A. Don chia doi (Fork)",
                "B. Don ghim quan (Pin)",
                "C. Don xien (Skewer)",
                "D. Don chieu mo (Discovered Check)"
            ],
            "dap_an_dung": "A",
            "giai_thich": "Don chia doi la khi mot quan co (dac biet la Ma) tan cong dong thoi hai muc tieu gia tri cao cua doi phuong khien doi thu khong the cuu het ca hai quan."
        },
        {
            "id": "cv_4",
            "the_co": "Hoc sinh so sanh gia tri quan co: 1 quan Xe va 1 quan Ma voi 1 quan Hau doi phuong.",
            "cau_hoi": "Theo quy uoc diem gia tri chuan trong co vua, tong diem cua 1 Xe (5 diem) va 1 Ma (3 diem) so voi 1 Hau (9 diem) la bao nhieu?",
            "cac_lua_chon": [
                "A. 8 diem so voi 9 diem (Kem hon 1 diem)",
                "B. 10 diem so voi 9 diem (Hon 1 diem)",
                "C. 7 diem so voi 9 diem (Kem hon 2 diem)",
                "D. Bang nhau 9 diem"
            ],
            "dap_an_dung": "A",
            "giai_thich": "1 Xe (5 diem) + 1 Ma (3 diem) = 8 diem, thap hon 1 Hau (9 diem) 1 diem. Nho quy uoc nay ma hoc sinh tinh toan duoc nuoc doi quan co loi hay khong."
        },
        {
            "id": "cv_5",
            "the_co": "Vua Den khong bi chieu, nhung den luot Den di thi khong con bat ky nuoc di hop le nao tren toan ban co.",
            "cau_hoi": "Ket qua cua van co trong truong hop nay duoc trong tai tuyen bo nhu the nao?",
            "cac_lua_chon": [
                "A. Den bi xu thua vi het gio",
                "B. Trang thang cuoc nho chieu het",
                "C. Van co hoa (The hoa Pat / Stalemate)",
                "D. Phai xep lai ban co choi lai tu dau"
            ],
            "dap_an_dung": "C",
            "giai_thich": "Khi mot ben khong bi chieu nhung khong con nuoc di hop le nao thi van co ket thuc hoa ngay lap tuc theo luat Co hoa Pat (Stalemate)."
        }
    ]
