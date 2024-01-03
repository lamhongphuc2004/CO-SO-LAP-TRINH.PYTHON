# tìm số hoàn hảo

def nhap():
    n=int(input())
    return n
def uocchung(n):
    tong=0
    for i in range(1,n):
        if n%i==0:
            tong+=i
        if tong ==n:
            return True
    return False
                
         
            
        
    
n=nhap()
kq = uocchung(n)
print(kq)
