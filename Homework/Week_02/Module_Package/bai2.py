d = {}
n = int(input("Nhap so luong phan tu: "))
for i in range(n):
    key = input(f"Nhap key thu {i+1}: ")
    val = input(f"Nhap gia tri cho '{key}': ")
    d[key] = val

unique_values = list(set(d.values()))
print("Cac gia tri khac nhau trong tu dien:", unique_values)