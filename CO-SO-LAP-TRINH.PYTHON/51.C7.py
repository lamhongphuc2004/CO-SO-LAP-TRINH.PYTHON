#Nhập vào một số nguyên, hãy chuyển số sang chuỗi, rồi đặt dấu chấm phân tách mỗi 3 chữ số (phân cách phần ngàn) rồi in ra màn hình
so=int(input())
chuoi=str(so)
# đảo ngược chuổi
daonguoc=chuoi[::-1]
# tạo danh sách chuổi con có 3 số
ds=[daonguoc[i:i+3] for i in range(0,len(daonguoc),3)]

daonguoc=".".join(ds)
chhuoidinhdang=daonguoc[::-1]
print(chhuoidinhdang)