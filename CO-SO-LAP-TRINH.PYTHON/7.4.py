#Nhập vào 3 xâu str1, str2, str3 
# In lên màn hình vị trí (index) đầu tiên str2 xuất hiện trong str1 
# Thay thế tẩt cả các xâu st2 bằng st3 
# In lên màn hình kq của xâu đó
def find_first_occurrence(st1, st2):
    for i in range(len(st1)):
        if st1[i:i+len(st2)] == st2:
            return i
    return -1

def replace_string(st1, st2, st3):
    result = ""
    i = 0
    while i < len(st1):
        if st1[i:i+len(st2)] == st2:
            result += st3
            i += len(st2)
        else:
            result += st1[i]
            i += 1
    return result

st1 = input("Nhập vào chuỗi st1: ")
st2 = input("Nhập vào chuỗi st2: ")
st3 = input("Nhập vào chuỗi st3: ")

# Tìm vị trí đầu tiên của st2 trong st1
index = find_first_occurrence(st1, st2)
print("Vị trí xuất hiện đầu tiên của st2 trong st1:", index)

# Thay thế tất cả các xâu st2 bằng st3
result = replace_string(st1, st2, st3)
print("Xâu kết quả:", result)
