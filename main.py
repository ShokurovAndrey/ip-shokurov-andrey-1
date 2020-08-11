"""__author__ = 'Шокуров Андрей Александрович'
Задача №1"""
'''
name = str(input('Введите ваше имя: '))
age = int(input('Введите ваш возраст: '))
age -= 18
print(name, 'на', age, 'лет больше 18')
'''

# Задача №2
'''
a = int(input('Введите 1 число: '))
b = int(input('Введите 2 число: '))
boofer = a
a = b
b = boofer
print('Перевернутое 1 число: ',a)
print('Перевернутое 2 число: ',b)
'''
# Задача №3
'''
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
'''
# Задача №4
