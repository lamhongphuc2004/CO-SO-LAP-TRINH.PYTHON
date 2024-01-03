#Viết chương trình:
#- Cho phép nhập vào một chuỗi ký tự bất kỳ;
#- Chương trình thực hiện làm sạch chuỗi ký tự trên. Biết rằng một chuỗi được gọi là “sạch” nếu:#
# Không bắt đầu và kết thúc bằng các ký tự trắng;
#o Mỗi từ chỉ được cách nhau bằng đúng 1 ký tự trắng;
#o Chỉ được phép viết hoa chữ cái đầu tiên của chuỗi;
#o Trước các dấu câu (phẩy, chấm phẩy, hai chấm, chấm) không có ký tự trắng;
#- In nội dung chuỗi sau khi xử lý lên màn hình.
def sach_chuoi(chuoi):
    
    chuoi=chuoi.strip()
    
    chuoi=chuoi.capitalize()   
    
    chuoi=" ".join(chuoi.split())
    chuoi=chuoi.replace(" ,",",").replace(" ;",";").replace(" :",":").replace(" .",".")
    
    return chuoi
chuoi=input()
xulychuoi=sach_chuoi(chuoi)
print(xulychuoi)