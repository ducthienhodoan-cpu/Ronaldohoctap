// Thu muc: public/xu_ly_co_tri_tue
// File: co_tri_tue.js
// Mo ta: Xu ly toan dien giao dien Web cho Co Vua va Co Tuong - Dau Tri Ky Thu voi 24 the co, ban co truc quan va he thong cup giai dau

(function () {
    "use strict";

    // Du lieu du phong day du 100% khi offline hoac ket noi kem
    const DU_LIEU_CO_VUA_FALLBACK = {
        pieces: [
            { id: "tot", ten: "Tot (Pawn)", ky_hieu: "P", diem_gia_tri: 1, cach_di: "Di thang 1 o (nuoc dau duoc di 2 o). Khong duoc di lui.", cach_an: "An cheo 1 o ve phia truoc.", luu_y: "Co kha nang phong cap thanh Hau khi tien den hang cuoi cung." },
            { id: "ma", ten: "Ma (Knight)", ky_hieu: "N", diem_gia_tri: 3, cach_di: "Di theo hinh chu L (2 o mot huong va 1 o vuong goc).", cach_an: "An quan tai o dich den cua chu L.", luu_y: "Quan duy nhat co the nhay qua dau cac quan khac tren ban co." },
            { id: "tuong", ten: "Tuong (Bishop)", ky_hieu: "B", diem_gia_tri: 3, cach_di: "Di cheo theo cac o cung mau khong gioi han so o neu khong bi chan.", cach_an: "An quan tren duong cheo cua minh.", luu_y: "Moi ben co 1 Tuong o sang va 1 Tuong o toi, phoi hop kiem soat ban co." },
            { id: "xe", ten: "Xe (Rook)", ky_hieu: "R", diem_gia_tri: 5, cach_di: "Di ngang hoac doc khong gioi han so o neu khong bi chan.", cach_an: "An quan tren duong ngang hoac doc cua minh.", luu_y: "Quan co nang chu luc o giai doan trung cuoc va tan cuoc, tham gia Nhap thanh." },
            { id: "hau", ten: "Hau (Queen)", ky_hieu: "Q", diem_gia_tri: 9, cach_di: "Ket hop suc manh cua Xe va Tuong: di ngang, doc hoac cheo khong gioi han so o.", cach_an: "An quan tren moi duong di cua minh.", luu_y: "Quan co manh nhat ban co, can bao ve can than khong nen dua ra tran qua som." },
            { id: "vua", ten: "Vua (King)", ky_hieu: "K", diem_gia_tri: 999, cach_di: "Di 1 o theo bat ky huong nao (ngang, doc, cheo) vao o an toan.", cach_an: "An quan ke ben khong co bao ve.", luu_y: "Quan co toi thuong, bi chieu het la thua cuoc. Cuoi van tro thanh quan tan cong." }
        ],
        special_rules: [
            { ten: "Nhap thanh (Castling)", mo_ta: "Vua di 2 o ve phia Xe, Xe nhay qua Vua sang o ke ben. Dieu kien ca hai quan chua tung di chuyen va khong bi chieu." },
            { ten: "Bat tot qua duong (En Passant)", mo_ta: "Khi Tot doi phuong di 2 o dung canh Tot minh o hang 5, minh co quyen an Tot do nhu the no chi di 1 o." },
            { ten: "Phong cap (Pawn Promotion)", mo_ta: "Tot tien xuong hang 8 (Trang) hoac hang 1 (Den) duoc doi ngay thanh Hau, Xe, Tuong hoac Ma tuy chon." },
            { ten: "Chieu het va Co hoa (Checkmate & Stalemate)", mo_ta: "Chieu het la thang cuoc. Neu khong bi chieu nhung khong con nuoc di hop le thi van co hoa (the hoa Pat)." }
        ],
        openings: [
            { ten: "Khai cuoc Y (Italian Game)", nuoc: "1. e4 e5 2. Nf3 Nc6 3. Bc4", y_nghia: "Phat trien Ma va Tuong nhanh chong, kiem soat trung tam va gay suc ep len o yeu f7." },
            { ten: "Phong thu Sicilia (Sicilian Defense)", nuoc: "1. e4 c5", y_nghia: "Phan cong bat doi xung gay gat tu canh hau, tao the tran doi cong hap dan." },
            { ten: "Gambit Hau (Queen's Gambit)", nuoc: "1. d4 d5 2. c4", y_nghia: "Thi sinh tot c4 de keo tot doi phuong roi khoi trung tam va gianh quyen chu dong." },
            { ten: "Khai cuoc Tay Ban Nha (Ruy Lopez)", nuoc: "1. e4 e5 2. Nf3 Nc6 3. Bb5", y_nghia: "Gay suc ep lau dai len quan Ma bao ve trung tam e5 cua Den." },
            { ten: "Phong thu Phap (French Defense)", nuoc: "1. e4 e6 2. d4 d5", y_nghia: "Thiet lap chuoi tot vung chac e6-d5 tan cong ngay vao trung tam e4 cua Trang." },
            { ten: "Phong thu Caro-Kann", nuoc: "1. e4 c6 2. d4 d5", y_nghia: "Phong thu kien co, giu duong phat trien cho Tuong canh hau khong bi chan." },
            { ten: "Phong thu An Do cua Vua", nuoc: "1. d4 Nf6 2. c4 g6 3. Nc3 Bg7", y_nghia: "Nhuong trung tam cho Trang roi phan cong manh me vao canh Vua cua Trang." },
            { ten: "He thong London (London System)", nuoc: "1. d4 d5 2. Bf4", y_nghia: "Cau truc quan co dinh, chac chan, it rui ro va de van dung cho hoc sinh." }
        ],
        tactics: [
            { ten: "Don chia doi (Fork)", mo_ta: "Mot quan co (dac biet la Ma hoac Tot) tan cong dong thoi hai muc tieu gia tri cao cua doi phuong." },
            { ten: "Don ghim quan (Pin)", mo_ta: "Tan cong quan co ma phia sau la quan gia tri cao hon (nhu Vua hoac Hau), khien no khong the di chuyen." },
            { ten: "Don xien (Skewer)", mo_ta: "Quan co gia tri cao o phia truoc bi tan cong phai thao chay, lam lo quan gia tri phia sau bi bat." },
            { ten: "Don chieu mo (Discovered Attack)", mo_ta: "Di chuyen mot quan mo duong cho quan khac phia sau chieu tuong hoac tan cong bat ngo." },
            { ten: "Don chieu nghet (Smothered Mate)", mo_ta: "Ma chieu Vua doi thu khi Vua bi chinh cac quan dong doi vay chat khong the buoc di." },
            { ten: "Don du do va Danh lac huong (Decoy & Deflection)", mo_ta: "Thi quan buoc quan chu luc phong thu cua doi phuong phai roi khoi vi tri then chot." },
            { ten: "Don coi xay gio (Windmill)", mo_ta: "Phoi hop Xe va Tuong chieu mo lien hoan de an sach cac quan cua doi thu tren duong di." },
            { ten: "Don chieu het hang day (Back-rank Mate)", mo_ta: "Xe hoac Hau chieu het o hang day vi Vua bi 3 quan Tot phia truoc chan duong chay." }
        ],
        masters: [
            { ten: "Le Quang Liem", danh_hieu: "Sieu Dai kien tuong quoc te Viet Nam", thanh_tich: "Vo dich Co chop the gioi 2013, Elo dinh cao 2740+." },
            { ten: "Magnus Carlsen", danh_hieu: "Vua co the gioi hien dai (Na Uy)", thanh_tich: "Elo cao nhat lich su 2882, vo dich tat ca the thuc co." },
            { ten: "Garry Kasparov", danh_hieu: "Huyen thoai co vua the ky 20 (Nga)", thanh_tich: "Giu ngoi vo dich the gioi 15 nam lien tiep (1985 - 2000)." },
            { ten: "Bobby Fischer", danh_hieu: "Ky tai co vua the ky 20 (My)", thanh_tich: "Vo dich the gioi nam 1972 voi nhung nuoc co kiet xuat." },
            { ten: "Judit Polgar", danh_hieu: "Nu ky thu vi dai nhat lich su", thanh_tich: "Nu ky thu duy nhat vao Top 10 the gioi giua cac nam ky thu." }
        ]
    };

    const DU_LIEU_CO_TUONG_FALLBACK = {
        pieces: [
            { id: "tuong_soai", ten: "Tuong / Soai (General)", ky_hieu: "TG", vi_tri: "O giua hang day trong Cuu Cung", cach_di: "Di tung o mot ngang hoac doc trong Cuu Cung. Khong duoc ra khoi cung.", quy_tac: "Luat mat Tuong: Hai Tuong khong bao gio duoc nhin thay nhau truc dien tren cung mot cot doc." },
            { id: "si", ten: "Si (Advisor)", ky_hieu: "SI", vi_tri: "Hai ben canh Tuong", cach_di: "Di cheo 1 o moi nuoc trong Cuu Cung.", quy_tac: "Nhiem vu ho ve Tuong, khong duoc ra khoi Cuu Cung." },
            { id: "tuong_voi", ten: "Tuong / Voi (Elephant)", ky_hieu: "TU", vi_tri: "Hai ben Si o hang day", cach_di: "Di cheo 2 o vuong (2x2).", quy_tac: "Khong duoc sang song. Neu co quan o giua duong cheo thi bi Can mat Tuong." },
            { id: "xe", ten: "Xe (Chariot)", ky_hieu: "XE", vi_tri: "Hai goc ban co", cach_di: "Di ngang hoac doc khong gioi han o neu khong bi can. An quan tren duong di.", quy_tac: "Quan co manh nhat ban co tuong, suc co dong va tan cong cao nhat." },
            { id: "phao", ten: "Phao (Cannon)", ky_hieu: "PH", vi_tri: "Hang 3 cach mep 2 o", cach_di: "Di ngang doc nhu Xe khi khong an quan.", quy_tac: "Khi an quan bat buoc phai nhay qua dung 1 quan co khac lam Ngoi." },
            { id: "ma", ten: "Ma (Horse)", ky_hieu: "MA", vi_tri: "Giua Xe va Tuong", cach_di: "Di theo hinh chu nhat (1 doc va 1 cheo hoac 1 ngang va 1 cheo).", quy_tac: "Bi Can chan Ma neu co quan dung o o lien ke theo huong buoc." },
            { id: "tot_binh", ten: "Tot / Binh (Soldier)", ky_hieu: "TO", vi_tri: "5 quan o hang 4", cach_di: "Chua sang song chi tien 1 o. Qua song duoc di thang hoac ngang 1 o.", quy_tac: "Tuyet doi khong bao gio duoc di lui. Sang song tro nen vo cung loi hai." }
        ],
        board_features: [
            { ten: "So Ha Han Gioi (Song)", y_nghia: "Ranh gioi giua 2 ben, Tuong khong duoc qua song, Tot qua song bat dau duoc di ngang." },
            { ten: "Cuu Cung (Cung Tuong)", y_nghia: "Khu vuc 3x3 co 2 duong cheo hinh chu X o moi dau san, Tuong va Si khong the roi khoi day." },
            { ten: "90 Giao Diem (Lo co)", y_nghia: "Quan co dat tai cac giao diem cua 9 duong doc va 10 duong ngang thay vi dat trong o." }
        ],
        tactics: [
            { ten: "Sat phap Ma Hau Phao", mo_ta: "Ma khong che cua thoat cua Tuong, dong thoi lam ngoi cho Phao phia sau chieu thang mat Tuong." },
            { ten: "Song Xe Toa Thanh", mo_ta: "Hai Xe tien sau vao Cuu Cung doi phuong, lien hoan chieu ep Tuong vao the het nuoc do." },
            { ten: "Diep Phao (Phao trung)", mo_ta: "Hai Phao cung nam tren mot duong, Phao truoc lam ngoi cho Phao sau chieu Tuong doi thu." },
            { ten: "Dai Dao Tieu Doi (Xe chem Si)", mo_ta: "Xe quyet doan chem Si pha toang phong tuyen Cuu Cung mo duong cho cac quan khac tran vao." },
            { ten: "Bat Son Cai The (Doi non lap be)", mo_ta: "Phoi hop giua Xe va Tot qua song ap sat hang day, don ep Tuong vao the het nuoc di." },
            { ten: "Trac Dien Ho (Ho vo nghieng)", mo_ta: "Ma danh nghieng tu suon Cuu Cung duoc Phao hoac Xe yem tro tao the sat cuc hiem." },
            { ten: "Thiet Mon Thuyen (Khoa cua sat)", mo_ta: "Xe khoa chat lo trung tam khong cho Tuong chay qua, quan con lai chieu hang day dut diem." },
            { ten: "Kham Dau Phao", mo_ta: "Phao danh thang vao Tot dau ghim chat Si Tuong khien bo chi huy bi te liet." }
        ],
        openings: [
            { ten: "Duong Dau Phao (Phao dau)", mo_ta: "Phao vao trung lo tan cong truc dien vao Tot dau va trung tam doi thu." },
            { ten: "Binh Phong Ma", mo_ta: "Hai Ma cung nhay len giu Tot dau, tao buc tuong phong thu vung chac va phan cong sac sao." },
            { ten: "Khoi Ma Cuoc", mo_ta: "Nuoc dau nhay Ma len giu trung lo, the tran uyen chuyen va giu nhieu bien hoa chien thuat." },
            { ten: "Nghich Thu Phao", mo_ta: "Doi cong sinh tu nhat trong co tuong, hai ben deu tan cong trung tam quyet liet." },
            { ten: "Tien Nhan Chi Lo", mo_ta: "Binh 7 tan 1 mo duong cho Ma va tham do phan ung chien luoc cua doi thu." },
            { ten: "Si Giac Phao", mo_ta: "Dua Phao len goc Si, phong thu kin ke va ho tro Xe Ma xuat tran." },
            { ten: "Qua Cung Phao", mo_ta: "Chuyen Phao sang mot canh tao uu the hoa luc cuc bo." }
        ],
        masters: [
            { ten: "Lai Ly Huynh", danh_hieu: "Ky vuong so 1 Viet Nam", thanh_tich: "Vo dich the gioi Co nhanh 2022, nhieu nam vo dich quoc gia." },
            { ten: "Ho Vinh Hoa", danh_hieu: "Thap lien ba Trung Quoc", thanh_tich: "10 lan vo dich lien tiep, sang tao nhieu the tran khai cuoc kinh dien." },
            { ten: "Vuong Thien Nhat", danh_hieu: "Ngoai tinh lai khach", thanh_tich: "Ky thu so 1 the gioi hon 10 nam lien tiep voi loi danh chuan xac tuyet doi." },
            { ten: "Nguyen Thanh Bao", danh_hieu: "Tay Doc co tuong Viet Nam", thanh_tich: "Huy chuong Bac the gioi, noi tieng voi loi tan cong ruc lua." }
        ]
    };

    const KHO_CAU_DO_FALLBACK = [
        // 6 cau do co vua
        {
            id: "cv_1",
            the_co: "Trang co Vua o g1, Xe o e1. Den co Vua o e8 dang o giua ban co va bi Xe kiem soat cot e.",
            cau_hoi: "Trong co vua, quan co nao la quan duy nhat co the nhay qua dau cac quan co khac tren ban co?",
            cac_lua_chon: ["A. Quan Tuong", "B. Quan Ma", "C. Quan Xe", "D. Quan Hau"],
            dap_an_dung: "B",
            giai_thich: "Quan Ma co cach di hinh chu L va la quan co duy nhat tren ban co duoc phep nhay qua dau bat ky quan nao."
        },
        {
            id: "cv_2",
            the_co: "Den vua di quan Tot tu d7 len d5 (di 2 o). Trang dang co quan Tot dung o o e5 ngay ben canh.",
            cau_hoi: "Trang co the su dung luat dac biet nao ngay lap tuc de bat quan Tot d5 cua Den?",
            cac_lua_chon: ["A. Luat Phong cap", "B. Luat Nhap thanh xa", "C. Luat Bat tot qua duong (En Passant)", "D. Luat Chieu het nhanh"],
            dap_an_dung: "C",
            giai_thich: "Luat Bat tot qua duong cho phep Tot Trang o hang 5 an Tot Den vua di 2 o ben canh bang cach di cheo xuong d6."
        },
        {
            id: "cv_3",
            the_co: "Quan Ma Trang nhay vao o e7 chieu Vua Den o g8, dong thoi tan cong quan Hau Den dang dung o c8.",
            cau_hoi: "Don chien thuat ma quan Ma Trang vua thuc hien duoc goi la don gi?",
            cac_lua_chon: ["A. Don chia doi (Fork)", "B. Don ghim quan (Pin)", "C. Don xien (Skewer)", "D. Don chieu mo"],
            dap_an_dung: "A",
            giai_thich: "Don chia doi la khi mot quan co (dac biet la Ma) tan cong dong thoi hai muc tieu gia tri cao khien doi thu khong the cuu het ca hai."
        },
        {
            id: "cv_4",
            the_co: "Tong diem cua 1 Xe (5 diem) va 1 Ma (3 diem) so voi 1 Hau (9 diem) la bao nhieu?",
            cau_hoi: "Khi doi 1 Xe va 1 Ma lay 1 Hau doi phuong, chenh lech diem so la gi?",
            cac_lua_chon: ["A. 8 diem so voi 9 diem (Kem hon 1 diem)", "B. 10 diem so voi 9 diem (Hon 1 diem)", "C. Bang nhau 9 diem", "D. 7 diem so voi 9 diem"],
            dap_an_dung: "A",
            giai_thich: "1 Xe (5) + 1 Ma (3) = 8 diem, thap hon 1 Hau (9) 1 diem."
        },
        {
            id: "cv_5",
            the_co: "Vua Den khong bi chieu nhung khong con nuoc di hop le nao tren toan ban co.",
            cau_hoi: "Ket qua cua van co trong truong hop nay duoc trong tai tuyen bo nhu the nao?",
            cac_lua_chon: ["A. Den bi xu thua", "B. Trang thang cuoc", "C. Van co hoa (The hoa Pat / Stalemate)", "D. Choi lai tu dau"],
            dap_an_dung: "C",
            giai_thich: "Khi mot ben khong bi chieu nhung khong con nuoc di hop le thi van co hoa theo luat Stalemate."
        },
        {
            id: "cv_6",
            the_co: "Vua Den o g8 bi bao quanh boi Tot f7, Tot g7 va Xe h8. Ma Trang nhay vao f7 chieu Vua.",
            cau_hoi: "Don chieu het khi Vua bi chinh cac quan cua minh vay chat khong the di chuyen duoc goi la gi?",
            cac_lua_chon: ["A. Don chieu nghet (Smothered Mate)", "B. Don coi xay gio", "C. Don ghim quan tuyet doi", "D. Don du do Vua"],
            dap_an_dung: "A",
            giai_thich: "Don chieu nghet la don dac trung cua quan Ma khi Vua doi thu bi quan nha bao kin."
        },
        // 6 cau do co tuong
        {
            id: "ct_1",
            the_co: "Hai Tuong Do va Den cung nam tren lo 5 ma khong co quan chan o giua.",
            cau_hoi: "Theo luat co tuong, tinh huong hai Tuong nhin thay mat nhau truc dien bi xu ly the nao?",
            cac_lua_chon: ["A. Luat mat Tuong - Nuoc di de lo mat Tuong la pham luat", "B. Duoc phep va hai ben hoa", "C. Ben nao di sau bi xu thua", "D. Ca hai Tuong bi loai"],
            dap_an_dung: "A",
            giai_thich: "Hai Tuong khong bao gio duoc doi mat truc dien tren cung mot cot doc ma khong co quan can."
        },
        {
            id: "ct_2",
            the_co: "Quan Phao Do muon an quan Xe Den dang dung o phia xa tren cung mot duong ngang.",
            cau_hoi: "Dieu kien bat buoc de quan Phao co the an quan doi phuong trong co tuong la gi?",
            cac_lua_chon: ["A. Phai co dung mot quan co o giua lam Ngoi", "B. Phai dung sat ngay quan Xe", "C. Phai co hai quan o giua", "D. Khong can quan nao o giua"],
            dap_an_dung: "A",
            giai_thich: "Phao khi an quan bat buoc phai nhay qua dung 1 quan co lam Ngoi."
        },
        {
            id: "ct_3",
            the_co: "Quan Ma Do dinh nhay chieu Tuong Den nhung ngay o lien ke truoc mat Ma co quan Tot dung chan.",
            cau_hoi: "Hien tuong nay trong co tuong duoc goi la gi va Ma co nhay duoc khong?",
            cac_lua_chon: ["A. Can chan Ma - Ma khong duoc phep nhay theo huong do", "B. Ma duoc phep nhay qua dau quan Tot", "C. Can mat Tuong", "D. Ma phai an quan Tot do"],
            dap_an_dung: "A",
            giai_thich: "Can chan Ma: neu co quan dung o lien ke theo huong buoc thi Ma khong the nhay."
        },
        {
            id: "ct_4",
            the_co: "Quan Tot Do da tien qua song va ap sat Cuu Cung doi phuong.",
            cau_hoi: "Sau khi qua song, quy tac di chuyen cua quan Tot trong co tuong co su thay doi quan trong nao?",
            cac_lua_chon: ["A. Duoc phep di ngang 1 o va tien 1 o (khong duoc di lui)", "B. Duoc di lui ve phong thu", "C. Duoc phong cap thanh Xe", "D. Duoc di cheo giong Si"],
            dap_an_dung: "A",
            giai_thich: "Sau khi qua song, Tot duoc di ngang va di thang 1 o moi nuoc, khong bao gio di lui."
        },
        {
            id: "ct_5",
            the_co: "Phao Do dung sau quan Ma Do tren cung mot duong thang, Ma Do nhay chieu dong thoi lam ngoi cho Phao.",
            cau_hoi: "Don sat phap kinh dien pho bien nay trong co tuong duoc goi la gi?",
            cac_lua_chon: ["A. Sat phap Ma Hau Phao", "B. Sat phap Song Xe Toa Thanh", "C. Sat phap Dai Dao Tieu Doi", "D. Sat phap Tam Cuu Lien Hoan"],
            dap_an_dung: "A",
            giai_thich: "Sat phap Ma Hau Phao: Ma khoa cua thoat va lam ngoi cho Phao phia sau chieu dut diem."
        },
        {
            id: "ct_6",
            the_co: "Quan Tuong (Voi) Do muon bay qua dong song de tan cong Tuong doi phuong.",
            cau_hoi: "Theo luat co tuong, quan Tuong (Voi) co duoc phep di qua song khong?",
            cac_lua_chon: ["A. Khong bao gio duoc phep qua song, chi phong thu san nha", "B. Duoc phep qua song khi doi phuong con 1 quan", "C. Duoc qua song neu di 4 o", "D. Duoc qua song neu co Ma bao ve"],
            dap_an_dung: "A",
            giai_thich: "Quan Tuong (Voi) la quan thuan tuy phong thu noi dia, khong duoc phep qua song."
        }
    ];

    const THE_CO_MAU_FALLBACK = [
        {
            id: "the_cv_1",
            loai: "co_vua",
            tieu_de: "The co Don Chia Doi cua Ma Trang (Fork)",
            mo_ta: "Ma Trang o o c7 chieu Vua Den o e8 dong thoi bat quan Xe Den o a8.",
            loi_khuyen: "Khi choi, luon quan sat cac o ma quan Ma co the nhay vao de khong bi dinh don chia doi.",
            ben_di_truoc: "Quan Trang (White)",
            nuoc_tiep_theo: "Vua Den phai di chuyen tranh chieu, Ma Trang an Xe Den o a8 thu ve 5 diem."
        },
        {
            id: "the_cv_2",
            loai: "co_vua",
            tieu_de: "The Chieu Het Hoc Gia (Scholar's Mate)",
            mo_ta: "Hau Trang o f7 chieu het Vua Den nho su bao ve cua Tuong Trang o c4.",
            loi_khuyen: "Diem yeu f7 chi co Vua bao ve trong khai cuoc. Den can phat trien Ma len f6 de ngan Hau tiep can.",
            ben_di_truoc: "Quan Trang (White)",
            nuoc_tiep_theo: "Hau Trang an vao f7 chieu het trong 4 nuoc neu Den khong phong thu dung cach."
        },
        {
            id: "the_cv_3",
            loai: "co_vua",
            tieu_de: "The Don Chieu Nghet (Smothered Mate)",
            mo_ta: "Vua Den bi quan nha vay kin tai o g8, Ma Trang nhay vao f7 chieu dut diem khong lo thoat.",
            loi_khuyen: "Tranh de cac quan co cua minh chen chuc xung quanh Vua ma khong co o thoat khi gap Ma.",
            ben_di_truoc: "Quan Trang (White)",
            nuoc_tiep_theo: "Ma Trang nhay den f7 hoac h6 chieu het hoan toan."
        },
        {
            id: "the_cv_4",
            loai: "co_vua",
            tieu_de: "The Chieu Het Hang Day (Back-rank Mate)",
            mo_ta: "Xe Trang lao xuong o e8 chieu het Vua Den vi 3 quan Tot f7, g7, h7 chua mo duong thoat.",
            loi_khuyen: "Luon chu dong day 1 quan Tot len de tao 'cua so thoat khi' cho Vua.",
            ben_di_truoc: "Quan Trang (White)",
            nuoc_tiep_theo: "Xe Trang danh chieu o e8, Vua Den khong the chay len hang 7."
        },
        {
            id: "the_ct_1",
            loai: "co_tuong",
            tieu_de: "Sat Phap Ma Hau Phao Tuyet Ky",
            mo_ta: "Ma Do khoa cua thoat cua Tuong Den, Phao Do dung phia sau Ma chieu thang mat Tuong.",
            loi_khuyen: "Canh giac cao do khi thay Ma va Phao doi phuong hop luc tan cong vao mot lo.",
            ben_di_truoc: "Quan Do (Red)",
            nuoc_tiep_theo: "Tuong Den khong the di chuyen vi Ma can duong, khong an duoc Phao o xa, ket thuc tran."
        },
        {
            id: "the_ct_2",
            loai: "co_tuong",
            tieu_de: "Song Xe Toa Thanh Pha Cung",
            mo_ta: "Hai Xe Do chim xuong hang day va hang ap day cua Cuu Cung doi phuong.",
            loi_khuyen: "Phong tuyen Si va Tuong can duoc bao ve chat che de ngan Xe doi phuong ap sat.",
            ben_di_truoc: "Quan Do (Red)",
            nuoc_tiep_theo: "Xe 1 chieu ep Tuong len, Xe 2 ap sat chieu het buoc Tuong phai dau hang."
        },
        {
            id: "the_ct_3",
            loai: "co_tuong",
            tieu_de: "Sat Phap Thiet Mon Thuyen (Khoa Cua Sat)",
            mo_ta: "Xe Do dung giua lo 5 khoa chat mat Tuong Den, Xe thu hai lao xuong hang 10 chieu het.",
            loi_khuyen: "Tuyet doi khong de doi phuong chiem giu lo trung tam khi Tuong nha dang lech canh.",
            ben_di_truoc: "Quan Do (Red)",
            nuoc_tiep_theo: "Tuong Den khong the sang lo 5 vi lo mat Tuong, bi Xe hang day chem ha."
        },
        {
            id: "the_ct_4",
            loai: "co_tuong",
            tieu_de: "Sat Phap Dai Dao Tieu Doi (Xe Chem Si)",
            mo_ta: "Xe Do dung luc chem thang vao Si trung tam mo toang Cuu Cung de Phao tran vao.",
            loi_khuyen: "Khi co co hoi dut diem nhanh, dung ngan ngai hy sinh quan nang de be gay phong tuyen.",
            ben_di_truoc: "Quan Do (Red)",
            nuoc_tiep_theo: "Phao va Ma Do tiep quan tran vao bat Tuong Den trong 2 nuoc tiep theo."
        }
    ];

    let currentQuizIndex = 0;
    let quizList = KHO_CAU_DO_FALLBACK;
    let userProgress = {
        cau_da_giai: [],
        tong_diem_exp: 0,
        danh_hieu: "Ky Thu Tap Su",
        cup_dat_duoc: ["Cup Dong Ky Thu"]
    };

    async function napDuLieuCoTriTue() {
        try {
            const res = await fetch("/api/chess");
            if (res.ok) {
                const data = await res.json();
                if (data.status === "success") {
                    hienThiCoVua(data.co_vua || DU_LIEU_CO_VUA_FALLBACK);
                    hienThiCoTuong(data.co_tuong || DU_LIEU_CO_TUONG_FALLBACK);
                    if (data.co_vua && data.co_tuong) {
                        quizList = (data.co_vua.puzzles || []).concat(data.co_tuong.puzzles || []);
                    }
                    if (data.progress) {
                        userProgress = data.progress;
                        capNhatHeaderBadge();
                    }
                    const posList = data.sample_positions || THE_CO_MAU_FALLBACK;
                    hienThiTheCoMau(posList);
                    hienThiCupGiaiDau(userProgress);
                    taiCauDo(0);
                    return;
                }
            }
        } catch (e) {
            console.warn("Khong the tai /api/chess, su dung du lieu du phong offline:", e);
        }

        hienThiCoVua(DU_LIEU_CO_VUA_FALLBACK);
        hienThiCoTuong(DU_LIEU_CO_TUONG_FALLBACK);
        quizList = KHO_CAU_DO_FALLBACK;
        hienThiTheCoMau(THE_CO_MAU_FALLBACK);
        hienThiCupGiaiDau(userProgress);
        taiCauDo(0);
    }

    function capNhatHeaderBadge() {
        const badgeTitle = document.getElementById("chess-badge-title");
        const badgeExp = document.getElementById("chess-badge-exp");
        const cups = userProgress.cup_dat_duoc || ["Cup Dong Ky Thu"];
        if (badgeTitle) badgeTitle.innerText = `${userProgress.danh_hieu || "Ky Thu Tap Su"} (Cup: ${cups.length})`;
        if (badgeExp) badgeExp.innerText = `EXP Co: ${userProgress.tong_diem_exp || 0}`;
    }

    function hienThiCoVua(data) {
        const container = document.getElementById("chess-vua-pieces-grid");
        if (!container) return;

        container.innerHTML = "";
        (data.pieces || []).forEach(p => {
            const card = document.createElement("div");
            card.className = "chess-piece-card";
            card.innerHTML = `
                <div class="chess-piece-badge">${p.ky_hieu}</div>
                <div class="chess-piece-info">
                    <div class="chess-piece-title">${p.ten} <span class="chess-val-pill">${p.diem_gia_tri} diem</span></div>
                    <div class="chess-piece-desc"><strong>Cach di:</strong> ${p.cach_di}</div>
                    <div class="chess-piece-desc"><strong>Cach an:</strong> ${p.cach_an}</div>
                    <div class="chess-piece-note"><strong>Luu y:</strong> ${p.luu_y}</div>
                </div>
            `;
            container.appendChild(card);
        });

        const specialContainer = document.getElementById("chess-vua-special-rules");
        if (specialContainer && data.special_rules) {
            specialContainer.innerHTML = "";
            data.special_rules.forEach(r => {
                const item = document.createElement("div");
                item.className = "chess-rule-item";
                item.innerHTML = `
                    <div class="chess-rule-title">${r.ten}</div>
                    <div class="chess-rule-desc">${r.mo_ta || r.dieu_kien || ""}</div>
                `;
                specialContainer.appendChild(item);
            });
        }
    }

    function hienThiCoTuong(data) {
        const container = document.getElementById("chess-tuong-pieces-grid");
        if (!container) return;

        container.innerHTML = "";
        (data.pieces || []).forEach(p => {
            const card = document.createElement("div");
            card.className = "chess-piece-card xiangqi-card";
            card.innerHTML = `
                <div class="xiangqi-piece-badge">${p.ky_hieu}</div>
                <div class="chess-piece-info">
                    <div class="chess-piece-title">${p.ten}</div>
                    <div class="chess-piece-desc"><strong>Vi tri:</strong> ${p.vi_tri}</div>
                    <div class="chess-piece-desc"><strong>Cach di:</strong> ${p.cach_di}</div>
                    <div class="chess-piece-note xiangqi-note"><strong>Quy tac:</strong> ${p.quy_tac || p.luat_dac_biet || ""}</div>
                </div>
            `;
            container.appendChild(card);
        });

        const tacticsContainer = document.getElementById("chess-tuong-tactics");
        if (tacticsContainer && data.tactics) {
            tacticsContainer.innerHTML = "";
            data.tactics.forEach(t => {
                const item = document.createElement("div");
                item.className = "chess-rule-item xiangqi-rule-item";
                item.innerHTML = `
                    <div class="chess-rule-title xiangqi-title">${t.ten}</div>
                    <div class="chess-rule-desc">${t.mo_ta}</div>
                `;
                tacticsContainer.appendChild(item);
            });
        }
    }

    function hienThiTheCoMau(positions) {
        const select = document.getElementById("chess-select-sample");
        if (!select) return;

        select.innerHTML = "";
        positions.forEach((pos, idx) => {
            const opt = document.createElement("option");
            opt.value = idx;
            opt.textContent = `[${pos.loai === 'co_vua' ? 'CO VUA' : 'CO TUONG'}] ${pos.tieu_de}`;
            select.appendChild(opt);
        });

        select.addEventListener("change", function () {
            const pos = positions[parseInt(this.value, 10)] || positions[0];
            capNhatThongTinTheCo(pos);
        });

        if (positions.length > 0) {
            capNhatThongTinTheCo(positions[0]);
        }
    }

    function capNhatThongTinTheCo(pos) {
        const titleEl = document.getElementById("chess-sample-title");
        const descEl = document.getElementById("chess-sample-desc");
        const moveEl = document.getElementById("chess-sample-move");
        const tipEl = document.getElementById("chess-sample-tip");

        if (titleEl) titleEl.innerText = pos.tieu_de.toUpperCase();
        if (descEl) descEl.innerText = `${pos.mo_ta} (Ben di truoc: ${pos.ben_di_truoc})`;
        if (moveEl) moveEl.innerText = `Nuoc di toi uu: ${pos.nuoc_tiep_theo}`;
        if (tipEl) tipEl.innerText = `Loi khuyen chien luoc: ${pos.loi_khuyen}`;

        veBanCoTrucQuan(pos);
    }

    // Ve ban co truc quan (Visual Board Rendering)
    function veBanCoTrucQuan(pos) {
        const boardContainer = document.getElementById("chess-visual-board-container");
        if (!boardContainer) return;

        if (pos.loai === "co_vua") {
            veBanCoVuaGrid(boardContainer, pos);
        } else {
            veBanCoTuongGrid(boardContainer, pos);
        }
    }

    function veBanCoVuaGrid(container, pos) {
        const files = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'];
        const ranks = ['8', '7', '6', '5', '4', '3', '2', '1'];

        // Vi tri quan co tieu bieu theo tung the co
        const piecePlacements = {
            'the_cv_1': { 'c7': 'N (Trang)', 'e8': 'K (Den)', 'a8': 'r (Den)', 'g1': 'K (Trang)', 'e1': 'R (Trang)' },
            'the_cv_2': { 'f7': 'Q (Trang)', 'e8': 'K (Den)', 'c4': 'B (Trang)', 'e4': 'P (Trang)', 'e5': 'p (Den)' },
            'the_cv_3': { 'f7': 'N (Trang)', 'g8': 'K (Den)', 'f8': 'r (Den)', 'g7': 'p (Den)', 'h7': 'p (Den)' },
            'the_cv_4': { 'e8': 'R (Trang)', 'g8': 'K (Den)', 'f7': 'p (Den)', 'g7': 'p (Den)', 'h7': 'p (Den)' }
        };

        const currentMap = piecePlacements[pos.id] || piecePlacements['the_cv_1'];

        let html = `
            <div style="display: flex; flex-direction: column; align-items: center;">
                <div style="font-weight: 900; color: #60A5FA; margin-bottom: 8px; font-size: 14px;">BAN CO VUA 8x8 TRUC QUAN (TOA DO A-H, 1-8)</div>
                <div style="display: grid; grid-template-columns: repeat(8, 42px); grid-template-rows: repeat(8, 42px); border: 3px solid #6366F1; border-radius: 6px; overflow: hidden; box-shadow: 0 8px 24px rgba(0,0,0,0.6);">
        `;

        ranks.forEach((r, rIdx) => {
            files.forEach((f, fIdx) => {
                const sq = `${f}${r}`;
                const isLight = (rIdx + fIdx) % 2 === 0;
                const bg = isLight ? '#E2E8F0' : '#475569';
                const hasPiece = currentMap[sq];
                const isHighlighted = (sq === 'c7' || sq === 'f7' || sq === 'e8' || sq === 'a8');
                const borderStyle = isHighlighted ? 'border: 2px solid #F59E0B; z-index: 2;' : '';

                let pieceHtml = '';
                if (hasPiece) {
                    const isWhite = hasPiece.includes('(Trang)');
                    const pieceColor = isWhite ? '#1E293B' : '#DC2626';
                    const pieceLetter = hasPiece.split(' ')[0];
                    pieceHtml = `<span style="font-size: 13px; font-weight: 900; color: ${pieceColor}; text-shadow: 0 1px 2px rgba(255,255,255,0.4);">${pieceLetter}</span>`;
                }

                html += `
                    <div style="width: 42px; height: 42px; background: ${bg}; ${borderStyle} display: flex; align-items: center; justify-content: center; position: relative;">
                        ${pieceHtml}
                        <span style="position: absolute; bottom: 1px; right: 2px; font-size: 8px; color: ${isLight ? '#64748B' : '#CBD5E1'}; font-weight: 700;">${sq}</span>
                    </div>
                `;
            });
        });

        html += `
                </div>
                <div style="font-size: 12px; color: #94A3B8; margin-top: 8px;">Quan Trang: K (Vua), Q (Hau), R (Xe), B (Tuong), N (Ma), P (Tot) | Quan Den (chu do)</div>
            </div>
        `;

        container.innerHTML = html;
    }

    function veBanCoTuongGrid(container, pos) {
        const piecePlacements = {
            'the_ct_1': { '4,0': 'TG (Den)', '4,2': 'MA (Do)', '4,3': 'PH (Do)' },
            'the_ct_2': { '4,0': 'TG (Den)', '3,1': 'XE (Do)', '5,0': 'XE (Do)' },
            'the_ct_3': { '4,0': 'TG (Den)', '4,5': 'XE (Do)', '3,0': 'XE (Do)' },
            'the_ct_4': { '4,0': 'TG (Den)', '3,0': 'XE (Do)', '4,1': 'PH (Do)' }
        };

        const currentMap = piecePlacements[pos.id] || piecePlacements['the_ct_1'];

        let html = `
            <div style="display: flex; flex-direction: column; align-items: center;">
                <div style="font-weight: 900; color: #EF4444; margin-bottom: 8px; font-size: 14px;">BAN CO TUONG PHUONG DONG (SO HA - HAN GIOI & CUU CUNG)</div>
                <div style="position: relative; width: 320px; height: 350px; background: #FEF3C7; border: 3px solid #B45309; border-radius: 8px; box-shadow: 0 8px 24px rgba(0,0,0,0.6); padding: 12px;">
                    <!-- So Ha Han Gioi River -->
                    <div style="position: absolute; top: 155px; left: 12px; right: 12px; height: 30px; background: #BAE6FD; border-top: 2px solid #B45309; border-bottom: 2px solid #B45309; display: flex; align-items: center; justify-content: center; font-weight: 900; color: #0369A1; font-size: 12px; letter-spacing: 2px;">
                        SO HA - HAN GIOI
                    </div>

                    <!-- Cuu Cung lines representation -->
                    <div style="position: absolute; top: 12px; left: 105px; width: 110px; height: 95px; border: 1.5px dashed #B45309; pointer-events: none;"></div>
                    <div style="position: absolute; bottom: 12px; left: 105px; width: 110px; height: 95px; border: 1.5px dashed #B45309; pointer-events: none;"></div>

                    <!-- Pieces rendering -->
        `;

        for (const coord in currentMap) {
            const [c, r] = coord.split(',').map(Number);
            const pieceName = currentMap[coord];
            const isRed = pieceName.includes('(Do)');
            const bgPiece = isRed ? '#EF4444' : '#1E293B';
            const borderPiece = isRed ? '#FDE047' : '#FFFFFF';
            const leftPx = 25 + c * 30;
            const topPx = 20 + r * 30;

            html += `
                <div style="position: absolute; left: ${leftPx}px; top: ${topPx}px; width: 28px; height: 28px; background: ${bgPiece}; border: 2px solid ${borderPiece}; border-radius: 50%; display: flex; align-items: center; justify-content: center; color: #FFFFFF; font-size: 10px; font-weight: 900; box-shadow: 0 2px 6px rgba(0,0,0,0.5); z-index: 3;">
                    ${pieceName.split(' ')[0]}
                </div>
            `;
        }

        html += `
                </div>
                <div style="font-size: 12px; color: #94A3B8; margin-top: 8px;">Quan Do: TG (Tuong), SI, TU, XE, PH (Phao), MA, TO | Quan Den (nen toi)</div>
            </div>
        `;

        container.innerHTML = html;
    }

    function hienThiCupGiaiDau(progress) {
        const container = document.getElementById("chess-tournament-cups");
        if (!container) return;

        const cupsInfo = [
            { id: "Cup Dong Ky Thu", ten: "Cup Dong Ky Thu", exp_req: 0, cap: "Vong 1: Tap Su Khoi Dong", mau: "#D97706" },
            { id: "Cup Bac Ky Thu", ten: "Cup Bac Ky Thu", exp_req: 100, cap: "Vong 2: Kien Tuong Lop", mau: "#94A3B8" },
            { id: "Cup Vang Ky Thu", ten: "Cup Vang Ky Thu", exp_req: 250, cap: "Vong 3: Kien Tuong Truong", mau: "#F59E0B" },
            { id: "Cup Bach Kim Ky Thu", ten: "Cup Bach Kim Ky Thu", exp_req: 500, cap: "Vong 4: Kien Tuong Tinh", mau: "#06B6D4" },
            { id: "Cup Kim Cuong Dai Kien Tuong", ten: "Cup Kim Cuong Dai Kien Tuong", exp_req: 800, cap: "Vong 5: Dai Kien Tuong THCS", mau: "#A855F7" }
        ];

        const unlockedCups = progress.cup_dat_duoc || ["Cup Dong Ky Thu"];
        const currentExp = progress.tong_diem_exp || 0;

        container.innerHTML = "";
        cupsInfo.forEach(c => {
            const isUnlocked = unlockedCups.includes(c.id) || currentExp >= c.exp_req;
            const card = document.createElement("div");
            card.style.cssText = `
                background: ${isUnlocked ? 'rgba(30, 27, 75, 0.9)' : 'rgba(15, 23, 42, 0.6)'};
                border: 2px solid ${isUnlocked ? c.mau : '#334155'};
                border-radius: 12px; padding: 12px; text-align: center;
                opacity: ${isUnlocked ? '1' : '0.55'};
            `;

            card.innerHTML = `
                <div style="font-weight: 900; font-size: 13px; color: ${isUnlocked ? c.mau : '#64748B'}; margin-bottom: 4px;">
                    ${c.ten}
                </div>
                <div style="font-size: 11.5px; color: #CBD5E1; margin-bottom: 6px;">${c.cap}</div>
                <div style="font-size: 11px; font-weight: bold; padding: 2px 8px; border-radius: 6px; display: inline-block; background: ${isUnlocked ? 'rgba(16, 185, 129, 0.2)' : 'rgba(100, 116, 139, 0.2)'}; color: ${isUnlocked ? '#34D399' : '#94A3B8'};">
                    ${isUnlocked ? 'DA MO KHOA' : `Can ${c.exp_req} EXP`}
                </div>
            `;
            container.appendChild(card);
        });
    }

    function taiCauDo(idx) {
        if (!quizList || quizList.length === 0) return;
        currentQuizIndex = idx % quizList.length;
        const q = quizList[currentQuizIndex];

        const sitEl = document.getElementById("chess-quiz-situation");
        const quesEl = document.getElementById("chess-quiz-question");
        const optsContainer = document.getElementById("chess-quiz-options");
        const resultEl = document.getElementById("chess-quiz-result");

        if (sitEl) sitEl.innerText = `Tinh huong the co (${currentQuizIndex + 1}/${quizList.length}): ${q.the_co}`;
        if (quesEl) quesEl.innerText = q.cau_hoi;
        if (resultEl) {
            resultEl.innerText = "Hay chon dap an dung de nhan +30 XP va +15 Coin!";
            resultEl.className = "chess-quiz-feedback default-feedback";
        }

        if (optsContainer) {
            optsContainer.innerHTML = "";
            (q.cac_lua_chon || []).forEach((opt, optIdx) => {
                const optLetter = ["A", "B", "C", "D"][optIdx];
                const btn = document.createElement("button");
                btn.className = "chess-opt-btn";
                btn.innerText = opt;
                btn.onclick = () => kiemTraDapAn(q, optLetter, btn);
                optsContainer.appendChild(btn);
            });
        }
    }

    async function kiemTraDapAn(q, chosenLetter, btnClicked) {
        const allBtns = document.querySelectorAll(".chess-opt-btn");
        allBtns.forEach(b => b.disabled = true);

        const dung = (chosenLetter.trim().toUpperCase() === q.dap_an_dung.trim().toUpperCase());
        const resultEl = document.getElementById("chess-quiz-result");

        if (dung) {
            btnClicked.classList.add("correct-btn");
            userProgress.tong_diem_exp = (userProgress.tong_diem_exp || 0) + 30;
            if (!userProgress.cau_da_giai.includes(q.id)) {
                userProgress.cau_da_giai.push(q.id);
            }

            const soDung = userProgress.cau_da_giai.length;
            const cups = new Set(userProgress.cup_dat_duoc || ["Cup Dong Ky Thu"]);

            if (soDung >= 18) {
                userProgress.danh_hieu = "Dai Kien Tuong THCS Toan Quoc";
                cups.add("Cup Kim Cuong Dai Kien Tuong");
            } else if (soDung >= 12) {
                userProgress.danh_hieu = "Kien Tuong Tinh";
                cups.add("Cup Bach Kim Ky Thu");
            } else if (soDung >= 8) {
                userProgress.danh_hieu = "Kien Tuong Truong";
                cups.add("Cup Vang Ky Thu");
            } else if (soDung >= 4) {
                userProgress.danh_hieu = "Kien Tuong Lop";
                cups.add("Cup Bac Ky Thu");
            }
            userProgress.cup_dat_duoc = Array.from(cups);

            if (resultEl) {
                resultEl.innerText = `CHINH XAC! (+30 XP, +15 Coin)\nGiai thich: ${q.giai_thich}`;
                resultEl.className = "chess-quiz-feedback correct-feedback";
            }

            capNhatHeaderBadge();
            hienThiCupGiaiDau(userProgress);

            try {
                fetch("/api/chess", {
                    method: "POST",
                    headers: { "Content-Type": "application/json" },
                    body: JSON.stringify({ action: "solve_puzzle", puzzle_id: q.id, answer: chosenLetter })
                });
            } catch (e) {}
        } else {
            btnClicked.classList.add("incorrect-btn");
            allBtns.forEach((b, idx) => {
                const optLetter = ["A", "B", "C", "D"][idx];
                if (optLetter === q.dap_an_dung) {
                    b.classList.add("correct-btn");
                }
            });

            if (resultEl) {
                resultEl.innerText = `CHUA CHINH XAC! (Dap an dung la ${q.dap_an_dung})\nGiai thich: ${q.giai_thich}`;
                resultEl.className = "chess-quiz-feedback incorrect-feedback";
            }
        }
    }

    window.switchChessSubTab = function (subId, btn) {
        const panes = document.querySelectorAll('.chess-subtab-pane');
        panes.forEach(p => p.style.display = 'none');
        const target = document.getElementById('chess-subpane-' + subId);
        if (target) target.style.display = 'block';

        if (btn && btn.parentElement) {
            const btns = btn.parentElement.querySelectorAll('.fb-subtab-btn');
            btns.forEach(b => {
                b.classList.remove('active');
                b.style.background = '';
            });
            btn.classList.add('active');
            btn.style.background = 'linear-gradient(135deg, #4F46E5, #3730A3)';
        }
    };

    document.addEventListener("DOMContentLoaded", () => {
        napDuLieuCoTriTue();

        const btnNext = document.getElementById("chess-btn-next-quiz");
        if (btnNext) {
            btnNext.addEventListener("click", () => {
                taiCauDo(currentQuizIndex + 1);
            });
        }

        const btnVua = document.getElementById("chess-filter-vua");
        if (btnVua) {
            btnVua.addEventListener("click", () => {
                quizList = KHO_CAU_DO_FALLBACK.filter(q => q.id.startsWith("cv"));
                taiCauDo(0);
            });
        }

        const btnTuong = document.getElementById("chess-filter-tuong");
        if (btnTuong) {
            btnTuong.addEventListener("click", () => {
                quizList = KHO_CAU_DO_FALLBACK.filter(q => q.id.startsWith("ct"));
                taiCauDo(0);
            });
        }

        const btnAll = document.getElementById("chess-filter-all");
        if (btnAll) {
            btnAll.addEventListener("click", () => {
                quizList = KHO_CAU_DO_FALLBACK;
                taiCauDo(0);
            });
        }
    });

})();
