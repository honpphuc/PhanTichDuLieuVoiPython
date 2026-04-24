def tongUocSo(k):
    tong = 0
    for i in range(1, k):
        if k % i == 0:
            tong += i
    return tong


n = int(input("Moi nhap n: "))

print("Cac so doi dao nho hon", n, "la:")
for i in range(1, n):
    if tongUocSo(i) > i:
        print(i)