# Thu muc: xu_ly_tro_choi
# File: quan_ly_checkpoint.py
# Mo ta: Module quan ly va tinh toan diem Checkpoint 5 man choi cho cac minigames va xuat phat lai khi thua

def tinh_man_checkpoint_gan_nhat(so_man_hien_tai):
    """
    Tinh man Checkpoint gan nhat ma nguoi choi da dat duoc.
    Quy tac: Cu 5 man se co 1 diem Checkpoint (Man 1, 6, 11, 16, 21, 26,...).
    Vi du: Nguoi choi dang o Man 7 ma bi thua, se quay lai xuat phat tu Man 6.
    """
    so_man = max(1, int(so_man_hien_tai))
    man_checkpoint = ((so_man - 1) // 5) * 5 + 1
    return man_checkpoint

def is_checkpoint_5_man(so_man):
    """
    Kiem tra mot man choi co phai la diem Checkpoint 5 man hay khong.
    Diem Checkpoint la cac man hoan thanh 5, 10, 15, 20... hoac xuat phat 1, 6, 11...
    """
    so_man = int(so_man)
    return (so_man % 5 == 0)

def lay_danh_sach_cac_man_checkpoint(so_man_max=100):
    """
    Tra ve danh sach tat ca cac man la diem Checkpoint xuat phat tu 1 den so_man_max.
    """
    danh_sach = []
    for m in range(1, so_man_max + 1, 5):
        danh_sach.append(m)
    return danh_sach
