# Nhập vào một chuỗi ký tự làm mật khẩu cho chương trình.
#Yêu cầu:
#- Mật khẩu có tối thiểu 8 ký tự;
#- Bao gồm: chữ cái, chữ số, chữ viết hoa và viết thường
def mk(password):
    if len(password)<8:
        return False
    if not any(c.isalpha for c in password):
        return False
    if not any(c.isdigit() for c in password):
        return False
    if not any(c.isupper() for c in password):
        return False
    if not any(c.islower() for c in password):
        return False
    return True
password=input("Nhap mat khau:")
if mk(password):
    print("Mật khẩu đúng")
else:
    print('mat khau sai')