# Viết chương trình giải và biện luận phương trình bậc 2
# Hàm nhap(), thực hiện nhập 3 số a,b,c
# hàm giaipt(a,b,c), thực hiện giải và biện luận phương trình bậc 2 với các tham số a,b,c đầu vào
# Hàm inkq(x1,x2): in kết quả là nghiệm của phương trình được in lên màn hình 
import math

def nhap():
    a = float(input("Nhập hệ số a: "))
    b = float(input("Nhập hệ số b: "))
    c = float(input("Nhập hệ số c: "))
    return a, b, c

def giaipt(a, b, c):
    delta = b**2 - 4*a*c
    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        return "Phương trình có hai nghiệm phân biệt", x1, x2
    elif delta == 0:
        x = -b / (2*a)
        return "Phương trình có nghiệm kép", x, x
    else:
        return "Phương trình vô nghiệm"

def inkq(x1, x2):
    print("x1 =", x1)
    print("x2 =", x2)

a, b, c = nhap()
result, x1, x2 = giaipt(a, b, c)
print(result)
inkq(x1, x2)