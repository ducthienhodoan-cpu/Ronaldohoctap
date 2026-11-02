# Thu muc: xu_ly_co_tri_tue
# File: quan_ly_co_vua.py
# Mo ta: Quan ly tri thuc co vua, luat choi, 8 khai cuoc, 8 don chien thuat, danh nhan va 12 cau do THCS

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
            "cach_thuc_hien": "Ban co quyen an Tot do bang cach di cheo ra phia sau quan Tot do giong nhu no chi di 1 o. Chi duoc thuc hien ngay o nuoc di lien sau.",
            "muc_dich": "Ngan chan viec Tot di 2 o de vuot qua vung kiem soat cua Tot doi phuong mot cach de dang."
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
    """Tra ve 8 he thong khai cuoc kinh dien co dien va hien dai."""
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
            "y_nghia": "Quan Den phan cong bat doi xung ngay tu nuoc dau tien, tao the tran phuc tap o canh hau va tranh the chu dong cua Trang.",
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
        },
        {
            "ten": "Phong thu Phap (French Defense)",
            "nuoc_di": "1. e4 e6 2. d4 d5",
            "y_nghia": "Quan Den thiet lap chuoi tot vung chac e6-d5 tan cong ngay vao trung tam e4 cua Trang.",
            "danh_cho": "Ky thu thich loi choi phong ngu phan cong chac chan, cho doi doi thu ham ho dang cao de phan kich."
        },
        {
            "ten": "Phong thu Caro-Kann (Caro-Kann Defense)",
            "nuoc_di": "1. e4 c6 2. d4 d5",
            "y_nghia": "Den chuan bi day tot len d5 ma khong bi chan duong phat trien cua quan Tuong o c8 nhu trong phong thu Phap.",
            "danh_cho": "Loi choi cuc ky chac chan, kien co, rat kho bi danh bai."
        },
        {
            "ten": "Phong thu An Do cua Vua (King's Indian Defense)",
            "nuoc_di": "1. d4 Nf6 2. c4 g6 3. Nc3 Bg7",
            "y_nghia": "Den nhuong trung tam cho Trang dang tot len, sau do phat trien Tuong canh vua (fianchetto) va phan cong bao luc vao canh Vua cua Trang.",
            "danh_cho": "Duoc hai nha vo dich the gioi Garry Kasparov va Bobby Fischer cuc ky yeu thich."
        },
        {
            "ten": "He thong London (London System)",
            "nuoc_di": "1. d4 d5 2. Bf4",
            "y_nghia": "Trang phat trien Tuong den f4 som truoc khi khoa chuoi tot bang e3, tao the tran linh hoat va an toan cao.",
            "danh_cho": "Hoc sinh THCS rat de ghi nho vi cau truc quan co dinh va it rui ro bi bat ngo."
        }
    ]

def lay_don_chien_thuat_co_vua():
    """Tra ve 8 don chien thuat can ban va nang cao giup hoc sinh rinh bat quan doi thu."""
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
        },
        {
            "ten": "Don chieu nghet (Smothered Mate)",
            "mo_ta": "Quan Ma chieu Vua doi phuong khi Vua bi chinh cac quan dong doi cua minh vay kin xung quanh khong con o thoat.",
            "vi_du": "Hau thi sinh chieu buoc Xe doi phuong phai an chan cua thoat cua Vua, Ma nhay den f7 hoac h6 ket lieu van dau."
        },
        {
            "ten": "Don du do va Danh lac huong (Decoy & Deflection)",
            "mo_ta": "Thi quan de buoc quan chu luc cua doi phuong phai roi khoi vi tri phong thu then chot.",
            "vi_du": "Chieu thi Xe de keo Vua ra khoi goc bao ve quan Hau, sau do an Hau doi phuong."
        },
        {
            "ten": "Don coi xay gio (Windmill)",
            "mo_ta": "Su phoi hop lien hoan giua Xe va Tuong thuc hien cac don chieu mo lien tuc de an sach cac quan cua doi thu.",
            "vi_du": "Xe vua an quan vua chieu mo bang Tuong, Vua doi phuong phai chay qua chay lai trong bat luc."
        },
        {
            "ten": "Don chieu het hang day (Back-rank Mate)",
            "mo_ta": "Xe hoac Hau chieu het Vua doi phuong o hang ngang so 8 (hoac hang 1) vi Vua bi 3 quan Tot phia truoc chan duong chay.",
            "vi_du": "Xe lao xuong o e8 chieu het khi hang tot f7-g7-h7 chua di chuyen."
        }
    ]

