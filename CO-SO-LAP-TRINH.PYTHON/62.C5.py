#.  Nhập  vào  một  list  số  nguyên  L,  hãy  kiểm  tra  xem  L  có  phải  là  một  cấp  số  cộng  hay  không?  Nếu  có  thì  tìm  và  in  ra  công  sai,  nếu  không  có  thì  in  ra  None.
def nhap():
    n=int(input('n='))
    L=[]
    for i in range(1,n+1):
        a=int(input())
        L.append(a)
    return L
def csc(L):
    if len(L)<2:
        return None
    else:
        congsai=L[1]-L[0]
        for i in range(2,len(L)):
            if L[i]-L[i-1] != congsai:
                return None
        return congsai
def inkq(kq):
    if kq:
        print("Cong sai la:",kq)
    else:
        print("None")
L=nhap()
kq=csc(L)
inkq(kq)
    
