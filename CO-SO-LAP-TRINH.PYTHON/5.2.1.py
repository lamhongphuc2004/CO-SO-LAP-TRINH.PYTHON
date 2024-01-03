# Nhập từ bàn phím 2 số nguyên x,k
# Nhập một số nguyên n và n số nguyên lưu vào list L
# Xây dựng các hàm sau, thực hiện gọi hàm để trở thành các chương trình hoàn chỉnh
# bài 1 .Hàm add(L,x,k) thêm phần thử x vào L tại vị trí index k, nếu k lớn hơn số phần tử của L thì thêm x vào cuối L 
def nhap():
    x=int(input('x='))
    k=int(input('k='))
    n=int(input('n='))
    L=[]
    for i in range(n):
        a=int(input())
        L.append(a)
    return x,k,L
def add(L,x,k):
    
    L=L[:k]+[x]+L[k:]
    return L
def inkq(kq):
    print(kq)
x,k,L=nhap()
kq=add(L,x,k)
inkq(kq)
    