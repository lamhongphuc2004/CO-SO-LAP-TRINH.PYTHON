#Viết chương trình thực hiện tính n!
#   Biết rằng: n!=n*(n-1)!
# Yêu cầu xây dựng các hàm sau:
#  -Hàm nhap(), thực hiện việc nhập một số nguyên dương n từ bàn phím 
# -Hàm giaithua(n),tính và trả về kết quả của phép tính n!
# -Hàm inkq(n,X), thực hiện in lên màn hình kết quả của n!
def Nhap():
    n=int(input('n='))
    return n 
def giaithua(n):
    if n==0:
        return 1
    else:
        gthua=1
        for i in range(1,n+1):
            gthua*=i
        return gthua
def inkq(n,x):
    print(n,"!=",x,sep="")
    
n=Nhap()
x=giaithua(n)
inkq(n,x)