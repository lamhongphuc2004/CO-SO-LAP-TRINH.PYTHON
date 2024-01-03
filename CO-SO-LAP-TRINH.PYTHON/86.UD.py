# Một nhà hàng có các món ăn : Gà Rán, hamburger, cocacola
# -Giá của gàn rán là :30.000
# -Giá của hamburger là: 25.000
# -Giá của cocacola : 10.000
#3 Yêu cầu người nhập vào số lượng từng món ăn In ra hoá đơn
print('Chao mừng các bạn đến với nhà hàng thức ăn nhanh!')
print("Mời bạn nhập số lượng từng món ăn")
print()
sl_ga=int(input("Gà rán: "))
sl_ham=int(input("Hambuger: "))
sl_coca=int(input("Cocacola: "))
print()

def dinhdang(s):
    while len(s)<20:
        s+= " "
    return s

print("Hoá đơn: ")
print(dinhdang("Gà rán")+"30.000đ x "+str(sl_ga))
print(dinhdang("Hambuger")+"20.000đ x "+str(sl_ham))
print(dinhdang("Gà rán")+"10.000đ x "+str(sl_coca))
print()
print("Tổng:") 

def phancachngan(a):
    a =str(a)
    i=len(a) -3 
    while i>0:
        a=a[:i] +"."+a[i:]
        i-=3
    return a

print(dinhdang("Gà rán")+phancachngan(30000*sl_ga)+"đ")
print(dinhdang("Hambuger")+phancachngan(25000*sl_ham)+"đ")
print(dinhdang("Cocacola")+phancachngan(10000*sl_coca)+"đ")