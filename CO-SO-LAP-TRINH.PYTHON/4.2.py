# Viết chương trình có sử dụng hàm, thực hiện nhập từ bàn phím một số nguyên n(2<=n<=100).
#Cho biết n có phải là số nguyên tố hay không. Biết rằng, n là số nguyên tố nếu n chỉ chia hết cho 2 và chính nó
#Yêu cầu sử dụng tối thiểu 3 hàm
def Nhap():
    n=int(input('n='))
    return n 
def LaSNT(n):
    if n<2:
        return False
    for i in range(2,int((n*0.5))+1):
        if n%i==0:
            return False
    return True
def Inkq(kq):
    if kq:
        print(n,"la SNT")
    else:
        print(n,"khong phai la SNT")
n=Nhap()
kq=LaSNT(n)
Inkq(kq)