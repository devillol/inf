import random


a = [random.randrange(0, 2) for i in range(10)]
print("Массив")
print(' '.join([str(i) for i in a]))
