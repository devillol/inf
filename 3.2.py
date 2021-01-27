a = input("Введите массив: ")
sum = 0
for i in a.split():
    sum += int(i)

print(f"Сумма: {sum}")
