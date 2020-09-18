""" __author__ = 'Шокуров Андрей Александрович' """
# Easy

# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()

lavka_ashota = ['apple', 'banana', 'mango']  # :D
i = 0
while len(lavka_ashota) > i:
    print(i + 1, '{:>10}'.format(lavka_ashota[i]))
    i += 1
print()

for fruit in lavka_ashota:
    i += 1
    print(i, '{:>10}'.format(fruit))
print()

# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.


a = [23, 0, 1, -20, 8, 999]
b = [23, 1, 11, -20, 100, 998]

a = [x for x in a if x not in b]
print(a)

# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.
# print('Easy. Задача 3')


pusS = []
proS = [100, 20, 30, -15, 0, 1, 7, 94632417]
for i in proS:
    if i % 2 == 0:
        i = i / 4
        pusS.append(i)
    elif i % 2 == 1:
        i = i * 2
        pusS.append(i)
print(pusS)

# Normal

# Задача-1:
# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример: Дано: [2, -5, 8, 9, -25, 25, 4] Результат: [3, 5, 2]

from math import sqrt

s_f = [2, -5, 8, 9, -25, 25, 4]
s_s = []

for i in s_f:
    if i > 0 and sqrt(i) % 1 == 0:
        s_s.append(int((sqrt(i))))
print(s_s)


# Задача-2: Дана дата в формате dd.mm.yyyy, например: 02.11.2013.
# Ваша задача вывести дату в текстовом виде, например: второе ноября 2013 года.
# Склонением пренебречь (2000 года, 2010 года)
# Пусть дана дата 01.01.2000


date = input('Введите дату: ')
data_list = date.split('.')

day_list = {
    '01': 'Первое', '02': 'Второе', '03': 'Ттретье', '04': 'Четвертое', '05': 'Пятое', '06': 'Шестое', '07': 'Седьмое',
    '08': 'Восьмое', '09': 'Девятое', '10': 'Десятое', '11': 'Одиннадцатое', '12': 'Двенадцатое', '13': 'Тринадцатое',
    '14': 'Четырнадцатое', '15': 'Пятнадцатое', '16': 'Шестнадцатое', '17': 'Семнадцатое', '18': 'Восемьнадцатое',
    '19': 'Девятнадцатое', '20': 'Двадцатое', '21': 'Двадцать первое', '22': 'Двадцать второе', '23': 'Двадцать третье',
    '24': 'Двадцать четвертое', '25': 'Двадцать пятое', '26': 'Двадцать шестое', '27': 'Двадцать седьмое',
    '28': 'Двадцать восьмое', '29': 'Двадцать девятое', '30': 'Тринадцатое', '31': 'Тридцать первое',
}

months_list = {
    '01': 'Января', '02': 'Февраля', '03': 'Марта', '04': 'Апреля', '05': 'Мая', '06': 'Июня', '07': 'Июля',
    '08': 'Августа', '09': 'Сентября', '10': 'Октября', '11': 'Ноября', '12': 'Декабря'
}

for key in day_list:
    if data_list[0] == key:
        data_list[0] = day_list[key]

for key in months_list:
    if data_list[1] == key:
        data_list[1] = months_list[key]

full_data = data_list[0] + ' ' + data_list[1] + ' ' + data_list[2] + ' ' + 'г.'

print(full_data)

# Задача-3: Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random

import random

nZ = int(input('Введите количество элементов в списке: '))
pusto = []
for el in range(nZ):
    pusto.append(random.randint(-100, 100))
print(pusto)


# Задача-4: Дан список, заполненный произвольными целыми числами.
# Получите новый список, элементами которого будут:
# а) неповторяющиеся элементы исходного списка:
# например, lst = [1, 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 2, 4, 5, 6]
# б) элементы исходного списка, которые не имеют повторений:
# например, lst = [1 , 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 4, 6]

lst = [1, 2, 4, 5, 6, 2, 5, 2]
new_list = set(lst)
print(list(new_list))

next_list = []
for item in lst:
    if lst.count(item) == 1:
        next_list.append(item)
print(next_list)

# Hard

# Задание-1: уравнение прямой вида y = kx + b задано в виде строки.
# Определить координату y точки с заданной координатой x.
# equation = 'y = -12x + 11111140.2121'
# x = 2.5
# вычислите и выведите y


# Задание-2: Дата задана в виде строки формата 'dd.mm.yyyy'.
# Проверить, корректно ли введена дата.
# Условия корректности:
# 1. День должен приводиться к целому числу в диапазоне от 1 до 30(31)
# (в зависимости от месяца, февраль не учитываем)
# 2. Месяц должен приводиться к целому числу в диапазоне от 1 до 12
# 3. Год должен приводиться к целому положительному числу в диапазоне от 1 до 9999
# 4. Длина исходной строки для частей должна быть в соответствии с форматом
# (т.е. 2 символа для дня, 2 - для месяца, 4 - для года)
# Пример корректной даты
# date = '01.11.1985'
# Примеры некорректных дат
# date = '01.22.1001'
# date = '1.12.1001'
# date = '-2.10.3001'


my_date = input('Введите дату через точку: ')
converted_date = my_date.split('.')
converted_day = int(converted_date[0])
converted_month = int(converted_date[1])
converted_year = int(converted_date[2])
long_month = [1, 3, 5, 7, 8, 10, 12]
if len(converted_date[0]) != 2 or len(converted_date[1]) != 2 or len(converted_date[2]) != 4:
    print('Не корректен формат даты')
elif converted_day > 31 or converted_day < 1:
    print('Введён не корректный день')
elif converted_month > 12 or converted_month < 1:
    print('Введён не корректный месяц')
elif converted_year > 9999 or converted_year < 1:
    print('Введён не корректный год')
elif converted_month not in long_month and converted_day > 30:
    print('Введён не корректный день')
else:
    print('Дата введена корректно: ', my_date)

