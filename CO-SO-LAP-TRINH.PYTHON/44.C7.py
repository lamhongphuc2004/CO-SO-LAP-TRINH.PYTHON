#Nhập vào một chuỗi, hãy in từ đầu tiên trong chuỗi
input_string = input("Nhập vào chuỗi: ")
words = input_string.split()
if len(words) > 0:
    print("Từ đầu tiên trong chuỗi:", words[0])
else:
    print("Chuỗi không có từ")
