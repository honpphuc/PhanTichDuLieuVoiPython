def tinhPhanSo():
    try:
        a = int(input("Nhap vao so a: "))
        b = int(input("Nhap vao so b: "))

        ket_qua = a / b
        print(f"Gia tri phan so {a}/{b} la: {ket_qua}")

    except ValueError:
        print("Loi: Ban phai nhap vao so nguyen!")
    except ZeroDivisionError:
        print("Loi: Mau so phai khac 0")

tinhPhanSo()