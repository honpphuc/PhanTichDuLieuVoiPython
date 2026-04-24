string = input("Moi nhap chuoi: ")

words = string.split()

words.sort()

print("Cac tu sau khi sap xep:")
for i in words:
    print(i)