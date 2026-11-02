# Thu muc: xu_ly_co_tri_tue
# File: quan_ly_co_tuong.py
# Mo ta: Quan ly kien thuc co tuong, luat choi, 7 khai cuoc, 8 sat phap, 4 danh thu va 12 cau do THCS

def lay_danh_sach_quan_co_tuong():
    """
    Tra ve danh sach 7 loai quan co tuong, quy tac di chuyen va dac diem rieng biet.
    Giai thich ngan gon, de hieu phu hop cho hoc sinh THCS.
    """
    return [
        {
            "id": "tuong_soai",
            "ten": "Tuong / Soai (General)",
            "ky_hieu": "TG",
            "vi_tri": "O giua hang day, ben trong Cuu Cung.",
            "cach_di": "Di tung o mot theo chieu ngang hoac doc. Tuyet doi khong duoc ra khoi pham vi Cuu Cung 3x3.",
            "luat_dac_biet": "Luat mat Tuong: Hai Tuong khong bao gio duoc nhin thay nhau tren cung mot duong doc ma khong co quan nao o giua chan mat."
        },
        {
            "id": "si",
            "ten": "Si (Advisor)",
            "ky_hieu": "SI",
            "vi_tri": "Hai ben canh Tuong trong Cuu Cung.",
            "cach_di": "Di cheo 1 o moi nuoc, chi hoat dong ben trong Cuu Cung de bao ve Tuong.",
            "luat_dac_biet": "Khong duoc ra khoi Cuu Cung, mat Si khien Tuong rat de bi Phao va Xe doi phuong tan cong truc dien."
        },
        {
            "id": "tuong_voi",
            "ten": "Tuong / Voi (Elephant)",
            "ky_hieu": "TU",
            "vi_tri": "Hai ben Si o hang day.",
            "cach_di": "Di cheo 2 o (tao thanh hinh vuong 2x2).",
            "luat_dac_biet": "Khong duoc sang song (chi phong thu o san nha). Neu co quan co dung o giua duong cheo thi bi Can mat Tuong, khong the di qua."
        },
        {
            "id": "xe",
            "ten": "Xe (Chariot / Rook)",
            "ky_hieu": "XE",
            "vi_tri": "Hai goc cua ban co.",
            "cach_di": "Di ngang hoac doc khong gioi han so o neu khong bi chan. An quan tren duong di cua minh.",
            "luat_dac_biet": "La quan co manh nhat ban co tuong, suc co dong cao nhat, chiem cac lo thong thoang de ap dao doi thu."
        },
        {
            "id": "phao",
            "ten": "Phao (Cannon)",
            "ky_hieu": "PH",
            "vi_tri": "O hang 3, cach mep ban co 2 o.",
            "cach_di": "Di ngang hoac doc giong nhu Xe khi khong an quan.",
            "luat_dac_biet": "Khi an quan, Phao bat buoc phai nhay qua dung 1 quan co khac lam Ngoi (quan ngoi co the cua ta hoac cua doi thu)."
        },
        {
            "id": "ma",
            "ten": "Ma (Horse / Knight)",
            "ky_hieu": "MA",
            "vi_tri": "Dung giua Xe va Tuong o hang day.",
            "cach_di": "Di theo hinh chu nhat (1 o doc va 1 o cheo, hoac 1 o ngang va 1 o cheo).",
            "luat_dac_biet": "Bi Can chan Ma: neu co quan co dung ngay o lien ke theo huong doc hoac ngang thi Ma khong the nhay qua huong do."
        },
        {
            "id": "tot_binh",
            "ten": "Tot / Binh (Soldier / Pawn)",
            "ky_hieu": "TO",
            "vi_tri": "5 quan dan hang ngang o hang 4.",
            "cach_di": "Chua qua song: chi duoc tien thang 1 o moi nuoc. Da qua song: duoc phep di thang hoac di ngang 1 o.",
            "luat_dac_biet": "Tuyet doi khong bao gio duoc di lui. Khi sang song, Tot tro nen vo cung loi hai vi co the tan cong theo 3 huong."
        }
    ]

