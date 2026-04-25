last_val = None
same_count = 0
even_count = 0

while True:
    try:
        s = input("Nhap mot so nguyen duong: ")
        
        try:
            n = int(s)
        except ValueError:
            raise Exception("Loi nhap so")
            
        if n == 0:
            break
            
        if n < 0:
            raise Exception("Loi so am!!!")
            
        if n == last_val:
            same_count += 1
        else:
            last_val = n
            same_count = 1
            
        if n % 2 == 0:
            even_count += 1
        else:
            even_count = 0
            
        if same_count == 4:
            same_count = 0
            last_val = None
            raise Exception("Loi nhap lap")
            
        if even_count == 5:
            even_count = 0
            raise Exception("Loi nhap chan")
            
    except Exception as e:
        print(e)