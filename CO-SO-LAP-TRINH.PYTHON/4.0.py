# Cho 2 số nguyên a,b tìm tất cả các số nguyên tố trong đoạn ab
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def count_primes_in_range(a, b):
    count = 0
    for num in range(a, b + 1):
        if is_prime(num):
            count += 1
    return count

a = int(input("Nhập số nguyên dương a: "))
b = int(input("Nhập số nguyên dương b: "))

if a > b or a <= 0 or b <= 0:
    print("Nhập không hợp lệ. Vui lòng nhập lại.")
else:
    prime_count = count_primes_in_range(a, b)
    print(f"Số lượng số nguyên tố trong đoạn từ {a} đến {b} là: {prime_count}")
