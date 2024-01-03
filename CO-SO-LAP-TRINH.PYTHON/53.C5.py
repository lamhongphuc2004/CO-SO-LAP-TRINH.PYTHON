#.  Nhập  vào  một  list  số  nguyên  L,  tìm  và  in  ra  giá  trị  lớn  nhất  trong  L.
def find_max_value(numbers):
    if len(numbers) == 0:
        print("List số nguyên trống.")
    else:
        max_value = max(numbers)
        print("Giá trị lớn nhất trong List là:", max_value)

# Nhập list số nguyên từ bàn phím
n = int(input("Nhập số phần tử của list: "))
L = []
for i in range(n):
    num = int(input("Nhập số nguyên thứ {}: ".format(i+1)))
    L.append(num)

# Tìm và in ra giá trị lớn nhất trong list
find_max_value(L)
