def nhap_dict(ten):
    d = {}
    n = int(input(f"Nhap so luong phan tu cho {ten}: "))
    for i in range(n):
        k = input(f"Nhap key: ")
        v = int(input(f"Nhap value (so): "))
        d[k] = v
    return d

print("Nhap tu dien A:")
a = nhap_dict("A")
print("Nhap tu dien B:")
b = nhap_dict("B")

c = {}
tat_ca_keys = set(a.keys()) | set(b.keys())

for k in tat_ca_keys:
    if k in a and k in b:
        c[k] = max(a[k], b[k])
    elif k in a:
        c[k] = a[k]
    else:
        c[k] = b[k]

print("Tu dien C sau khi hop nhat:", c)