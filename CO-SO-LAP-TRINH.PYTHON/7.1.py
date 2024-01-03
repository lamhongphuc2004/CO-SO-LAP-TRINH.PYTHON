#Viết chương trình nhập vào họ tên của một sinh viên. Kiểm tra
#tính hợp lệ của chuỗi nhập vào. Biết rằng họ tên hợp lệ nếu tất cả được
#viết thường, chỉ viết hoa chữ cái đầu của từ.
def vietten(ten):
    
    tu=ten.split()     # tách chuổi thành các chữ cái
    
    for word in tu:
        if word[0] !=word[0].upper():
            return False
        
    return True
hs_ten=input("Ho va ten: ")

            
if vietten(hs_ten):
    print("Ho ten hop le")
else:
    print("Ho ten khong hop le")
