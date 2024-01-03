soam = []
so_0 = []
so_duong= []

while True:
    n = input("")
    if n == "":
        break
    num = int(n)
    if num < 0:
            soam.append(num)
    elif num == 0:
        so_0.append(num)
    else:
        so_duong.append(num)

for num in soam:
    print(num)
for num in so_0:
    print(num)
for num in so_duong:
    print(num)
