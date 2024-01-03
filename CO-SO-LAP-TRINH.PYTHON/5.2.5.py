# Nhập từ bàn phím 2 số nguyên x,k
# Nhập một số nguyên n và n số nguyên lưu vào list L
# Xây dựng các hàm sau, thực hiện gọi hàm để trở thành các chương trình hoàn chỉnh
# bài 5. Hàm replace(L,x,y) tìm tất cả các phần tử có giá trị bằng x trong list L và thay thế bằng y
def nhap():
    n=int(input('n='))
    x=int(input('x='))
    y=int(input('y='))
    L=[]
    for i in range(1,n+1):
        a=int(input())
        L.append(a)
    return x,y,L
def replace(L,x,y):
    for i in range(len(L)):
        if L[i]==x:
            L[i]=y
    return L
def inkq(kq):
    print(kq)

x,y,L=nhap()
kq=replace(L,x,y)
inkq(kq)