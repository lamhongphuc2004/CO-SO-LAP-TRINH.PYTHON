# Nhập từ bàn phím 2 số nguyên x,k
# Nhập một số nguyên n và n số nguyên lưu vào list L
# Xây dựng các hàm sau, thực hiện gọi hàm để trở thành các chương trình hoàn chỉnh
# bài 2. Hàm search(L,x) tìm x trong list L, nếu tìm thấy thì trả về index của x trong L , còn lại trả về none
def nhap():
    x=int(input('x='))
    k=int(input('k='))
    n=int(input('n='))
    L=[]
    for i in range(n):
        a=int(input())
        L.append(a)
    return x,k,L
def search(L,x):
    for i in range(len(L)):
        if L[i]==x:
            return i
    return None
def inkq(kq):
    print("so chi muc cua",x,"la",kq)
    
x,k,L=nhap()
kq=search(L,x)
inkq(kq)