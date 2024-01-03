number = int(input("Nhập vào một số nguyên: "))

number_str = str(number)

# Đặt dấu chấm phân tách mỗi 3 chữ số
result = ""
count = 0
for digit in reversed(number_str):
    if count != 0 and count % 3 == 0:
        result = "." + result
    result = digit + result
    count += 1

print("Kết quả:", result)
