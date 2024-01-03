L=input("Nhập vào L")
L= L.split(",")
for i in range(len(L)):
    if L[i].isnumeric():
        L[i] = int(L[i])
if len(L)%2 ==0:
    kq=True
    for i in range(len(L)-1):
        if not( (type(L[i])is str and type(L[i+1])is int) or (type(L[i+1])is str and type(L[i])is int)):
            kq=False
    if kq:
        K=[]
        for i in range(0,len(L)//2,2):
            K.append(L[i]*L[i+1])
        print("K=",K)
    else:
        print('Khong the xay dung list K vì list L khong phai dang chuoi xen ke so')
else:
    print("Khong the xay dung duoc list k vi so phan tu cua l la le")