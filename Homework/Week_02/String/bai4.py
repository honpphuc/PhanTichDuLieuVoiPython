chuoi = input("Nhap vao chuoi: ")

result = "".join(i for i in chuoi if not i.isdigit())

print(f"Ket qua: {result}")