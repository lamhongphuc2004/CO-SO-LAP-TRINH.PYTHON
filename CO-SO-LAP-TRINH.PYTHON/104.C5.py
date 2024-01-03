numbers =[]
while True:
    number = int(input())
    if number == 0:
        break
    else:
        numbers.append(number)
        numbers.sort()
    for number in numbers:
        print(number)
