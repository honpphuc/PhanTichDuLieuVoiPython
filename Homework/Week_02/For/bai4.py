import math
from functools import reduce

numbers = []

while True:
    n = int(input("Nhap vao so: "))
    if n <= 0:
        break
    numbers.append(n)

if numbers:
    ucln = math.gcd(*numbers)
    bcnn = reduce(lambda a, b: abs(a * b) // math.gcd(a, b), numbers)
    print(f"UCLN = {ucln}")
    print(f"BCNN = {bcnn}")
else: print("Chuoi rong!")