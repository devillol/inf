a = input("Введите массив: ")
max, ind = -1, []
for n, i in enumerate(a.split()):
    if int(i) > max:
        max, ind = int(i), [n + 1]
    elif int(i) == max:
        ind.append(n + 1)

print(f"Максимальный элемент {', '.join([f'A[{i}]' for i in ind])} = {max}")
