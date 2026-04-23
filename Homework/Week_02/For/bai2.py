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

a = 10
b = 0

while a > b:
    a = int(input("Nhap vao so thu nhat: "))
    b = int(input("Nhap vao so thu 2 lon hon so thu nhat:"))

for i in range(a,b+1):
    if is_prime(int(i)):
        print(i,end=" ")