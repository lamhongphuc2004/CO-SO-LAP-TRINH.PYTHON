# Viết chương trình đếm số nguyên tố
# Hàm LaSNT(x): trả về True nếu x là số nguyên tố, còn lại trả về False
# Hàm Sohople(x): trả về True nếu x<=1 , còn lại trả về False
# Hàm Nhapvadem(): thực hiện nhập liên tục các số nguyên cho đến khi số được nhập vào là số <=1 thì dừng
# Hàm Inkq(kq): in lên màn hình kết quả theo mẫu
def LaSNT(x):
    for i in range (2,int(x*0.5)+1):
        if x%i==0:
            return False
    return True
def Sohople(x):
    return x<=1
def Nhapvadem():
    print('Nhap day so:')
    dem=0
    while True:
        x=int(input())
        if Sohople(x):
            break
        if LaSNT(x):
            dem+=1
    return dem
def Inkq(kq):
    print("Co",kq,"so nguyen to")

        
kq=Nhapvadem()
Inkq(kq)