#Viết chương trình:
#- Nhập vào một chuỗi gồm các từ được phân tách bởi dấu phẩy;
#- Chương trình thực hiện loại bỏ các từ trùng lắp, sau đó sắp xếp các từ theo thứ tự bảng chữ cái, phân
#tách nhau bởi dấu phẩy rồi in kết quả ra màn hình.
def remove_duplicates_and_sort(chuoi):
    # Chuyển đổi chuỗi thành danh sách các từ
    tu = chuoi.split(",")

    # Loại bỏ các từ trùng lắp
    tu_duy_nhat= []
    for word in tu:
        if word not in tu_duy_nhat:
            tu_duy_nhat.append(word)

    # Sắp xếp các từ theo thứ tự bảng chữ cái
    for i in range(len(tu_duy_nhat) - 1):
        for j in range(i + 1, len(tu_duy_nhat)):
            if tu_duy_nhat[i] > tu_duy_nhat[j]:
                tu_duy_nhat[i], tu_duy_nhat[j] = tu_duy_nhat[j], tu_duy_nhat[i]

    # Ghép các từ thành chuỗi mới, phân tách nhau bởi dấu phẩy
    kq = ""
    for i in range(len(tu_duy_nhat)):
        kq += tu_duy_nhat[i]
        if i != len(tu_duy_nhat) - 1:
            kq += ", "

    return kq

chuoi = input("Nhập vào chuỗi các từ, phân tách bởi dấu phẩy: ")

# Xử lý chuỗi và in kết quả
output_string = remove_duplicates_and_sort(chuoi)
print("Kết quả:", output_string)
