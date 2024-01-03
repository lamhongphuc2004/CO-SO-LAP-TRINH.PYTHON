#Viết chương trình sử dụng hàm, thực hiện nhập từ bàn phím 1 số nguyên n.
#In lên màn hình n số nguyên tố đầu tiên
def Nhap():
    n=int(input('n='))
    return n 
def ktra(n):
    if n<2:
        return False
    for i in range(2,int(n*0.5)+1):
        if n%i==0:
            return False
    return True
def laSNT(n):
    dem=0
    SNT=2
    while dem<n:
        if ktra(SNT):
            print(SNT,end='')
            dem+=1
            if dem<n:
                print(",",end='')
        SNT+=1
                   
n=Nhap()
laSNT(n)

    