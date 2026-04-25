import random

rain_data = {}
for i in range(1, 13):
    thang = f"Thang {i}"
    rain_data[thang] = [round(random.uniform(100, 4000), 2) for _ in range(20)]

print("Da tao xong du lieu luong mua ngau nhien.")
print("Vi du du lieu Thang 1:", rain_data["Thang 1"])