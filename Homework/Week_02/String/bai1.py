chuoi = input("Nhap vao chuoi de kiem tra: ")

if chuoi.endswith("!!!"):
    print("Chuoi co ket thuc bang \"!!!\"")
else:
    chuoi += "!!!"
    print(f"Chuoi da duoc them \"!!!\": {chuoi}")