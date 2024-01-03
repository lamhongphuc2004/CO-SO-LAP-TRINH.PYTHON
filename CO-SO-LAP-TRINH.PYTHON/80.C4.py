#viết hàm đưa vào 1 list số nguyên : và 1 số nguyên a. 
# Hãy tìm và trả về một list mới có số phần tử là a, giá trị các phần tử là các số nguyên tố tìm được trong list L
def nhap():
    n=int(input('n='))
    a=int(input('a='))
    L=[]
    for i in range(n):
        k=int(input())
        L.append(k)
    return L,a
def tim_SNT(a,L):
    def laSNT(n):
        if n<2:
            return False
        for i in range(2,int(n*0.5)+1):
            if n%i==0:
                return False
        return True
    songuyento=[]
    for num in L:
        
        if laSNT(num):
            songuyento.append(num)
            if len(songuyento)==a:
                break
    return songuyento[:a]
def inkq(kq):
    print(kq)
L,a=nhap()
kq=tim_SNT(a,L)
inkq(kq)
        
            