def lay_dac_diem_ban_co_tuong():
    """Tra ve cau truc dac biet cua ban co tuong phuong Dong."""
    return [
        {
            "ten": "So Ha Han Gioi (Dong song)",
            "vi_tri": "Nam o giua ban co, chia doi 2 ben chien tuyen.",
            "y_nghia": "La ranh gioi quy dinh quan Tuong khong duoc vuot qua, va la moc danh dau quan Tot bat dau duoc di ngang sau khi qua song."
        },
        {
            "ten": "Cuu Cung (Cung Tuong)",
            "vi_tri": "Khu vuc hinh vuong 3x3 o moi dau san, co 2 duong cheo noi cac goc tao thanh hinh chu X.",
            "y_nghia": "La noi Tuong va Si phai o lai suot van dau de chi huy va bao ve bo chi huy, khong duoc phep roi khoi cung."
        },
        {
            "ten": "Giao diem va Lo co (90 Diem)",
            "vi_tri": "Ban co gom 9 duong doc (lo tu 1 den 9) va 10 duong ngang tao thanh 90 giao diem.",
            "y_nghia": "Khac voi co vua dat quan trong o vuong, quan co tuong duoc dat ngay tai cac diem giao nhau cua cac duong ke."
        }
    ]

def lay_the_tran_khai_cuoc_co_tuong():
    """Tra ve 7 the tran khai cuoc noi tieng trong co tuong."""
    return [
        {
            "ten": "Duong Dau Phao (Phao dau)",
            "nuoc_di": "Phao 2 binh 5 hoac Phao 8 binh 5 vao trung lo.",
            "y_nghia": "Tan cong truc dien vao Tot dau va uy hiep thang vao trung tam cua doi phuong. Loi choi cong pha manh me.",
            "phu_hop": "Nguoi choi thich the chu dong, muon tao ap luc ngay tu nhung nuoc co dau tien."
        },
        {
            "ten": "Binh Phong Ma",
            "nuoc_di": "Hai Ma cung nhay len giu Tot dau o lo 3 va lo 7.",
            "y_nghia": "Hang phong ngu vung chac nhu buc tuong binh phong, phan cong sac sao o hai bien.",
            "phu_hop": "The tran doi pho hieu qua nhat voi Duong Dau Phao, yeu cau tinh kien tri va phong ngu chat che."
        },
        {
            "ten": "Khoi Ma Cuoc",
            "nuoc_di": "Nuoc dau tien nhay Ma len lo 3 hoac lo 7 truoc.",
            "y_nghia": "Loi danh uyen chuyen, kin dao, tranh doi dau truc dien qua som va giu nhieu phuong an bien hoa.",
            "phu_hop": "Nhung ky thu thich loi danh chien luoc lau dai va thu thach ban linh cua doi phuong."
        },
        {
            "ten": "Nghich Thu Phao (Nghich Phao)",
            "nuoc_di": "Ben di sau cung dua Phao vao trung lo nhung o huong nguoc lai voi Phao dau cua ben di truoc.",
            "y_nghia": "The tran doi cong sinh tu nhat trong co tuong, hai ben deu tan cong trung tam quyet liet.",
            "phu_hop": "Ky thu muon danh nhanh thang nhanh, khong ngai va cham va chap nhan rui ro cao."
        },
        {
            "ten": "Tien Nhan Chi Lo (Tan Binh 7)",
            "nuoc_di": "Nuoc dau tien day Tot 7 tien 1 (Binh 7 tan 1) de mo duong cho Ma va do tham y do cua doi thu.",
            "y_nghia": "Nuoc co tham do chien luoc, nhu tien nhan chi loi, linh hoat chuyen sang Phao dau hoac Binh phong ma.",
            "phu_hop": "Cac ky thu co loi danh tham tram, thau hieu tam ly doi phuong."
        },
        {
            "ten": "Si Giac Phao (Phao goc Si)",
            "nuoc_di": "Dua Phao len o goc Si (Phao 2 tan 4 hoac Phao 8 tan 4) phong thu kin ke.",
            "y_nghia": "Vua co the phong ngu hanh lang can yeu vua san sang ho tro Xe Ma xuat tran.",
            "phu_hop": "Loi choi can trong, an toan, lay thu lam cong."
        },
        {
            "ten": "Qua Cung Phao",
            "nuoc_di": "Dua Phao tu ben nay sang ben kia Cuu Cung (Phao 2 binh 6 hoac Phao 8 binh 4).",
            "y_nghia": "Tap trung hoa luc ve mot canh de tao the ap dao cuc bo, buoc doi phuong phai chong do vat va.",
            "phu_hop": "Ky thu thich khoet vao canh yeu cua doi phuong."
        }
    ]

