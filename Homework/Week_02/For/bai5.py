numbers = []

while True:
    n = int(input("Nhap so: "))

    if n == 0:
        break

    numbers.append(n)

print(f" Danh sach cac phan tu: {numbers}")

print(f"So lon nhat la: {max(*numbers)}")

print(f"So nho nhat la: {min(*numbers)}")