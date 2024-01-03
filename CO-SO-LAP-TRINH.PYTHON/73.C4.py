# Viết hàm đưa vào 2 số nguyên , số nào lớn hơn thì in ra bảng cửu chương của số đó
def Nhap():
    a=int(input('a='))
    b=int(input('b='))
    return a,b
def SLN(a,b):
    max_num=a
    if b>max_num:
        max_num=b
    return max_num
def BangCC(kq):
    x=0
    if kq:
        for i in range(1,11):
            print(f"{kq}x{i}={kq*i}")
a,b=Nhap()
kq=SLN(a,b)
BangCC(kq)
            
    
    