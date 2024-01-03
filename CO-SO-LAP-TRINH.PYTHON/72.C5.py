#Nhập vào một list L có các phần tử là chuỗi. Hãy tìm ra chuỗi có vị trí ký tự in hoa lớn nhất
L=input("Nhập vào L:")
L=L.split(",")
chuoi_kq=None
vtr_max=None
for i in L:
    kq = -1
    for j in range(len(i)):
        if i[j].isupper():
            kq=i
    if chuoi_kq==None or vtr_max < kq:
        chuoi_kq=i
        vt_max=kq
print(chuoi_kq)      