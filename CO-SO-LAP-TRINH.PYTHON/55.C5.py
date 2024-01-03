#Nhập  vào  một  list  số  nguyên  L,  hãy  kiểm  tra  xem  tất  cả  các  phần  tử  trong  mảng  có  bằng  nhau  hay  không,  nếu  có  thì  in  True,  không  có  thì  in  False.
def check_all_equal(numbers):
    if len(numbers) < 2:
        return True

    first_number = numbers[0]

    for num in numbers[1:]:
        if num != first_number:
            return False

    return True

# Nhập list số nguyên từ bàn phím
n = int(input("Nhập số phần tử của list: "))
L = []
for i in range(n):
    num = int(input("Nhập số nguyên thứ {}: ".format(i+1)))
    L.append(num)

# Kiểm tra và in ra kết quả
result = check_all_equal(L)
print(result)
