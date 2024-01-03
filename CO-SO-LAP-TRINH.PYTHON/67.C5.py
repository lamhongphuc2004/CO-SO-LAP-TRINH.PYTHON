#Nhập  vào  một  list  số  nguyên  L,  hãy  đưa  các  số  chẵn  trong  list  về  đầu  list,  số  lẻ  về  cuối  list  và  các  phần  tử  0  nằm  ở  giữa.
L=input()
L=L.split(",")
L=list(map(int,L))
L_chan=[]
L_le=[]
L_khong=[]
for i in L:
    if i==0:
        L_khong.append(i)
    elif i%2==0:
        L_chan.append(i)
    else:
        L_le.append(i)
L_kq=L_chan+L_khong+L_le
print(L_kq)