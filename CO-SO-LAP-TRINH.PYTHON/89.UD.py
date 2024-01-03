#Một người dùng số tiền là U đô-la và V Euro để mua một loại nguyên liệu sản xuất.

#Có N công ty nước ngoài bán nguyên liệu trên được đánh số từ 1 đến N. Công ty thứ i có giá bán Ai đô la/1 kg nguyên liệu và Bi Euro/1 kg nguyên liệu.

#Tuy nhiên, tại mỗi công ty chỉ bán nguyên liệu cho một khách hàng hoặc theo đô-la, hoặc theo Euro.

#Hãy giúp người đó tìm cách chọn ra 2 công ty để mua hàng sao cho số lượng nguyên liệu sản xuất có thể mua được là nhiều nhất.

#Nhập vào: U, V và List A và List B

#In ra: Số lượng nguyên liệu S (kg) người đó mua được với 2 chữ số thập phân.
U=float(input("U="))
V=float(input("V="))
L_A=input()
L_A=L_A.split(",")
L_A=list(map(float,L_A))
L_B=input()
L_B=L_B.split(",")
L_B=list(map(float,L_B))
def vtri_min(L):
    kq=None
    for i in range(len(L)):
        if kq==None or L[kq] > L[i]:
            kq=i
    return kq
cty_dola=vtri_min(L_A)
cty_euro=vtri_min(L_B)

def giarenhi(L):
    L=L.copy
    vt_min=vtri_min(L)
    L.pop(vt_min)
    kq=None
    for i in L:
        if kq==None or kq>i:
            kq=i
    return kq
if cty_dola != cty_euro:
    S = U/L_A[cty_dola] + V/L_B[cty_euro]
else:
    gianhi_dola = giarenhi(L_A)
    gianhi_euro = giarenhi(L_B)
    S1 = U/L_A[cty_dola] + V/gianhi_euro
    S2 = U/gianhi_dola + V/L_B[cty_euro]
    if S1 > S2:
        S=S1
    else:
        S=S2
print(S)