def lay_sat_phap_kinh_dien_co_tuong():
    """Tra ve 8 sat phap kinh dien danh bai doi thu trong co tuong."""
    return [
        {
            "ten": "Ma Hau Phao (Ma truoc Phao sau)",
            "mo_ta": "Quan Ma nhay vao khong che cac cua thoat cua Tuong, dong thoi lam Ngoi cho quan Phao phia sau chieu truc dien vao Tuong.",
            "ung_dung": "La mot trong nhung sat phap co dien va pho bien nhat, doi phuong rat kho phong thu vi bi kep giua hai quan."
        },
        {
            "ten": "Song Xe Toa Thanh (Song Xe sat)",
            "mo_ta": "Hai quan Xe cung tien vao cung doi phuong, mot Xe chieu tuong buoc Tuong phai chay len hoac xuong, Xe thu hai ap sat chieu het.",
            "ung_dung": "Uy luc cua hai Xe khi phoi hop la cuc ky khung khiep, thuong ket lieu van co trong nhay mat khi hang Si bi be gay."
        },
        {
            "ten": "Diep Phao (Phao trung)",
            "mo_ta": "Hai quan Phao dung tren cung mot duong doc hoac ngang, quan Phao truoc lam ngoi cho quan Phao sau chieu Tuong.",
            "ung_dung": "Doi thu khong the dung quan co khac de che chan boi vi Phao sau van tiep tuc co ngoi de chieu."
        },
        {
            "ten": "Dai Dao Tieu Doi (Xe chem Si)",
            "mo_ta": "Xe dung suc manh tan cong chem nat quan Si phong ngu cua doi phuong, mo toang cua vao Cuu Cung de cac quan khac tran vao.",
            "ung_dung": "The hien tu duy dam quyet doan: danh doi mot quan Xe lay su sup do toan dien cua hang phong thu doi thu."
        },
        {
            "ten": "Bat Son Cai The (Doi non lap be)",
            "mo_ta": "Phoi hop giua Xe va Tot da qua song ap sat hang day, don ep Tuong doi phuong vao goc cung khong loi thoat.",
            "ung_dung": "Nuoc di the hien suc manh phi thuong cua quan Tot sau khi da qua song."
        },
        {
            "ten": "Trac Dien Ho (Ho vo nghieng)",
            "mo_ta": "Quan Ma o vi tri toa do ngach ngoai Cuu Cung chieu Tuong, duoc Xe hoac Phao yem tro khong cho Tuong quay dau.",
            "ung_dung": "Don sat phap cuc hiem vi danh vao suon nghieng cua bo chi huy doi phuong."
        },
        {
            "ten": "Thiet Mon Thuyen (Khoa cua sat)",
            "mo_ta": "Dung Xe hoac Tot chiem giu lo cot trung tam, sau do dua Xe hoac Phao con lai xuong hang day chieu dut diem.",
            "ung_dung": "Tuong bi khoa chat cua thoat nhu bi nhot trong then cua sat, khong the giay giua."
        },
        {
            "ten": "Kham Dau Phao (Phao giang dau)",
            "mo_ta": "Phao danh thang vao trung tam Tot dau khi Si doi phuong chua giuong, ghim chat khien hai Si khong the di chuyen.",
            "ung_dung": "Thuong xuat hien trong cac the tran Phao dau cong pha nhanh o trung cuoc."
        }
    ]

