#Nhập  vào  một  list  số  nguyên  L,  hãy  sắp  xếp  list  L  theo  thứ  tự  từ  bé  đến  lớn.
def nhap():
    n=int(input('n='))
    L=[]
    for i in range(1,n+1):
        a=int(input())
        L.append(a)
    return L
def sapxep(L):
    for j in range(len(L)-1):
        for i in range(len(L)-1-j):
            if L[i]>L[i+1]:
                L[i],L[i+1]=L[i+1],L[i]
    return L
def inkq(kq):
    print(kq)
L=nhap()
kq=sapxep(L)
inkq(kq)