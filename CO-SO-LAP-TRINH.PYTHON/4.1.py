# - Hàm nhap()  Nhập liên tục từ bàn phím n số nguyên . Đếm mà in lên màn hình có bao nhiêu chữ số chẵn được nhập vào
# - Hàm nhapvadem(n)
# - Hàm Inkq(kq)
def nhap():
    n=int(input('n='))
    return n
def NhapvaDem(n):
    dem=0
    print('Nhap',n,'so nguyen:')
    for i in range(n):
       
        num=int(input())
        if num%2==0:
            dem+=1
    return dem
def InkQ(kq):
    print('So chu so chan la:',kq)

n=nhap()
dem=NhapvaDem(n)

kq=dem
InkQ(kq)