def kiemTraTamGiac():
    try:
        a = float(input("Nhap vao do dai canh a: "))
        b = float(input("Nhap vao do dai canh b: "))
        c = float(input("Nhap vao do dai canh c: "))

        if a <= 0 or b <= 0 or c <= 0:
            print("Loi: Do dai cac canh phai la so duong lon hon 0")
            return
        
        if (a + b > c) and (a + c > b) and (b + c > a):
            print(f"So do ba canh {a}, {b}, {c} tao thanh mot tam giac")
        else:
            print("So do ba canh khong the tao thanh mot tam giac")

    except ValueError:
        print("Loi: Du lieu nhap vao phai la mot so nguyen (hoac mot so thuc)")
    
kiemTraTamGiac()