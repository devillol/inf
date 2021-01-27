import random


x = random.randrange(100, 1000)
print(f"Случайное трёхзначное число: {x}")
print(f"Первая цифра {x//100}")
print(f"Последняя цифра {x % 10}")
