import math
s = int(input("Введите сумму двух натуральных чисел: "))
p = int(input("Введите произведение этих же чисел: "))
D = s*s - 4*p
if D > 0:
    print(f"Первое число равно {int((s-math.sqrt(D))/2)}, второе равно {int((s+math.sqrt(D))/2)}")
else:
    print(f"Первое число равно {int(s/2)}, второе тоже {int(s/2)}")