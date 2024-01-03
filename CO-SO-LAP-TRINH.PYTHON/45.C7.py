#Nhập vào một chuỗi có dạng 3 số nguyên, mỗi số nguyên cách nhau một dấu phẩy, hãy tính tổng 3 số nguyên đó
#VD:
#Nhập:3,12,15
#Tổng: 30
str=input("nhap chuoi:")
chuoi=str.split(",")
tong=0
for i in chuoi:
    if i.isdigit():
        i=int(i)
        tong+=i
print(tong)