def nhap():
    n=input("")
    return n
def kitu(n):
    dem=0
    chuoi=n.split()
    for i in chuoi:
        if  len(i)<=5:
            dem+=1
    return dem
n=nhap()
kq=kitu(n)
print(kq)