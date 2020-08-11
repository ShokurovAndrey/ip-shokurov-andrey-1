"""__author__ = 'Шокуров Андрей Александрович'

# Задача-1:
Ввести ваше имя и возраст в отдельные переменные,
# вычесть из возраста 18 и вывести на экран в следующем виде:
# "Василий на 2 года/лет больше 18"
# по желанию сделать адаптивный вывод, то есть "на 5 лет больше", "на 3 года меньше" и.т.д."""

name = str(input('Введите ваше имя: '))
age = int(input('Введите ваш возраст: '))
age -= 18
print(name, 'на', age, 'лет больше 18')


# Задача-2:
# Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Подсказка:
# * постарайтесь сделать решение через дополнительную переменную
#   или через арифметические действия
# Не нужно решать задачу так:
# print("a = ", b, "b = ", a) - это неправильное решение!

a = int(input('Введите 1 число: '))
b = int(input('Введите 2 число: '))
boofer = a
a = b
b = boofer
print('Перевернутое 1 число: ',a)
print('Перевернутое 2 число: ',b)

# Задача-3:
# Напишите программу, вычисляющую корни квадратного уравнения вида
# ax² + bx + c = 0.
# Коэффициенты уравнения вводятся пользователем.
# Для вычисления квадратного корня воспользуйтесь функцией sqrt() модуля math:
# import math
# math.sqrt(4) - вычисляет корень числа 4

import math

print('ax² + bx + c = 0')
a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))
discr = b ** 2 - 4 * a * c
print('Дискриминант =', discr)

if discr > 0:
    x1 = (-b + math.sqrt(discr)) / (2 * a)
    x2 = (-b - math.sqrt(discr)) / (2 * a)
    print('x1 =',x1,'x2 =', x2)
elif discr == 0:
    x = -b / (2 * a)
    print('x =', x)
else:
    print('Уравнение корней не имеет')

# Задание-1: Hard
# Ваня набрал несколько операций в интерпретаторе и получал результаты:
# 	Код: a == a**2
# 	Результат: True
# 	Код: a == a*2
# 	Результат: True
# 	Код: a > 999999
# 	Результат: True

# Вопрос: Чему была равна переменная a,
# если точно известно, что её значение не изменялось?

a = 1000000
print(bool(a) == bool(a ** 2))
print(bool(a) == bool(a * 2))
print(a > 999999)

print('Значение не менялось. Любое число > 999999')
