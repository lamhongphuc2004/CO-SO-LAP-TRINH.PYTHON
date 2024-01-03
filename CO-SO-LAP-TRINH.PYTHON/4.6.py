# Viết chươ ng trình nhập từ bàn phím một số nguyên n, in lên màn hình các số nguyên chẵn trong n số tự nhiên đầu tiên.
# Hàm nhap(), thực hiện việc nhập một số nguyên dương n
# Hàm inkq(), thực hiện việc nhập một số nguyên dương n 
#Chương trình lặp lại các côgn việc cho đến khi bấm phím k hoặc K thì kết thúc 
def nhap():
    n=int(input('n='))
    return n
def inkq(n):
    for i in range(1,n+1):
        if i%2==0:
            print(i, end=' ')
while True:
    n=nhap()
    inkq(n)
    tt=input('\nTiep tuc khong?')
    if tt=="K" or tt=="k":
        break