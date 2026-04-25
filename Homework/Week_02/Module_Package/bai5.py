# Nhap du lieu gia (prices)
prices = {}
n = int(input("Nhap so luong loai trai cay: "))
for i in range(n):
    name = input(f"Nhap ten loai thu {i+1}: ")
    p = float(input(f"Nhap gia cua {name}: "))
    prices[name] = p


stock = {}
print("--- Nhap so luong ton kho ---")
for name in prices:
    qty = int(input(f"Nhap so luong ton kho cua {name}: "))
    stock[name] = qty

total_val = {}
for name in prices:
    total_val[name] = prices[name] * stock.get(name, 0)

ket_qua = sorted(total_val.items(), key=lambda x: x[1], reverse=True)

print("Ket qua (Ten - Tong gia tri):")
for name, total in ket_qua:
    print(f"{name}: {total}")