n = int(input("Введите число: "))
k = 1
list = []
while k <= n:
    list.append(k)
    k *= 2
print(f"Все целые степени двойки: {list}")