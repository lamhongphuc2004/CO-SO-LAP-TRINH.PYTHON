# Tránh trùng lặp 
Nhap = []
while True:
    word = input("Nhap cac tu: ")
    if word == "":
        break
    elif word not in Nhap:
        Nhap.append(word)
for word in Nhap:
    print(word)