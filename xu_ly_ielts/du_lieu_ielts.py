# Thu muc: xu_ly_ielts
# File: du_lieu_ielts.py
# Mo ta: Du lieu va bai tap Tap Thi IELTS ho tro phan loai Band diem va tach biet Script Nghe cho khoi tao TTS sang Tieng Viet co dau

def lay_danh_sach_tu_vung_ielts(band="Band 5.5 - 6.0"):
    """Trả về danh sách từ vựng IELTS phân loại theo Band điểm target."""
    if "4.5" in band or "5.0" in band:
        return [
            {
                "id": 1,
                "cau_hoi": "Từ vựng IELTS Band 4.5 - 5.0: Từ 'Improve' có nghĩa là gì?",
                "dap_an": ["Cải thiện, nâng cao", "Hủy bỏ", "Bắt đầu", "Kết thúc"],
                "dap_an_dung": "Cải thiện, nâng cao",
                "giai_thich": "Improve (động từ) nghĩa là làm cho tốt hơn, cải thiện. Ví dụ: Improve English skills.",
                "mon_hoc": "Tiếng Anh IELTS",
                "chuong": "Từ vựng IELTS Band 4.5 - 5.0"
            },
            {
                "id": 2,
                "cau_hoi": "Từ vựng IELTS Band 4.5 - 5.0: Chọn từ nghĩa là 'Thuận lợi / Thuận tiện':",
                "dap_an": ["Convenient", "Difficult", "Dangerous", "Expensive"],
                "dap_an_dung": "Convenient",
                "giai_thich": "Convenient (tính từ) nghĩa là thuận tiện, thích hợp.",
                "mon_hoc": "Tiếng Anh IELTS",
                "chuong": "Từ vựng IELTS Band 4.5 - 5.0"
            }
        ]
    elif "6.5" in band or "7.0" in band:
        return [
            {
                "id": 1,
                "cau_hoi": "Từ vựng IELTS Band 6.5 - 7.0: Từ 'Accumulate' có nghĩa là gì?",
                "dap_an": ["Tích lũy, tích tụ", "Phân phát", "Hủy bỏ", "Di chuyển"],
                "dap_an_dung": "Tích lũy, tích tụ",
                "giai_thich": "Accumulate (động từ) nghĩa là tích lũy, gom lại theo thời gian.",
                "mon_hoc": "Tiếng Anh IELTS",
                "chuong": "Từ vựng IELTS Band 6.5 - 7.0"
            },
            {
                "id": 2,
                "cau_hoi": "Từ vựng IELTS Band 6.5 - 7.0: Chọn từ đồng nghĩa chính xác với 'Crucial':",
                "dap_an": ["Vital / Extremely important", "Unimportant", "Small", "Temporary"],
                "dap_an_dung": "Vital / Extremely important",
                "giai_thich": "Crucial nghĩa là cực kỳ quan trọng, tương đương với Vital.",
                "mon_hoc": "Tiếng Anh IELTS",
                "chuong": "Từ vựng IELTS Band 6.5 - 7.0"
            }
        ]
    elif "7.5" in band or "8.5" in band:
        return [
            {
                "id": 1,
                "cau_hoi": "Từ vựng IELTS Band 7.5 - 8.5+: Chọn từ có nghĩa là 'Làm giảm nhẹ / Giảm thiểu tác hại':",
                "dap_an": ["Mitigate", "Exacerbate", "Aggregate", "Formulate"],
                "dap_an_dung": "Mitigate",
                "giai_thich": "Mitigate (động từ) nghĩa là làm dịu bớt, giảm nhẹ hậu quả (to make something less harmful).",
                "mon_hoc": "Tiếng Anh IELTS",
                "chuong": "Từ vựng IELTS Band 7.5 - 8.5+"
            },
            {
                "id": 2,
                "cau_hoi": "Từ vựng IELTS Band 7.5 - 8.5+: Điền collocations phù hợp: 'The policy had a _____ effect on the local economy.'",
                "dap_an": ["profound", "shallow", "tiny", "careless"],
                "dap_an_dung": "profound",
                "giai_thich": "Profound effect (cụm từ cố định) nghĩa là tác động vô cùng sâu sắc.",
                "mon_hoc": "Tiếng Anh IELTS",
                "chuong": "Từ vựng IELTS Band 7.5 - 8.5+"
            }
        ]
    else:
        # Band 5.5 - 6.0
        return [
            {
                "id": 1,
                "cau_hoi": "Từ vựng IELTS Band 5.5 - 6.0: Từ 'Encouraging' có nghĩa là gì?",
                "dap_an": ["Khuyến khích, mang lại hy vọng", "Thất vọng", "Lo lắng", "Chán nản"],
                "dap_an_dung": "Khuyến khích, mang lại hy vọng",
                "giai_thich": "Encouraging (tính từ) nghĩa là mang lại niềm hy vọng, sự khuyến khích.",
                "mon_hoc": "Tiếng Anh IELTS",
                "chuong": "Từ vựng IELTS Band 5.5 - 6.0"
            },
            {
                "id": 2,
                "cau_hoi": "Từ vựng IELTS Band 5.5 - 6.0: Chọn từ phù hợp: 'Education plays a _____ role in society.'",
                "dap_an": ["significant", "useless", "tiny", "bad"],
                "dap_an_dung": "significant",
                "giai_thich": "Significant (tính từ) nghĩa là có ý nghĩa quan trọng.",
                "mon_hoc": "Tiếng Anh IELTS",
                "chuong": "Từ vựng IELTS Band 5.5 - 6.0"
            }
        ]

