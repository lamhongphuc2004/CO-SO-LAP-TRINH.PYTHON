#Nhập  vào  một  list  số  nguyên  L,  hãy  biến  đổi  L  bằng  cách  thay  đổi  vị  trí  giữa  giá  trị  nhỏ  nhất  và  lớn  nhất
def nhap():
    n=int(input('n='))
    L=[]
    for i in range(n):
        a=int(input())
        L.append(a)
    return L

def doivitri(L):
    vtr_max=max(L)
    vtr_min=min(L)
    
    chisomuc_max=L.index(vtr_max)
    chisomuc_min=L.index(vtr_min)
    
    L[chisomuc_max],L[chisomuc_min]=L[chisomuc_min],L[chisomuc_max]
    return L
def inkq(kq):
    print('Ket qua sau khi doi vi tri la:',kq)

L=nhap()
kq=doivitri(L)
inkq(kq)
    