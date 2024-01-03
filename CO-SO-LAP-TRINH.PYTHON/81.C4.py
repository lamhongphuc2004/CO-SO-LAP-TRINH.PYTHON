# Viết hàm đưa vào 1 list số nguyên L và 1 số nguyên dương a. Hãy tìm và trả về giá trị lớn nhất thứ a trong list L(nếu a=1 thì tìm giá trị lớn nhất, a=2 thì tìm giá trị lớn nhì,...)
def nhap():
    n=int(input('n='))
    a=int(input('a='))
    L=[]
    for i in range(n):
        k=int(input())
        L.append(k)
    return L,a
def tim_gia_tri_lon_thu_a(a,L):
    if a<=0 and a>len(L):
        return None
    else:
        gtri_lon_thu_a=float()
        for i in range(a):
            GTLN=max(L)
            L.remove(GTLN)
            gtri_lon_thu_a=GTLN
        return gtri_lon_thu_a
def inkq(a,L,kq):
    print('Gia tri lon thu',a,'la:',kq)
    
L,a=nhap()
kq=tim_gia_tri_lon_thu_a(a,L)
inkq(a,L,kq)
    