def lay_danh_sach_ngu_phap_va_thi(band="Band 5.5 - 6.0"):
    """Trả về bài tập Ngữ Pháp & Các Thì Tiếng Anh phân loại theo Band điểm."""
    if "4.5" in band or "5.0" in band:
        return [
            {
                "id": 1,
                "cau_hoi": "Thì Tiếng Anh (Band 4.5 - 5.0): Cho câu 'Every day, she _____ to school by bus.' Điền thì Present Simple:",
                "dap_an": ["goes", "went", "is going", "has gone"],
                "dap_an_dung": "goes",
                "giai_thich": "Dấu hiệu 'Every day' dùng thì Hiện tại đơn. Chủ ngữ 'she' số ít chia 'goes'.",
                "mon_hoc": "Tiếng Anh IELTS",
                "chuong": "Các Thì Tiếng Anh Cơ Bản"
            },
            {
                "id": 2,
                "cau_hoi": "Thì Tiếng Anh (Band 4.5 - 5.0): Cho câu 'Yesterday, they _____ a new film.' Điền thì Past Simple:",
                "dap_an": ["watched", "watch", "are watching", "will watch"],
                "dap_an_dung": "watched",
                "giai_thich": "Dấu hiệu 'Yesterday' dùng thì Quá khứ đơn (V2/ed -> watched).",
                "mon_hoc": "Tiếng Anh IELTS",
                "chuong": "Các Thì Tiếng Anh Cơ Bản"
            }
        ]
    elif "6.5" in band or "7.0" in band:
        return [
            {
                "id": 1,
                "cau_hoi": "Ngữ pháp IELTS (Band 6.5 - 7.0): Cho câu 'She _____ English for 5 years before moving to London.' Điền Past Perfect:",
                "dap_an": ["had studied", "has studied", "studies", "will study"],
                "dap_an_dung": "had studied",
                "giai_thich": "Quá khứ hoàn thành (had + V3) diễn tả hành động xảy ra trước 1 mốc thời gian/hành động trong quá khứ.",
                "mon_hoc": "Tiếng Anh IELTS",
                "chuong": "Ngữ Pháp Nâng Cao"
            },
            {
                "id": 2,
                "cau_hoi": "Ngữ pháp IELTS (Band 6.5 - 7.0): Chọn câu đảo ngữ đúng cấu trúc:",
                "dap_an": [
                    "Not only did he arrive late, but he also forgot the key.",
                    "Not only he arrived late, but he also forgot the key.",
                    "Not only does he arrived late, but he also forgot the key.",
                    "Not only has he arrive late, but he also forgot the key."
                ],
                "dap_an_dung": "Not only did he arrive late, but he also forgot the key.",
                "giai_thich": "Cấu trúc đảo ngữ với 'Not only': Not only + Trợ động từ + S + V-bare...",
                "mon_hoc": "Tiếng Anh IELTS",
                "chuong": "Đảo Ngữ Inversion"
            }
        ]
    elif "7.5" in band or "8.5" in band:
        return [
            {
                "id": 1,
                "cau_hoi": "Ngữ pháp IELTS (Band 7.5 - 8.5+): Cho câu 'Had it not been for your help, we _____ in time.'",
                "dap_an": [
                    "would not have finished",
                    "will not finish",
                    "did not finish",
                    "would not finish"
                ],
                "dap_an_dung": "would not have finished",
                "giai_thich": "Đảo ngữ câu điều kiện loại 3: Had it not been for + N, S + would have + V3/ed.",
                "mon_hoc": "Tiếng Anh IELTS",
                "chuong": "Cấu Trúc Ngữ Pháp Chuyên Sâu"
            }
        ]
    else:
        # Band 5.5 - 6.0
        return [
            {
                "id": 1,
                "cau_hoi": "Ngữ pháp IELTS (Band 5.5 - 6.0): Chuyển sang bị động: 'They build a new school every year.'",
                "dap_an": [
                    "A new school is built every year.",
                    "A new school was built every year.",
                    "A new school is building every year.",
                    "A new school has built every year."
                ],
                "dap_an_dung": "A new school is built every year.",
                "giai_thich": "Bị động thì Hiện tại đơn: S + am/is/are + V3/ed.",
                "mon_hoc": "Tiếng Anh IELTS",
                "chuong": "Cấu Trúc Bị Động"
            }
        ]

