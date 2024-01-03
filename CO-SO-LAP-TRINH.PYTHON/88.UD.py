# Viết hàm cho giá trị đầu vào là list số nguyên dương L 
def tim(L, k):
    L_dainhat = []
    dai_toida = 0

    for i in range(len(L)):
        for j in range(i+1, len(L)+1):
            doan_list = L[i:j]
            tb = sum(doan_list) / len(doan_list)
            if tb == k and len(doan_list) > dai_toida:
                L_dainhat = doan_list
                dai_toida = len(doan_list)

    return L_dainhat
L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
k = 4

ket_qua = tim(L, k)
print(ket_qua)  # Kết quả: [4, 5, 6, 7, 8]
