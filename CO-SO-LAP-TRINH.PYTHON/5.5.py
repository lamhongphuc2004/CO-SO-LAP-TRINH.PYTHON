# Nhập từ bàn phím một số nguyên n(n>0) , và n số nguyên lưu trử vào 1 list
# In lên màn hình 
# Số lượng các số nguyên dương
# Trung bình cộng của các số nguyên chẵn được lưu trữ trong List trên
def nhap():
    n=int(input('n='))
    L=[]
    for i in range(1,n+1):
        a=int(input())
        L.append(a)
    return L,a
def songuyenduong(L,a):
    dem=0
    tong=0
    
    for i in range(len(L)):
        if a>0:
            dem+=1
        
        if a%2==0:
            tong+=a
            dem+=1
    print(dem)
    print("Trung binh cac so:",tong/dem)
    
    
def inkq(kq):
    print(kq)
L=nhap()
kq=songuyenduong(L)
inkq(kq)



def nhap():
    n=int(input('n='))
    L=[]
    for i in range(n):
        a=int(input())
        L.append(a)
    return L
def tbc(L):
    dem=0
    tong=0
    for i in range(len(L)):
        if L[i]>0:
            dem+=1
        if L[i]%2==0:
            tong+=i
    return dem,tong/i

L=nhap()
soluong,trungbinh=tbc(L)
print('So chu so nguyen duong la:',soluong)
print("Trung binh cong:",trungbinh)