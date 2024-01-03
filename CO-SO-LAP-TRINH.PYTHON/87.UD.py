# Viết  hàm cho giá trị đầu vào là list số nguyên dương L và số nguyên dương k.
# Hãy tạo và trả về 1 list L_kq có các phần tử là giá trị của phần tử 
# xuất hiện nhiều hơn k lần trong list L theo thứ tự tăng dần
def listklan(L,k):
    L_kq=[]
    for i in L:
        if L.count(i) > k:
            if i not in L_kq:
                L_kq.append(i)
    L_kq.sort()
    return L_kq
print(listklan([2,2,1,5,6,7,4,2,3,4,4,5,1,2],2))
            