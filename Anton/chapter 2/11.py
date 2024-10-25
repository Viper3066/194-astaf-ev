mass = [10, -3, -5, 2, 5]
index = 0
mini = min(mass)
for el in mass:
    if el == mini:
        print(index)
        break
    index += 1