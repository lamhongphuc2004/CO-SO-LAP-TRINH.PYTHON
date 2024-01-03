#Nhập  vào  một  list  số  nguyên  L,  Hãy  tìm  và  in  ra  một  vị  trí  trong  L  thỏa  hai  điều  kiện:  có  hai  giá  trị  lân  cận  và  giá  trị  tại  vị  trí  đó  bằng  tích  hai  giá  trị  lân  cận.  Nếu  L  không  tồn  tại  giá  trị  như  vậy  thì  in  ra  –  1.
def nhap():
    n=int(input('n='))
    L=[]
    for i in range(1,n+1):
        a=int(input())
        L.append(a)
    return L
def gtri(L):
    for i in range(len(L)):
        if L[i]==L[i-1]*L[i+1]:
            return i
    else:
        return -1
def inkq(kq):
    print("So co gia tri dac biet la",kq)
L=nhap()
kq=gtri(L)
inkq(kq)