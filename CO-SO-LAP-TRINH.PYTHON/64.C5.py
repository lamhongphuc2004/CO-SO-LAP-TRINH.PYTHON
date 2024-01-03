#.  Người  ta  định  nghĩa  một  list  số  nguyên  là  list  chẵn  lẻ,  nếu  như  tổng  2  phần  tử  bất  kỳ  bên  trong  list  đều  là  số  lẻ
#Nhập  vào  một  list  số  nguyên  L  và  kiểm  tra  xem  L  có  phải  là  list  chẵn  lẻ  hay  không.
def nhap():
    n=int(input('n='))
    L=[]
    for i in range(n):
        a=int(input())
        L.append(a)
    return L
def kiem_tra_list_chan_le(lst):
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if (lst[i] + lst[j]) % 2 == 0:
                return False
    return True

# Kiểm tra xem list L có phải là list chẵn lẻ hay không
def inkq(L):
    if kiem_tra_list_chan_le(L):
        print("Là list chẵn lẻ")
    else:
        print("Không phải là list chẵn lẻ")
L=nhap()
kq=kiem_tra_list_chan_le(L)
inkq(L)


