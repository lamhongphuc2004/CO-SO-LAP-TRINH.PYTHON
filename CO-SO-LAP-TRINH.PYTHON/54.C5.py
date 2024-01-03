#Nhập  vào  một  list  số  nguyên  L,  nhập  vào  2  số  nguyên  dương  a  và  b  (a  <  b  <  len(L))
#Tìm  và  in  ra  số  nhỏ  nhất  trong  list  từ  vị  trí  a  đến  vị  trí  b.
def nhap():
    n=int(input('n='))
    a=int(input('a='))
    b=int(input('b='))
    L=[]
    for i in range(1,n+1):
        k=int(input())
        L.append(k)
    return a,b,L
def sonhonhat(a,b,L):
    if len(L)==0:
        return None
    else:
        NN=L[a]
        for i in range (int(L[a]),int(L[b])+1):
            if i<NN:
                NN=i
        return NN
def inkq(kq):
    print("So nho nhat tỏng khoang",a,"den",b,"la",kq)
a,b,L=nhap()
kq=sonhonhat(a,b,L)
inkq(kq)
        