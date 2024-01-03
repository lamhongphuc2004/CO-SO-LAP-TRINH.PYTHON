L=input()
L=L.split()
L=list(map(int,L))

def tich(L):
    GTLN=L[0]*L[1]
    for i in range(len(L)-1):
        for j in range(i+1,len(L)):
            if L[j]*L[i]>GTLN:
                GTLN=L[j]*L[i]
    return GTLN
    
kq=tich(L)
print(kq)