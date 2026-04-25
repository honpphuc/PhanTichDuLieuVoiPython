d = {}
n = int(input("Nhap so luong phan tu: "))
for i in range(n):
    key = input(f"Nhap key thu {i+1}: ")
    val = int(input(f"Nhap gia tri so nguyen cho '{key}': "))
    d[key] = val

top_3 = sorted(d.values(), reverse=True)[:3]
print("3 gia tri lon nhat la:", top_3)