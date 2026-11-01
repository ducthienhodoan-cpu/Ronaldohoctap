# Thu muc: xu_ly_co_tri_tue
# File: quan_ly_co_tuong.py
# Mo ta: Quan ly kien thuc co tuong, luat choi, 7 loai quan co, sat phap kinh dien va cau do THCS

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
            "vi_tri": "Nang o giua ban co, chia doi 2 ben chien tuyen.",
            "y_nghia": "La ranh gioi quy dinh quan Tuong khong duoc vuot qua, va la moc danh dau quan Tot bat dau duoc di ngang sau khi qua song."
        },
        {
            "ten": "Cuu Cung (Cung Tuong)",
            "vi_tri": "Khu vuc hinh vuong 3x3 o moi dau san, co 2 duong cheo noi cac goc.",
            "y_nghia": "La noi Tuong va Si phai o lai suot van dau de chi huy va bao ve bo chi huy, khong duoc phep roi khoi cung."
        },
        {
            "ten": "Giao diem va Lo co",
            "vi_tri": "Ban co gom 9 duong doc (lo) va 10 duong ngang tao thanh 90 giao diem.",
            "y_nghia": "Khac voi co vua dat quan trong o vuong, quan co tuong duoc dat ngay tai cac diem giao nhau cua cac duong ke."
        }
    ]

def lay_sat_phap_kinh_dien_co_tuong():
    """Tra ve cac don sat phap kinh dien danh bai doi thu trong co tuong."""
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
        }
    ]

def lay_the_tran_khai_cuoc_co_tuong():
    """Tra ve cac the tran khai cuoc noi tieng trong co tuong."""
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
        }
    ]

def lay_danh_thu_co_tuong():
    """Tra ve thong tin cac ky vuong, danh thu co tuong tieu bieu."""
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
        }
    ]

def lay_kho_cau_do_co_tuong():
    """Tra ve danh sach cac cau hoi the co va cau do chien thuat co tuong cho hoc sinh THCS."""
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
        }
    ]
