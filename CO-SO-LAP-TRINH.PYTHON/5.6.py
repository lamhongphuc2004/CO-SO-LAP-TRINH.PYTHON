#Nhập từ bàn phím một số nguyên n (n>0) và n số nguyên lưu vào List A:
#- Hãy đảo ngược giá trị của các phần tử trong List A và lưu vào List B. In giá trị các phần tử trongList B sau khi thực hiện đảo;
#- Sắp xếp và in lên màn hình List B sau khi được sắp xếp tăng dần;


n=int(input('n='))
A=[]
i=0
while i<n:
    k=int(input())
    i+=1
    A.append(k)
B=A[::-1]
print(B)
B.sort()
print(B)
