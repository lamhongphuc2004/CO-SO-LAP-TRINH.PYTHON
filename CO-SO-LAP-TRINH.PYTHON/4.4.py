#Yêu cầu sử dụng tôi thiểu 3 hàm
# Nhập từ bàn phím hai số thực a và b
# Nhập từ bàn phím một toán tử (+,-,*,/)
#In lên màn hình kết quả của biểu thức tương ứng

def nhap():
    a=float(input('a='))
    b=float(input('b='))
    ch=input('Toan tu:')
    return a,b,ch
def tinhtoan(a,b,ch):
    if ch=="+":
        print(a,"+",b,'=',a+b,sep="")
    elif ch=="-":
        print(a,"-",b,"=",a-b,sep="")
    elif ch=="*":
        print(a,"*",b,"=",a*b,sep="")
    elif ch=="/":
        if b==0:
            print("Phep tinh loi")
        else:
            print(a,"/",b,"=",a/b,sep="")


while True:
    a,b,ch=nhap()
    tinhtoan(a,b,ch)
    tt=input("Tiep tuc:")
    if tt=="t" or tt=="T":
        break