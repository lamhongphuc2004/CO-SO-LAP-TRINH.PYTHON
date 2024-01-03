# Nhập  vào  một  list  số  nguyên  L,  hãy  kiểm  tra  xem  L  có  được  sắp  xếp  từ  bé  đến  lớn  hay  không,  nếu  có  thì  in  True,  không  có  thì  in  False.
def nhap():
    n=int(input('n='))
    L=[]
    for i in range(1,n+1):
        a=int(input())
        L.append(a)
    return L
def sapxep(L):
    
    for i in range(len(L)):
        if L[i]<L[i+1]:
            return True
            
        else:
            return False

def inkq(kq):
    print(kq)
L=nhap()
kq=sapxep(L)
inkq(kq)