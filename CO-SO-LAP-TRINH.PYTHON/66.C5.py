# Nhập  vào  một  list  số  nguyên  L,  hãy  đếm  số  lượng  giá  trị  trong  list  thỏa  tính  chất:  “lớn  hơn  tất  cả  các  giá  trị  đứng  đằng  trước  nó”.
def dem_gia_tri_lon_hon_truoc(L):
    count = 0
    max_value = float('-inf')  # Giá trị lớn nhất ban đầu, giả sử âm vô cùng

    for num in L:
        if num > max_value:
            count += 1
            max_value = num

    return count

# Nhập danh sách từ người dùng
L = [int(x) for x in input("Nhập danh sách các số nguyên, cách nhau bởi dấu cách: ").split()]

# Gọi hàm để đếm số lượng giá trị thỏa tính chất
so_luong = dem_gia_tri_lon_hon_truoc(L)

print("Số lượng giá trị thỏa tính chất: ", so_luong)
