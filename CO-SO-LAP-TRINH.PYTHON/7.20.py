#Viết chương trình:
#- Nhập vào một chuỗi gồm các số nguyên, mỗi số cách nhau bởi một dấu cách; và một số nguyên X;
#- Chương trình thực hiện tìm X trong dãy số trên, in lên màn hình thứ tự xuất hiện của X nếu có. Nếu
#không tìm thấy thì trả về 0
str=input()
x=int(input("x="))
chuoi=str.split()
vitri=0
for i in range(len(chuoi)):
    if int(chuoi[i]) == x:
        vitri=i+1
        print(vitri)