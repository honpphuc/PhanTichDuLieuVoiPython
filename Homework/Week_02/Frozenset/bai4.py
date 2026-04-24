students = []

print("Nhap ho va ten sinh vien (Bam Enter sau dong trong de ket thuc):")
while True:
    full_name = input().strip()
    if full_name == "":
        break
    students.append(full_name)

print("\n--- Ket qua tach ho va ten ---")
for name in students:
    parts = name.split()
    if len(parts) >= 2:
        ho = parts[0]
        ten = parts[-1]
        print(f"Ho: {ho:10} | Ten: {ten}")
    else:
        # Trường hợp tên chỉ có 1 từ
        print(f"Ho/Ten {name}")