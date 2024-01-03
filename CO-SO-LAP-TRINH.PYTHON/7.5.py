# Viết chương trình cho phép nhập vào một chuỗi bất kỳ, đếm số chữ cái và chữ số trong
#câu đó và in kết quả ra màn hình.
str=input("")
chu=0
so=0
 
for ch in str:
    if ch.isalpha():
        chu+=1
    if ch.isdigit():
        so+=1
print('Chu cai:',chu)
print("Chu so:",so)