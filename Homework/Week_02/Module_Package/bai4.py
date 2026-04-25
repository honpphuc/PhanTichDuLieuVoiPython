s = input("Nhap vao mot chuoi S: ")
d = {}

for char in s:
    if char in d:
        d[char] += 1
    else:
        d[char] = 1

print("Tu dien ket qua:", d)