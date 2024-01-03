# Nhập từ bàn phím 2 số nguyên x,k
# Nhập một số nguyên n và n số nguyên lưu vào list L
# Xây dựng các hàm sau, thực hiện gọi hàm để trở thành các chương trình hoàn chỉnh
# bài 3. Hàm delete(L,x) xoá tất cả phần tử có giá trị bằng x trong list L
def nhap():
    x=int(input('x='))
    k=int(input('k='))
    n=int(input('n='))
    L=[]
    for i in range(n):
        a=int(input())
        L.append(a)
    return x,k,L
def delete(L,x):
    if x in L:
        L.remove(x)
    return L
def inkq(kq):
    print(kq)
x,k,L=nhap()
kq=delete(L,x)
inkq(kq)