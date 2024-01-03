# Nhập vào một chuổi , hãy đếm xem trong chuổi có bao nhiêu kí tự in hoa hoa, bao nhiêu kí tự in thường, bao nhiêu ký tự số

str=input("Nhập vào chuổi:")

chuoi=str.split()
tong=0
for i in str:
    if i.isdigit():
        i=int(i)
        tong+=i
print('tong la:',tong)
