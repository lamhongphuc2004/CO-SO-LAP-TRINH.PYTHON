text = "--Người---đâu-gặp---gỡ-làm-chi--- Trăm----năm-biết-có---duyên---gì--hay--không. Ngổn-ngang---trăm-mối---bên---lòng---- Nên-câu---tuyệt--diệu-ngụ-trong-tính-tình."

# Loại bỏ các dấu gạch ngang và khoảng trắng dư thừa
xulychuoi = " ".join(text.split("-"))

# Tách đoạn văn bản thành các từ
tu = xulychuoi.split()

# Tạo danh sách các câu lục bát
luc_bat = []
i = 0
while i < len(tu):
    if len(luc_bat) % 2 == 0:
        dong = " ".join(tu[i:i+6])
        luc_bat.append(dong)
        i += 6
    else:
        dong = " ".join(tu[i:i+8])
        luc_bat.append(dong)
        i += 8

# Đưa các dòng thơ vào đúng cấu trúc
cautruc = "\n".join(luc_bat)

# In ra đoạn văn bản đã được tiền xử lý và các dòng thơ đã được định dạng
print(cautruc)
