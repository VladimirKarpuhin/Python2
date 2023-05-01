import random
n = int(input("Введите число монеток: "))
count = 0
count2 = 0
k = 0
for i in range(n):
    k = random.randint(0,1)
    print(k, end=" ")
    if k == 0:
        count += 1
    else:
        count2 += 1
if count < count2:
    print(f"\nМинимальное количество монет, котрые нужно перевернуть: {count}")
else:
    print(f"\nМинимальное количество монет, котрые нужно перевернуть: {count2}")