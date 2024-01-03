#Nhập vào một chuỗi, hãy tách toàn bộ con số trong chuỗi ra rồi tính tổng của chúng
#VD:
#Nhậpchuỗi:abd45ecf47wde3s1
#Tổng: 45 + 47 + 3 + 1 = 96
str=input("")
tong=0
number=""
for char in str:
    if char.isdigit():
        number+=char
    else:
        if number != "" :
            tong+=int(number)
            number=""
if number != "":
    tong+=int(number)
print("Tong:",tong)