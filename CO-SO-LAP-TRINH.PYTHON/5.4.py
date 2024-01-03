# Viết chương trình sử dụng hàm thực hiện yêu cầu:
# Hàm input(): nhập một số nguyên n(n>0) và n số nguyên lưu trử vào một list L
# Hàm search(L): tìm và trả về số nhỏ nhất và lớn nhất trong list L
# Hàm output(max,min): In lên màn hình số lớn nhất và số nhỏ nhất 
def Input():
    n=int(input('n='))
    x=int(input('x='))
    L=[]
    for i in range(n):
        a=int(input())
        L.append(a)
    return x,L
def search(L):
    SLN=L[0]
    SNN=L[0]
    for i in range(len(L)):
        if L[i]>SLN:
            SLN=L[i]
            
        if L[i]<SNN:
            SNN=L[i]
    return SLN, SNN
def Output(max,min):
    if max:
        print("So lon nhat la:",max)
    if min:
        print("So be nhat la:",min)
x,L=Input()
max,min=search(L)
Output(max,min)
    
    