def nhap():
    L=[]
    x=int(input('x='))
    for i in range(10):
        a=int(input())
        L.append(a)
    return L,x
def thahthe(L,x):
    for i in range(len(L)):
        if L[i]==5:
            L[i]=x
    print(L)
    
L,x=nhap()
thahthe(L,x)