def lay_danh_nhan_co_vua():
    """Tra ve danh sach 5 Dai kien tuong tieu bieu the gioi va Viet Nam."""
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
        },
        {
            "ten": "Bobby Fischer",
            "quoc_tich": "My",
            "danh_hieu": "Thien tai co vua the ky 20",
            "thanh_tich": "Vo dich the gioi nam 1972 sau tran dau lich su voi Boris Spassky tai Reykjavik, dat nen mong cho co vua the thao hien dai.",
            "loi_khuyen": "Toi khong tin vao tam ly hoc trong co vua, toi chi tin vao nhung nuoc di tot nhat."
        },
        {
            "ten": "Judit Polgar",
            "quoc_tich": "Hungary",
            "danh_hieu": "Nu ky thu vi dai nhat moi thoi dai",
            "thanh_tich": "Nu ky thu duy nhat tung lot vao Top 10 the gioi giua cac ky thu nam, tung danh bai Garry Kasparov va Magnus Carlsen.",
            "loi_khuyen": "Khong co gioi han nao cho tri tue phu nu. Su kien tri va quyet tam se vuot qua moi ranh gioi."
        }
    ]

def lay_kho_cau_do_co_vua():
    """Tra ve danh sach 12 cau hoi the co va cau do chien thuat cho hoc sinh THCS."""
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
        },
        {
            "id": "cv_6",
            "the_co": "Vua Den o g8 bi bao quanh boi Tot f7, Tot g7 va Xe h8. Ma Trang nhay vao f7 chieu Vua.",
            "cau_hoi": "Don chieu het khi Vua bi chinh cac quan cua minh vay chat khong the di chuyen duoc goi la gi?",
            "cac_lua_chon": [
                "A. Don chieu nghet (Smothered Mate)",
                "B. Don coi xay gio",
                "C. Don ghim quan tuyet doi",
                "D. Don du do Vua"
            ],
            "dap_an_dung": "A",
            "giai_thich": "Don chieu nghet la don dac trung cua quan Ma, khi Vua doi thu bi quan nha bao chat, khong con o nao de thao chay."
        },
        {
            "id": "cv_7",
            "the_co": "Trang di 1. e4 e5 2. Qh5 Nc6 3. Bc4 Nf6 4. Qxf7# chieu het trong 4 nuoc.",
            "cau_hoi": "The chieu het 4 nuoc danh vao o yeu f7 cua Den duoc goi la gi va Den nen phong thu nhu the nao?",
            "cac_lua_chon": [
                "A. The chieu het hoc gia (Scholar's Mate) - Den nen day Tot g6 hoac dua Ma len f6 som",
                "B. The chieu het Ngu ngo (Fool's Mate)",
                "C. The Gambit Vua",
                "D. The phong thu Sicilia"
            ],
            "dap_an_dung": "A",
            "giai_thich": "Chieu het hoc gia danh vao o f7 chi duoc Vua bao ve. Den chi can phat trien Ma len f6 chan Hau hoac day Tot g6 la phong thu de dang."
        },
        {
            "id": "cv_8",
            "the_co": "Tuong Trang dung o c4 chieu Ma Den o d5, phia sau Ma Den la quan Hau Den o e6.",
            "cau_hoi": "Don chien thuat ma quan Tuong Trang dang su dung len Ma Den duoc goi la don gi?",
            "cac_lua_chon": [
                "A. Don ghim tuong doi (Relative Pin)",
                "B. Don chieu het hang day",
                "C. Don chia doi ba quan",
                "D. Don thi quan bat buoc"
            ],
            "dap_an_dung": "A",
            "giai_thich": "Don ghim tuong doi la khi quan bi ghim (Ma) van co the di chuyen ve mat luat, nhung neu di chuyen thi quan Hau gia tri cao phia sau se bi an mat."
        },
        {
            "id": "cv_9",
            "the_co": "Vua Den dung o hang 8 voi 3 quan Tot o f7, g7, h7 chua di chuyen. Xe Trang lao xuong d8 chieu Vua.",
            "cau_hoi": "Vua Den khong the buoc len vi bi vuong 3 quan Tot va bi chieu het. Day la vi du dien hinh cua don gi?",
            "cac_lua_chon": [
                "A. Don chieu het hang day (Back-rank Mate)",
                "B. Don Phong cap bat ngo",
                "C. Don Bat tot qua duong",
                "D. Don xien quan doc"
            ],
            "dap_an_dung": "A",
            "giai_thich": "Don chieu het hang day xay ra khi Vua khong co o thoat (lo thoat khi) vi bi cac quan Tot cua minh chan phia truoc."
        },
        {
            "id": "cv_10",
            "the_co": "Trang muon phong cap quan Tot o hang 7. Khi Tot di xuong hang 8, luat cho phep phong thanh nhung quan nao?",
            "cau_hoi": "Theo luat co vua quoc te FIDE, Tot co the duoc doi thanh nhung quan nao sau day?",
            "cac_lua_chon": [
                "A. Hau, Xe, Tuong hoac Ma (Khong duoc phong thanh Vua hoac giu nguyen Tot)",
                "B. Chi duoc phep phong thanh Hau duy nhat",
                "C. Chi duoc phong thanh nhung quan da bi an mat",
                "D. Co the phong thanh mot quan Vua thu hai"
            ],
            "dap_an_dung": "A",
            "giai_thich": "Khi Tot xuong hang 8, nguoi choi co the chon bien thanh Hau, Xe, Tuong hoac Ma ngay lap tuc, bat ke tren ban co con nhung quan do hay khong."
        },
        {
            "id": "cv_11",
            "the_co": "Trong khai cuoc Gambit Hau (1. d4 d5 2. c4), muc dich chien thuat cua quan Trang khi day Tot c4 la gi?",
            "cau_hoi": "Tai sao Trang lai chu dong moi Den an Tot c4 o nuoc thu hai?",
            "cac_lua_chon": [
                "A. De doi Tot bien lay Tot trung tam cua Den va chiem linh cac o trung tam",
                "B. Do Trang bi di nham nuoc",
                "C. De phong thu an toan cho Vua",
                "D. De cho Vua Trang nhap thanh nhanh"
            ],
            "dap_an_dung": "A",
            "giai_thich": "Gambit Hau thi Tot canh de doi Tot trung tam d5 cua Den, giup Trang dua Tot e len e4 chiem toan bo trung tam ban co."
        },
        {
            "id": "cv_12",
            "the_co": "Xe Trang chieu Vua Den o cot e, Vua Den buoc phai thao chay de lo quan Hau Den dung phia sau bi Xe Trang an.",
            "cau_hoi": "Don chien thuat ma quan gia tri cao o phia truoc phai chay lam lo quan phia sau duoc goi la gi?",
            "cac_lua_chon": [
                "A. Don xien (Skewer)",
                "B. Don ghim quan (Pin)",
                "C. Don chia doi (Fork)",
                "D. Don chieu mo (Discovered Attack)"
            ],
            "dap_an_dung": "A",
            "giai_thich": "Don xien (Skewer) nguoc voi don ghim: quan gia tri cao hon (Vua) dung truoc bi chieu phai chay, khien quan gia tri phia sau (Hau) bi an."
        }
    ]
