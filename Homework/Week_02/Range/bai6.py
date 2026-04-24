n = int(input("Nhap so nguyen n: "))

fib_list = []
a, b = 0, 1

while a < n:
    fib_list.append(a)
    a, b = b, a + b

print(f"Danh sach cac so Fibonacci nho hon {n}:")
print(fib_list)