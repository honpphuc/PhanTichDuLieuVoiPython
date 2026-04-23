def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return  True
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    i = 5
    while i*i <= n:
        if n % i == 0 or n % (i+2) == 0:
            return False
        i += 6
        return True

n = int(input("Nhap vao so can kiem tra: "))
check = is_prime(n)

if is_prime:
    print(f"{n} la so nguyen to")
else:
    print(f"{n} khong phai so nguyen to")