def lay_danh_thu_co_tuong():
    """Tra ve thong tin 4 ky vuong, danh thu co tuong tieu bieu."""
    return [
        {
            "ten": "Lai Ly Huynh",
            "quoc_tich": "Viet Nam",
            "danh_hieu": "Ky vuong so 1 Viet Nam, Vo dich the gioi Co nhanh 2022",
            "thanh_tich": "Nhieu lan vo dich quoc gia, thi dau thanh cong ruc ro tai giai vo dich dong doi Trung Quoc (Giap Cap Lien Trieu).",
            "loi_khuyen": "Luyen co giong nhu ren luyen y chi. Phai biet chap nhan that bai de rut ra bai hoc quy gia cho tran sau."
        },
        {
            "ten": "Ho Vinh Hoa",
            "quoc_tich": "Trung Quoc",
            "danh_hieu": "Thap lien ba (10 lan vo dich lien tiep)",
            "thanh_tich": "Len ngoi vo dich toan Trung Quoc khi moi 15 tuoi, sang tao ra nhieu the tran khai cuoc con ton tai den ngay nay.",
            "loi_khuyen": "Dung go bo minh vao nhung khuon mau co san, the co luon bien doi va nguoi sang tao moi la nguoi chien thang."
        },
        {
            "ten": "Vuong Thien Nhat",
            "quoc_tich": "Trung Quoc",
            "danh_hieu": "Ngoai tinh lai khach (Ky thu so 1 the gioi hien dai)",
            "thanh_tich": "Dung dau bang he so diem Elo co tuong the gioi hon 10 nam lien tiep nho loi danh tinh toan nhu may tinh.",
            "loi_khuyen": "Moi nuoc co deu phai dua tren su tinh toan sau sac va do chinh xac tuyet doi."
        },
        {
            "ten": "Nguyen Thanh Bao",
            "quoc_tich": "Viet Nam",
            "danh_hieu": "Tay Doc - Ky thu tai hoa",
            "thanh_tich": "Huy chuong Bac the gioi, tung danh bai nhieu kien tuong hang dau Trung Quoc voi loi choi tan cong ruc lua.",
            "loi_khuyen": "Dung bao gio ngai mao hiem khi ban nhin thay co hoi tan cong sang tao tren ban co."
        }
    ]

