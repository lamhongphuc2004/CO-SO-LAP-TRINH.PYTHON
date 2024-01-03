# Viết chương trình nhập vào 3 số a,b,c cho biết số lớn nhất trong 3 số:
# Hàm nhap() thực hiện việc nhậo vào 3 số nguyên a,b,c
# Hàm max3(a,b,c) thực hiện việc tìm và trả về qua tên hàm số lớn nhất trong 3 sốa,b,c
# Hàm inkq(kq) thực hiện in lên màn hình kết quả số lớn nhất theo mẫu sau
def nhap():
    a=int(input('Nhap 3 so nguyen:\na='))
    b=int(input('b='))
    c=int(input('c='))
    return a,b,c
def max3(a,b,c):
    SLN=None
    if b>a and b>c:
        SLN=b
    elif c>b and c>a:
        SLN=c
    else:
        SLN=a
    return SLN
def inkq(kq):
    print('So lon nhat trong 3 so la',kq)
a,b,c=nhap()
SLN=max3(a,b,c)    
kq=SLN
inkq(kq)
