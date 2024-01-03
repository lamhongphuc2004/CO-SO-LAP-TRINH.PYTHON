a = []
while True:
    num = int(input("Nhap so nguyen: "))
    if num == 0:
        break
    a.append(num)
print("\nTap hop cac so nguyen:")
for i in range(len(a) - 1, -1, -1):
    print(a[i])
