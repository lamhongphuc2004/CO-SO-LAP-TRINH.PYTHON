# Nhập vào một list L có các phần tử bao gồm chuỗi và số nguyên, hãy kiểm tra các phần tử trong L có phải là chuỗi và số xen kẽ nhau không, nếu có thì ta tiến hành tạo một list K mới có các phần tử như sau:
#K[i/2] = L[i]*L[i+1] (với i chẵn)
def check_interleaved(L):
    for i in range(len(L)):
        if i % 2 == 0 and (type(L[i]) is not str):
            return False
        if i % 2 == 1 and (type(L[i]) is not int):
            return False
    return True

def create_new_list(L):
    K = []
    if not check_interleaved(L):
        return K
    for i in range(0, len(L)-1, 2):
        new_element = L[i] * L[i + 1]
        K.append(new_element)
    return K

def input_elements():
    L = []
    while True:
        element = input("Nhập phần tử (nhập 'q' để kết thúc): ")
        if element == 'q':
            break
        L.append(element)
    return L

# Nhập các phần tử của list L
L = input_elements()

# Kiểm tra và tạo list K mới
K = create_new_list(L)

print("List L:", L)
print("List K:", K)
