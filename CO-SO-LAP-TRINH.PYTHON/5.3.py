# Viết chương trình sử dụng hàm thực hiện các yêu cầu sau:
# Hàm Input() : nhap số nguyên n (n>0) và n số nguyên lưu vào list L, và một số nguyên x
# hàm FirstAndLast(L): trả về và in lên màn hình List mới chỉ gồm phần tử đầu tiên và cuối cùng của L
# Hàm search(L,x): xác định x có nằm trong L hay không .Trả về True nếu tìm thấy, còn lại trả về False

def Input():
    n=int(input('n='))
    x=int(input('x='))
    L=[]
    for i in range(1,n+1):
        a=int(input())
        L.append(a)
    return x,L
def FirstAndLast(L):
    for i in range(len(L)):
        return L[0] , L[-1]
def Search(L,x):
    if x in L:
        return True
    return False
x,L=Input()
print(Search(L,x))