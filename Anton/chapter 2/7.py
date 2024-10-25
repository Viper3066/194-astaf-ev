radius = int(input())
print("Диаметр: " + str(radius * 2))

sum = 0
for i in range(100, 501):
    sum += i
print("Сумма всех целых чисел от 100 до 500: " + str(sum))

sum = 0
intI = int(input())
if intI < 500:
    for i in range(intI, 501):
        sum += i
    print("Сумма всех целых чисел от " + str(intI) + " до 500: " + str(sum))