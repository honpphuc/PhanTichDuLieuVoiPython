def ucln(a, b):
    a = abs(a)
    b = abs(b)
    while b != 0:
        a, b = b, a % b
    return a

def bcnn(a,b):
    if a == 0 or b == 0:
        return 0
    return int(abs(a*b)/ucln(a,b))


a = int(input("Nhap vao so thu nhat: "))
b = int(input("Nhap vao so thu hai: "))

print(f"UCLN({a},{b}) = {ucln(a,b)}")
print(f"BCNN({a},{b}) = {bcnn(a,b)}")