# Viết hàm đưa ra một list số nguyên và một số nguyên dương k.
# Hãy tìm và trả về phần tử đầu tiên có giá trị k trong list số nguyên, nếu không có thì trả về -1
def nhap():
    n=int(input('n='))
    k=int(input('k='))
    L=[]
    for i in range(n):
        a=int(input())
        L.append(a)
    return L,k
def vitri(k,L):
    for i in range(L):
        if int(L[i])==k:
            return i
        
    return -1
        

def inkq(kq):
    print("Vi tri cua k trong L la:",kq)
k,L=nhap()
kq=vitri(k,L)
inkq(kq)
    
