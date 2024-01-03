#Nhập vào một chuỗi, kiểm tra chuỗi đó có phải là một chuỗi mật khẩu mạnh hay không
# (một chuỗi mật khẩu mạnh cần có ít nhất 1 ký tự đặc biệt, 1 ký tự in hoa, 1 con số, 1 chữ thường và độ dài phải lớn hơn 6)
def mk(password):
    if len(password)<=6:
        return False
    dacbiet=False
    hoa=False
    thuong=False
    so=False

    kitudacbiet="!@#$%^&*()_+[]{}:;,.<>?/|-'"
    for char in password:
        if not dacbiet and char in kitudacbiet:
            dacbiet=True
        if not hoa and char.isupper():
            hoa =True
        if not thuong and char.islower():
            thuong=True
        if not so and char.isdigit():
            so=True
        if dacbiet and so and thuong and hoa:
            break
    if dacbiet and hoa and thuong and so:
        return True
    else:
        return False
password=input("Nhap mat khau:")
if mk(password):
    print("Mat khau manh")
else:
    print("mat khau khong hop le")

    