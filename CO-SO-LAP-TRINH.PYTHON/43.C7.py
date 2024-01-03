#Bài 43: Nhập vào một chuỗi, hãy đếm xem trong chuỗi có bao nhiêu từ (quy định là chuỗi không có ký tự đặc biệt, không số, không có dấu câu, chỉ có ký tự chữ và khoảng trắng)
str=input()
chuoi=str.split()
dem=0
for i in chuoi:
    if i.isalpha():
        dem+=1
print(dem)
