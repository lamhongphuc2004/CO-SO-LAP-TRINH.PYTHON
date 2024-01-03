# Nhập vào một chuổi, hãy tách toàn bộ kí tự số trong chuổi ra rồi tính tổng của chúng
str=input("")

s=0
for ch in str:
    if ch.isdigit():
        ch=int(ch)
        s+=ch
print(s)