def sieve_of_eratosthenes(limit):
    is_prime = [True] * limit
    is_prime[0] = is_prime[1] = False
    
    for p in range(2, int(limit**0.5) + 1):
        if is_prime[p]:
            for i in range(p * p, limit, p):
                is_prime[i] = False
    
    return [num for num, prime in enumerate(is_prime) if prime]

print("Đang tính toán các số nguyên tố nhỏ hơn 1.000.000...")
P = tuple(sieve_of_eratosthenes(1000000))

print(f"Đã tạo xong tuple P. Số lượng số nguyên tố tìm được: {len(P)}")
print("10 số đầu tiên trong P:", P[:10])