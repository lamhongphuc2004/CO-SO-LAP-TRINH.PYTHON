# Nhập  vào  một  list  số  nguyên  L,  tìm  và  in  ra  giá  trị  dương  đầu  tiên  của  list,  nếu  không  có  giá  trị  dương,  ta  in  ra  -1
def find_first_positive(numbers):
    for num in numbers:
        if num > 0:
            return num
    return -1

# Nhập list số nguyên từ bàn phím
n = int(input("Nhập số phần tử của list: "))
L = []
for i in range(n):
    num = int(input("Nhập số nguyên thứ {}: ".format(i+1)))
    L.append(num)

# Tìm và in ra giá trị dương đầu tiên
first_positive = find_first_positive(L)
print(first_positive)
