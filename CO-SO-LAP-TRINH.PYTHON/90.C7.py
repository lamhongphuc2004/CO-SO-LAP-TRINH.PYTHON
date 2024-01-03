#Giả sử ta có một số n
#Phỏng đoán COLLATZ hoạt động như sau:
#Nếu n là số chẵn, thì ta chia n cho 2 (n/2)
#Nếu n là số lẻ, thì ta nhân n cho 3 rồi + 1 (3n + 1)
#Phỏng đoán hoạt động cho đến khi nào n = 1




m=int(input("Nhập vào m:"))

def collatz(n):
    kq=str(n)
    while n != 1:
        if n % 2 ==0:
            n=n//2
        else:
            n=n*3+1
        kq += "," + str(n)
    return kq
for i in range (1, m+1):
    print(collatz(i))
