a = input("Введите массив: ")

for n, i in enumerate(a.split()):
    if n == 0:
        max, ind = i, []
    if float(i) > float(max):
        max, ind = i, [n + 1]
    elif float(i) == float(max):
        ind.append(n + 1)

print(f"Максимальный элемент {', '.join([f'A[{i}]' for i in ind])} = {max}")
