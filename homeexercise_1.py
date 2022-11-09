# Дано натуральное число N. Найдите значение 
# выражения: N + NN + NNN
# N может быть любой длины.
# N = 132: 132 + 132132 + 132132132 = 132264396
n = int(input("Введите число N: "))
num = str(n)
res = n + int(num + num) + int(num + num + num)
print("Решим по формуле N + NN + NNN")
print(f'{num} + {num}{num} + {num}{num}{num}')
print("Результат равен:", res)
