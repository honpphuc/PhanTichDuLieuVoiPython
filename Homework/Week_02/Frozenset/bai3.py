input_data = input("Nhap cac so cach nhau boi dau cach: ")

numbers_set = set(map(int, input_data.split()))

count = len(numbers_set)
max_val = max(numbers_set)
min_val = min(numbers_set)

print(f"Tập hợp các số bạn đã nhập (không trùng): {numbers_set}")
print(f"Số lượng phần tử trong tập: {count}")
print(f"Giá trị lớn nhất: {max_val}")
print(f"Giá trị nhỏ nhất: {min_val}")