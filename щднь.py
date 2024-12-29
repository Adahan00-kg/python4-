# 1.2. Факториал числа
# num = int(input('san jaz: '))
# total  = 1
# if num >= 0:
#     for i in range(1,num+1):
#         total *= i
#     print(f'{num} dyn factorily {total}')
#
# else:
#     print(f'eto sifra menshe 0 ')
from enum import unique
from random import random


# 1.3. Сумма чисел до n
# Напишите программу, которая вычисляет сумму всех чисел от 1 до n.
# num = int(input('num jaz: '))
# san1 = 0
# for i in range(num+1):
#     san1 += i
#
# print(san1)

# 2.1. Поиск палиндрома
# soz = input('soz jaz:')
# if soz == soz[::-1]:
#     print('polimdroma')
#
# else:
#     print('polindroma emes')


# num = int(input('san jaz: '))
# if num > 0:
#     print(f'фабинч число по счету {num} будет {(num-2)+(num-3)}')

# # Ввод количества чисел Фибоначчи
# n = int(input('Введите количество чисел Фибоначчи: '))
#
# # Проверка, что количество чисел положительное
# if n <= 0:
#     print('Количество чисел должно быть больше 0')
# else:
#     # Инициализация первых двух чисел последовательности
#     fib_sequence = [0, 1]
#
#     # Генерация последовательности Фибоначчи
#     for i in range(2, n):  # Начинаем с третьего числа
#         next_number = fib_sequence[-1] + fib_sequence[-2]
#         fib_sequence.append(next_number)
#
#     # Вывод последовательности
#     print('Последовательность Фибоначчи:', ', '.join(map(str, fib_sequence[:n])))

# import random
#
# number1 = int(input('напиши минимум: '))
# number2 = int(input('напишите максимум: '))
# step = 1
# random_number = random.randint(number1,number2)
# world = input('вы готовы? да/нет').split()
# if world =='нет':
#     print('пока')
# elif world == 'да':
#     print('тогда начали')
#     while True:
#         num = int(input('напишите среднию цифру'))
#         if num > random_number:
#             print('ваше цифро больше чем загаданное ')
#             step += 1
#
#         elif num < random_number:
#             print('ваше цифро меньше чем загаданное')
#             step += 1
#
#         elif num == random_number:
#             print('ura')
#             break
#     print(f'вы угадали {random_number} по {step} попытку ')


# def unique_in_order(sequence):
#     first_world = ''#A
#     unique_world = []
#     for i in sequence: #B
#         if i != first_world: # B != A
#             unique_world.append(i)
#             first_world = i
#         else:
#             continue
#     return unique_world
# print(unique_in_order('AAABBSSSBAA'))