def lay_kho_cau_do_co_tuong():
    """Tra ve danh sach 12 cau hoi the co va cau do chien thuat co tuong cho hoc sinh THCS."""
    return [
        {
            "id": "ct_1",
            "the_co": "Hai ben dang giao tranh o trung lo. Tuong Do va Tuong Den cung nam tren duong doc lo 5 ma o giua khong co quan co nao.",
            "cau_hoi": "Theo luat co tuong, tinh huong hai Tuong doi dien nhau truc tiep tren cung mot lo doc ma khong co quan chan duoc goi la gi va bi xu ly the nao?",
            "cac_lua_chon": [
                "A. Luat mat Tuong - Nuoc di lam lo mat Tuong la pham luat",
                "B. Duoc phep va hai ben bat tay hoa co",
                "C. Ben nao di sau se bi chieu het ngay",
                "D. Ca hai Tuong deu bi loai khoi ban co"
            ],
            "dap_an_dung": "A",
            "giai_thich": "Luat mat Tuong quy dinh hai Tuong khong bao gio duoc doi mat truc tiep tren cung mot cot doc ma khong co quan can. Nuoc di de lo mat Tuong la nuoc di pham quy."
        },
        {
            "id": "ct_2",
            "the_co": "Quan Phao Do muon an quan Xe Den dang dung o phia xa tren cung mot duong ngang.",
            "cau_hoi": "Dieu kien bat buoc de quan Phao co the an quan doi phuong trong co tuong la gi?",
            "cac_lua_chon": [
                "A. Phai co dung mot quan co bat ky o giua lam Ngoi",
                "B. Phai dung sat ngay ben canh quan Xe",
                "C. Phai co hai quan co o giua moi an duoc",
                "D. Khong can quan nao o giua, an giong nhu quan Xe"
            ],
            "dap_an_dung": "A",
            "giai_thich": "Trong co tuong, quan Phao khi di chuyen khong can ngoi, nhung khi an quan doi phuong thi bat buoc phai co dung 1 quan co o giua lam Ngoi nhay qua."
        },
        {
            "id": "ct_3",
            "the_co": "Quan Ma Do dinh nhay vao de chieu Tuong Den, nhung ngay o lien ke truoc mat Ma co mot quan Tot dung chan.",
            "cau_hoi": "Hien tuong nay trong co tuong duoc goi la gi va quan Ma co nhay duoc khong?",
            "cac_lua_chon": [
                "A. Can chan Ma - Ma khong duoc phep nhay theo huong do",
                "B. Ma duoc phep nhay qua dau quan Tot",
                "C. Can mat Tuong - Ma van di binh thuong",
                "D. Ma phai an quan Tot do truoc moi duoc di"
            ],
            "dap_an_dung": "A",
            "giai_thich": "Co tuong co quy tac Can chan Ma: neu co quan co dung o o lien ke theo huong Ma dinh buoc thi Ma bi can chan va khong the nhay theo huong do."
        },
        {
            "id": "ct_4",
            "the_co": "Quan Tot Do da tien qua song va ap sat Cuu Cung doi phuong.",
            "cau_hoi": "Sau khi qua song, quy tac di chuyen cua quan Tot trong co tuong co su thay doi quan trong nao?",
            "cac_lua_chon": [
                "A. Duoc phep di ngang 1 o va tien 1 o (khong duoc di lui)",
                "B. Duoc phep di lui ve phong thu cho Tuong nha",
                "C. Duoc phong cap ngay thanh quan Xe hoac Phao",
                "D. Duoc di cheo giong nhu quan Si"
            ],
            "dap_an_dung": "A",
            "giai_thich": "Khi da qua song, quan Tot tro nen loi hai hon vi duoc phep di ngang sang trai hoac phai 1 o, va tien 1 o. Tot khong bao gio duoc di lui."
        },
        {
            "id": "ct_5",
            "the_co": "Phao Do dung sau quan Ma Do tren cung mot duong thang, Ma Do nhay chieu Tuong dong thoi lam ngoi cho Phao chieu buoc Tuong Den het duong chay.",
            "cau_hoi": "Don sat phap kinh dien pho bien nay trong co tuong duoc goi la gi?",
            "cac_lua_chon": [
                "A. Sat phap Ma Hau Phao",
                "B. Sat phap Song Xe Toa Thanh",
                "C. Sat phap Dai Dao Tieu Doi",
                "D. Sat phap Tam Cuu Lien Hoan"
            ],
            "dap_an_dung": "A",
            "giai_thich": "Sat phap Ma Hau Phao la don phoi hop noi tieng: Ma khoa goc cua Tuong va lam ngoi cho Phao phia sau chieu dut diem."
        },
        {
            "id": "ct_6",
            "the_co": "Quan Tuong (Voi) Do muon bay qua dong song de tan cong Tuong doi phuong.",
            "cau_hoi": "Theo luat co tuong, quan Tuong (Voi) co duoc phep di qua song (So Ha Han Gioi) khong?",
            "cac_lua_chon": [
                "A. Khong bao gio duoc phep qua song, chi hoat dong ben san nha de phong thu",
                "B. Duoc phep qua song khi doi phuong chi con 1 quan",
                "C. Duoc qua song neu di cheo 4 o",
                "D. Duoc qua song neu co quan Ma bao ke"
            ],
            "dap_an_dung": "A",
            "giai_thich": "Trong co tuong, quan Tuong (Voi) la quan thuan tuy phong thu noi dia, tuyet doi khong duoc phep qua song."
        },
        {
            "id": "ct_7",
            "the_co": "Hai Xe Do chim xuong hang day va hang ap day cua Cuu Cung doi phuong, lien tuc chieu ep Tuong Den.",
            "cau_hoi": "Don sat phap day uy luc nay cua hai quan Xe trong co tuong duoc goi la gi?",
            "cac_lua_chon": [
                "A. Song Xe Toa Thanh",
                "B. Ma Hau Phao",
                "C. Trac Dien Ho",
                "D. Binh Phong Ma"
            ],
            "dap_an_dung": "A",
            "giai_thich": "Song Xe Toa Thanh la the tran hai Xe ap sat Cuu Cung, mot Xe khoa chan, mot Xe dut diem ket lieu van dau."
        },
        {
            "id": "ct_8",
            "the_co": "Quan Xe Do muon chem phang quan Si Den dang phong thu trong Cuu Cung de mo toang loi vao cho Phao va Ma.",
            "cau_hoi": "Don chien thuat dung Xe chem Si pha vo hoan toan he thong phong thu Cuu Cung mang ten la gi?",
            "cac_lua_chon": [
                "A. Dai Dao Tieu Doi (Xe chem Si)",
                "B. Diep Phao",
                "C. Khoi Ma Cuoc",
                "D. Thiet Mon Thuyen"
            ],
            "dap_an_dung": "A",
            "giai_thich": "Dai Dao Tieu Doi la don sat phap quyet doan dung Xe chem thang vao Si mo toang phong tuyen de ket thuc tran dau."
        },
        {
            "id": "ct_9",
            "the_co": "Xe Do chiem giu lo 5 (trung lo) khoa chat mat Tuong Den, Xe thu hai Do lao xuong hang 10 chieu Tuong.",
            "cau_hoi": "Don sat phap khoa chat cua thoat cua Tuong giong nhu khoa then cua sat duoc goi la gi?",
            "cac_lua_chon": [
                "A. Thiet Mon Thuyen (Khoa cua sat)",
                "B. Bat Son Cai The",
                "C. Duong Dau Phao",
                "D. Kham Dau Phao"
            ],
            "dap_an_dung": "A",
            "giai_thich": "Thiet Mon Thuyen dung mot quan khong che lo trung tam khong cho Tuong chay qua, quan kia giang xuong hang day chieu het."
        },
        {
            "id": "ct_10",
            "the_co": "Quan Si trong co tuong chi co the di chuyen theo cach nao sau day?",
            "cau_hoi": "Quy tac di chuyen va pham vi hoat dong chuan cua quan Si la gi?",
            "cac_lua_chon": [
                "A. Di cheo 1 o moi nuoc va chi hoat dong ben trong Cuu Cung 3x3",
                "B. Di thang 1 o moi nuoc giong quan Tot",
                "C. Di ngang doc khong gioi han o ben trong san nha",
                "D. Duoc phep nhay qua dau Tuong"
            ],
            "dap_an_dung": "A",
            "giai_thich": "Si chi duoc phep di cheo 1 o tai cac duong cheo cua Cuu Cung, khong the buoc ra khoi pham vi 3x3 nay."
        },
        {
            "id": "ct_11",
            "the_co": "Nguoi choi di nuoc dau tien la Binh 7 tan 1 (day Tot 7 tien 1 o) de tham do phan ung doi thu.",
            "cau_hoi": "The tran khai cuoc tham do chien luoc linh hoat nay trong co tuong mang ten goi gi?",
            "cac_lua_chon": [
                "A. Tien Nhan Chi Lo",
                "B. Duong Dau Phao",
                "C. Nghich Thu Phao",
                "D. Si Giac Phao"
            ],
            "dap_an_dung": "A",
            "giai_thich": "Tien Nhan Chi Lo (Nguoi dan duong) la nuoc co Binh 7 tan 1 mo duong cho Ma va linh hoat bien hoa theo nuoc di cua doi thu."
        },
        {
            "id": "ct_12",
            "the_co": "Khi quan Tuong (Voi) muon di cheo 2 o, neu tai o giua duong cheo co mot quan co dung chan thi se xay ra dieu gi?",
            "cau_hoi": "Hien tuong nay trong co tuong goi la gi va Tuong co di chuyen duoc khong?",
            "cac_lua_chon": [
                "A. Bi Can mat Tuong - Tuong khong the di qua huong do",
                "B. Tuong duoc phep nhay qua dau quan co do",
                "C. Tuong an luon quan co o giua",
                "D. Tuong bien thanh quan Xe"
            ],
            "dap_an_dung": "A",
            "giai_thich": "Can mat Tuong (Can mat Voi) xay ra khi tam hinh vuong 2x2 co quan co chan, khien Tuong khong the di cheo qua huong do."
        }
    ]
