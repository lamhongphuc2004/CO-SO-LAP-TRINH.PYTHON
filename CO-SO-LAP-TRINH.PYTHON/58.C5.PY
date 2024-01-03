#Nhập  vào  một  list  số  nguyên  L,  nhập  vào  số  nguyên  x,  tìm  giá  trị  trong  list  xa  x  nhất.
def nhap():
    n=int(input('n='))
    x=int(input('x='))
    L=[]
    for i in range(1,n+1):
        a=int(input())
        L.append(a)
    return L,x
def soxanhat(x,L):
    kq=None
    for i in L:
        if kq==None or abs(kq-x) < abs(i-x):
            kq=i
           
    return kq
def inkq(kq):
    print("Gia tri trong list xa x nhat",kq)
x,L=nhap()
kq=soxanhat(L,x)
inkq(kq)

            
