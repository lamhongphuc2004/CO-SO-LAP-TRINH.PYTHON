#: Viết chương trình:
#- Cho phép nhập vào một chuỗi ký tự bất kỳ;
#- Chương trình thực hiện đếm có bao nhiêu chữ cái in hoa, chữ cái in thường, chữ số và ký tự khác (bao
#gồm ký tự trắng) xuất hiện trong chuỗi trên;
#- In kết quả lên màn hình.
str=input("")
hoa=0
thuong=0
so=0
kitukhac=0
for ch in str:
    if ch.isupper():
        hoa+=1
    elif ch.islower():
        thuong+=1
    elif ch.isdigit():
        so+=1
    else:
        kitukhac+=1
    
print("In hoa:",hoa)
print("In thuong:",thuong)
print("Chu so:",so)
print("Khac:",kitukhac)
