a = input("Введите массив: ")
sum = 0
for i in a.split():
    sum += float(i)

print(f"Сумма: {sum if int(sum) != float(sum) else int(sum)}")  # убираем лишний 0
