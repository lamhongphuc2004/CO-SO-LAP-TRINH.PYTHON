#Người  ta  định  nghĩa  một  list  số  nguyên  được  gọi  là  “dạng  sóng”  khi  tất  cả  các  phần  tử  đều  lớn  hơn  hoặc  nhỏ  hơn  hai  phần  tử  xung  quanh  nó.
#Nhập  vào  một  list  số  nguyên  L  và  kiểm  tra  xem  L  có  phải  là  list  “dạng  sóng”  hay  không,  nếu  có  thì  ta  in  ra  True,  không  có  thì  ta  in  False.
def nhap():
    n=int(input('n='))
    L=[]
    for i in range(1,n+1):
        a=int(input())
        L.append(a)
    return L
def dangsong(L):
    for i in range(len(L)+1):
        if L[i-1]<L[i]>L[i+1] or (L[i]<L[i-1] and L[i]<L[i+1]):
            return True
    return False
def inkq(kq):
    print(kq)
L=nhap()
kq=dangsong(L)
inkq(kq)