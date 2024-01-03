# Nhập từ bàn phím 2 số nguyên x,k
# Nhập một số nguyên n và n số nguyên lưu vào list L
# Xây dựng các hàm sau, thực hiện gọi hàm để trở thành các chương trình hoàn chỉnh
# bài 4. Hàm count(L) trả về số lượng phần tử trong list L
def nhap():
    x=int(input('x='))
    k=int(input('k='))
    n=int(input('n='))
    L=[]
    for i in range(n):
        a=int(input())
        L.append(a)
    return x,k,L
def count(L):
    dem=0
    for i in L:
        dem+=1
    return dem
def inkq(kq):
    print("So phan tu trong list la",kq)
x,k,L=nhap()
kq=count(L)
inkq(kq)
    