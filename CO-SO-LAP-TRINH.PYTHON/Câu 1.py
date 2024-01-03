def nhap():
    n=int(input())
    return n 
def namnhuan(n):
    
    while n%4 ==0:
        return True
    while n%100==0:
        if n%400==0:
            return True
    else:
        return False
            
def inkq(kq):
    if kq:
        print("Co")
    else:
        print("Khong")
n=nhap()
kq=namnhuan(n)
inkq(kq)