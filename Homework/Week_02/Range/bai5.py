n = int(input("Nhap so dong n: "))

pascal = []

for i in range(n):
    row = [1]
    
    if pascal:
        last_row = pascal[-1]
        for j in range(len(last_row) - 1):
            row.append(last_row[j] + last_row[j+1])
        row.append(1)
    
    pascal.append(row)

for i in range(n):
    print(" " * (n - i), end="")
    for val in pascal[i]:
        print(val, end=" ")
    print()