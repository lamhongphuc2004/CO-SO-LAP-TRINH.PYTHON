#Một khách sạn có N phòng đôi được đánh số từ 1 đến N và M đoàn khách.

#Với mỗi đoàn khách, ta xếp mỗi cặp khách của đoàn vào một phòng trống theo thứ tự phòng tăng dần.

#Nếu đoàn khách có số người lẻ thì người khách cuối cùng được xếp vào một phòng trống tiếp theo.

#Nếu đã hết phòng còn trống thì ta sẽ xếp khách vào những phòng mới chỉ có 1 khách theo thứ tự phòng tăng dần.

#In ra số khách của mỗi phòng sau khi xếp.

#Giả sử không có 2 đoàn khách nào đến cùng một lúc.

#Ví dụ 1:
#N = 7, M = 3
#doankhach = [3,7,3]
#Ta in: 2, 2, 2, 2, 2, 1, 2
N=int(input('Nhap vao so luong phong:'))
L_doankhach=input()
L_doankhach=L_doankhach.split(",")
L_doankhach=list(map(int,L_doankhach))
thutuphong=0
hetphong=False
L_phong=[0]*N
for i in L_doankhach:
    while i !=0:
        if hetphong ==False:
            if i>1:
                i-=2
                L_phong[thutuphong]=2
                thutuphong+=1
                if thutuphong ==N:
                    hetphong=True
                    thutuphong=0
            else:
                L_phong[thutuphong]=1
                i-=1
                thutuphong+=1
                if thutuphong ==N:
                    hetphong =True
                    thutuphong=0
        else:
            if L_phong[thutuphong]==1:
                L_phong[thutuphong]+=1
            thutuphong+=1
print(L_phong)