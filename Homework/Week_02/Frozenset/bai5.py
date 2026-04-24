def nhap_ma_phong(ten_phong):
    s = input(f"Nhap ma nhan vien phong {ten_phong}: ")
    return set(map(int, s.split(',')))

p_ns = nhap_ma_phong("Nhan su")
p_hc = nhap_ma_phong("Hanh chinh")
p_tt = nhap_ma_phong("Truyen thong")

tat_ca = p_ns | p_hc | p_tt
print(f"Ba phong ban nay su dung: {len(tat_ca)} nhan vien")

chung_3 = p_ns & p_hc & p_tt
print(f"Danh sach ma nhan vien thuoc ca 3 phong: {list(chung_3)}")

chi_1 = (p_ns ^ p_hc ^ p_tt) - chung_3
print(f"Danh sach ma nhan vien chi thuoc 1 phong: {list(chi_1)}")

giao_ns_hc = p_ns & p_hc
giao_ns_tt = p_ns & p_tt
giao_hc_tt = p_hc & p_tt

caps = [
    ("Nhan su - Hanh chinh", len(giao_ns_hc)),
    ("Nhan su - Truyen thong", len(giao_ns_tt)),
    ("Hanh chinh - Truyen thong", len(giao_hc_tt))
]

max_chung = max(caps, key=lambda x: x[1])[1]
print("Cap phong dung chung nhieu nhan vien nhat:")
for ten, sl in caps:
    if sl == max_chung and sl > 0:
        print(f"- {ten} ({sl} nhan vien)")

print(f"Ma nhan vien dau tien phong Nhan su: {min(p_ns) if p_ns else 'Trong'}")
print(f"Ma nhan vien dau tien phong Hanh chinh: {min(p_hc) if p_hc else 'Trong'}")
print(f"Ma nhan vien dau tien phong Truyen thong: {min(p_tt) if p_tt else 'Trong'}")