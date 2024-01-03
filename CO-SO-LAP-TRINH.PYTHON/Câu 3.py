L=input()
L=L.split(",")
L=list(map(int,L))

def sapxep(L):
    for i in range(len(L)-1):
        for j in range(i+1,len(L)):
            if L[j]>L[i]:
                L[i],L[j]=L[j],L[i]
    
    
    return L

def inkq(kq):
    if kq:
        kq=str(kq)
        print(kq)
        
kq=sapxep(L)
inkq(kq)