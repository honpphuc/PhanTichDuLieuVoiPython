words = input("Nhap vao cac tu: ").split()

if words:
    max_len = max(len(w) for w in words)
    longest = [w for w in words if len(w) == max_len]
    print(f"Do dai tu lon nhat la: {max_len}")
    print(f"Cac tu co do dai lon nhat la: {', '.join(longest)}")