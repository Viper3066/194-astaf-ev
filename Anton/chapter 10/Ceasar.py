text = input("Введите текст, который хотите зашифровать: ")
k = int(input("Укажите ключ: "))

def ceaser(t, key):
    res, n = "", ""
    dictionary, dictionary_upper = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя", "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"

    for i in range(len(t)):
        if t[i] in dictionary:
            n = dictionary
        elif t[i] in dictionary_upper:
            n = dictionary_upper
        else:
            res += (t[i])
        if t[i] in n:
            for j in range(len(n)):
                if 0 <= j + key < len(n) and t[i] == n[j]:
                    res += (n[j + key])
                elif j + key >= len(n) and t[i] == n[j]:
                    res += (n[(1 - j - key) % (len(n) - 1)])
                elif j + key < 0 and t[i] == n[j]:
                    res += (n[(j + key) % len(n)])
    return res

print(ceaser(text, k))