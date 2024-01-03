# Viết hàm đưa vào list là phần tử các chuổi,tìm và trả về chuổi ngắn nhất
def vitrichuoi(L):
    kq=None
    for i in L:
        if kq==None or len(kq)>len(i):
            kq=i
    return kq
print(vitrichuoi(["xin chao","hello"]))



def nhap():
    n=int(input('n='))
    L=[]
    for i in range(n):
        a=input()
        L.append(a)
    return L
def chuoingannhat(L):
    NN=L[0]
    for i in L:
        if len(i)<len(NN):
            NN=i
    return NN
def inkq(kq):
    print("Chuoi co do dai ngan nhat la:",kq)
L=nhap()
kq=chuoingannhat(L)
inkq(kq)