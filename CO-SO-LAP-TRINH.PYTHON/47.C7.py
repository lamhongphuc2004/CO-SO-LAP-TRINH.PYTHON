#Nhập vào một chuỗi, hãy đếm xem trong chuỗi có bao nhiêu ký tự in hoa, bao nhiêu ký tự in thường, bao nhiêu ký tự số
str=input("")
hoa=0
thuong=0
so=0
for ch in str:
    if ch.isupper():
        hoa+=1
    elif ch.islower():
        thuong+=1
    elif ch.isdigit():
        so+=1
print("So chu hoa",hoa)
print("So chu thuong",thuong)
print("So ",so)