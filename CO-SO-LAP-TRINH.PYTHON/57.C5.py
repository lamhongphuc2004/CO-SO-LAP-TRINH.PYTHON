#Bài  57.  Nhập  vào  một  list  L,  hãy  tìm  và  in  ra  giá  trị  âm  lớn  nhất  trong  L,  nếu  L  không  có  giá  trị  âm  thì  ta  in  0
def nhap():
    n=int(input('n='))
    L=[]
    for i in range(n):
        a=int(input())
        L.append(a)
    return L
def giatriam(L):
    gtriam=0
    for i in L:
        if i<0:
            if gtriam==0 or gtriam<i:
                gtriam=i
    print(gtriam)
   