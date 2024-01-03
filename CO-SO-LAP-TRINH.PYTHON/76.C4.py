#Viết hàm đưa vào 1 list số nguyên, tìm và trả về vị trí có giá trị lớn nhất trong list.
def nhap():
    n=int(input('n='))
    L=[]
    for i in range(n):
        a=int(input())
        L.append(a)
    return L
def SLN(L):
    if not L:
        return False
    vitri=0
    LN=L[0]
    
    for i in range(1,len(L)):
        if L[i] > LN:
            LN=L[i]
            vitri=i
    return vitri
def inkq(kq):
    print("Vi tri của gia tri lon nhat la",kq)
L=nhap()
vitri=SLN(L)
kq=vitri
inkq(kq)
        