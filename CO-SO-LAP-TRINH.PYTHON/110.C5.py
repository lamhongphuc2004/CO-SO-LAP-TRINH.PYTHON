def uocchung(n):
    L = []
    for i in range(1, n):
        if n % i == 0:
            L.append(i)
    return L
def sohoanhao():
    s=0
    for j in range(len(L)):
        s+=int(L[j])
    if s==n:
        return True
    else:
        return False
    
 ##
n=int(input())
L=uocchung(n)
s=sohoanhao()
print(s)