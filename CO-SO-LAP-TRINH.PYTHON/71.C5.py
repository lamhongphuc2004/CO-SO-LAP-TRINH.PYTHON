#Nhập vào một list L có các phần tử là chuỗi (các chuỗi này không có ký tự đặc biệt, dấu câu, ký tự số, chỉ có ký tự chữ cái và khoảng trắng)
#Hãy tìm ra vị trí của chuỗi có nhiều từ nhất
L=input()
L=L.split(",")
max=None
kq_vitri=None
for i in range(len(L)):
    x= L[i].count(" ")+1
    if max == None or max < x :
        max =x
        kq_vitri=i
print(kq_vitri)
