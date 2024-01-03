#Nhập vào chuỗi a và chuỗi b
#Hãy xóa chuỗi b trong chuỗi a rồi in lại chuỗi a ra màn hình (không dùng hàm replace)
def dichuyen(a,b):
    while b in a:
        index=a.find(b)
        a=a[:index]+a[index+len(b)+1:]
    return a
a=input()
b=input()
a_dc=dichuyen(a,b)
print(a_dc)