# Задан массив из случайных цифр на 15 элементов. 
# На вход подаётся трёхзначное натуральное число. 
# Напишите программу, которая определяет, 
# есть в массиве последовательность из трёх элементов, 
# совпадающая с введённым числом.
# [0, 5, 6, 2, 7, 7, 8, 1, 1, 9] - 277 -> да
# [4, 4, 3, 6, 7, 0, 8, 5, 1, 2] - 812 -> нет

import random

numbers = [1, 2, 3, 7, 5, 4, 4, 9, 6, 6, 6, 5, 4, 4, 3]
print(numbers)

num = int(input("Введите трехзначное число: "))
print(num)
if num >= 100 and num <= 999:
    isnum = False
    for i in range(len(numbers)-2):
        sum = str(numbers[i]) + str(numbers[i+1]) + str(numbers[i+2])
        if sum == str(num):
            isnum = True
            print("yes")
            break
    if isnum == False: 
        print("no")          
else:
    print("Вы ввели не трехзначное число")



    