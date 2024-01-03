#Viết hàm đưa vào 1 list số nguyên L và 1 số nguyên dương a. Hãy tính và trả về giá trung bình của a phần tử đầu tiên trong L
def nhap():
    n=int(input('n='))
    L=[]
    a=int(input('a='))
    
    for i in range(1,n+1):
        k=int(input())
        L.append(k)
    return L,a
def tinhtrungbinh(a):
    tbc=0
    for i in range(1,a+1):
        tbc+=i
    
    return tbc/i
def inkq(kq):
    print('Trung binh cua',a,"so dau tien la",kq)
L,a=nhap()
kq=tinhtrungbinh(a)
inkq(kq)
