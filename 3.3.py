import random


a = [random.randrange(1, 6) for i in range(10)]
print("Массив:")
print(' '.join([str(i) for i in a]))
print(f"Элементов, которые равны 3: {len([i for i in a if i == 3])}")
