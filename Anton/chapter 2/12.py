def toB(kb):
    return kb * 1024

def toKB(b):
    return b / 1024

print("Введите число для конвертации:")
number = int(input())
print("Выберите действие (1 - В килобайты, 2 - В байты)")
choice = input()

if choice == "1":
    print("Результат в КБ: " + str(toKB(number)))
else:
    print("Результат в Б: " + str(toB(number)))