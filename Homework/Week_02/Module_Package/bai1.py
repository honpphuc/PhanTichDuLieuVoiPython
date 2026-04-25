d = {}
n = int(input("Nhap so luong phan tu cho tu dien D: "))
for i in range(n):
    key = input(f"Nhap key thu {i+1}: ")
    val = input(f"Nhap gia tri (cach doc tieng Anh) cho '{key}': ")
    d[key] = val

sorted_values = sorted(d.values())
print("Ket qua value tang dan:", sorted_values)