def lay_bai_doc_ielts_reading(band="Band 5.5 - 6.0"):
    """Trả về các bài đọc hiểu IELTS Reading phân loại theo Band điểm."""
    passage_text = f"IELTS Reading Passage ({band}): Renewable energy sources such as solar and wind power play a key role in reducing carbon emissions worldwide."
    return [
        {
            "id": 1,
            "cau_hoi": f"{passage_text}\n\nQuestion 1: What is the main benefit of solar and wind power mentioned in the text?",
            "dap_an": [
                "Reducing carbon emissions worldwide.",
                "Making electricity completely free.",
                "Replacing all cars immediately.",
                "Creating colder winters."
            ],
            "dap_an_dung": "Reducing carbon emissions worldwide.",
            "giai_thich": "Đoạn văn nêu rõ: 'play a key role in reducing carbon emissions worldwide.'",
            "mon_hoc": "Tiếng Anh IELTS",
            "chuong": f"Reading Passage ({band})"
        }
    ]

def lay_bai_nghe_ielts_listening(band="Band 5.5 - 6.0"):
    """Trả về các bài tập luyện nghe IELTS Listening với kịch bản âm thanh TTS ẩn hoàn toàn khỏi màn hình."""
    script_text_1 = "Hello, welcome to City Central Library. My name is David Miller, and my phone number is 0912-345-678. I am registering for a library card."
    script_text_2 = "The university library opens from 8 AM to 9 PM from Monday to Friday, and 9 AM to 5 PM on Saturday."

    return [
        {
            "id": 1,
            "is_listening": True,
            "script_audio": script_text_1,
            "cau_hoi": f"IELTS Listening Test ({band}) - Question 1: What is the full name and phone number of the library card applicant?",
            "dap_an": [
                "David Miller - Phone: 0912-345-678",
                "John Smith - Phone: 0987-654-321",
                "Michael Brown - Phone: 0900-111-222",
                "David Miller - Phone: 0912-000-111"
            ],
            "dap_an_dung": "David Miller - Phone: 0912-345-678",
            "giai_thich": f"Nội dung âm thanh kịch bản bài nghe: '{script_text_1}'",
            "mon_hoc": "Tiếng Anh IELTS",
            "chuong": f"Listening Test ({band})"
        },
        {
            "id": 2,
            "is_listening": True,
            "script_audio": script_text_2,
            "cau_hoi": f"IELTS Listening Test ({band}) - Question 2: What are the opening hours of the university library on Saturday?",
            "dap_an": [
                "9 AM to 5 PM",
                "8 AM to 9 PM",
                "8 AM to 5 PM",
                "10 AM to 4 PM"
            ],
            "dap_an_dung": "9 AM to 5 PM",
            "giai_thich": f"Nội dung âm thanh kịch bản bài nghe: '{script_text_2}'",
            "mon_hoc": "Tiếng Anh IELTS",
            "chuong": f"Listening Test ({band})"
        }
    ]

def lay_de_thi_ielts_tong_hop(band="Band 5.5 - 6.0"):
    """Trả về bộ đề thi thử tổng hợp tất cả các phần theo Band điểm target."""
    ds_tu_vung = lay_danh_sach_tu_vung_ielts(band)
    ds_ngu_phap = lay_danh_sach_ngu_phap_va_thi(band)
    ds_doc = lay_bai_doc_ielts_reading(band)
    ds_nghe = lay_bai_nghe_ielts_listening(band)
    
    de_tong_hop = ds_tu_vung + ds_ngu_phap + ds_doc + ds_nghe
    for idx, item in enumerate(de_tong_hop):
        item["id"] = idx + 1
        item["cau_so"] = idx + 1
        item["nguon"] = f"Bộ Đề Thi IELTS Tổng Hợp ({band})"
    
    return de_tong_hop
