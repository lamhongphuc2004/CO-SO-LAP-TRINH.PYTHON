def tim_chuoi_dai_nhat_va_so_nho_nhat(L):
    chuoi_lon_nhat = ""
    so_nho_nhat = None

    for item in L:
        if type(item) == str:
            if len(item) > len(chuoi_lon_nhat):
                chuoi_lon_nhat = item
        elif type(item) == int:
            if so_nho_nhat is None or item < so_nho_nhat:
                so_nho_nhat = item

    return chuoi_lon_nhat, so_nho_nhat

# Nhập danh sách từ người dùng
L = input("Nhập danh sách các chuỗi và số nguyên, cách nhau bởi dấu cách: ").split()

# Chuyển các phần tử là số nguyên từ chuỗi sang kiểu int
for i in range(len(L)):
    if L[i].isdigit():
        L[i] = int(L[i])

# Gọi hàm để tìm chuỗi có độ dài lớn nhất và số nguyên có giá trị nhỏ nhất
chuoi_dai_nhat, so_nho_nhat = tim_chuoi_dai_nhat_va_so_nho_nhat(L)

print("Chuỗi có độ dài lớn nhất: ", chuoi_dai_nhat)
print("Số nguyên có giá trị nhỏ nhất: ", so_nho_nhat)
