n = int(input("Введите натуральное число: "))
cnt = 0
while n > 0:
    last = n % 10
    if last == 1:
        cnt += 1
    n = n // 10

print(f"Единиц: {cnt}")
