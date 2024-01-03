# Nhập vào 1 list số nguyên L,tính giá trị trung bình của list L
def nhap():
    n=int(input('n='))
    L=[]
    for i in range(1,n+1):
        a=int(input())
        L.append(a)
    return L
def trungbinh(L):
    sum=0
    for i in range((len(L))):
        sum+=i
    return sum/i
def inkq(kq):
    print('Trung binh',kq,round(1,1))
L=nhap()
kq=trungbinh(L)
inkq(kq)