# for i in range(0, 8, 2): # 0 - начало, 8 - конец, 2 - шаг
#     print(i, end=" ")

# print(abs(-2))  # вывод абсолютной велечины

# print(max([1,2,3,4,5])) # максимальное значение
# x = round(5.876) # округление до большего
# x = sum([2.56, 1, 12]) # суммирует все элементы последовательности
# x = type('') # возвращаяет тип объекта
# x = [1,2,3,4,5]
# for i, y in enumerate(x): # enumerate возвращ. пару (индекс, значение)
#     print(i, y)

# def summ(a, b):
#     c = a + b
#     return c
#
#
# def test():
#     """
#     ничего
#     :return:
#     """
#     pass
#
#
# x = 5
# y = 6
# s = summ(x, y)
# print(s)
# print(test())

# f = lambda x: x ** 2
# print(f(4))
# print((lambda x: x ** 2)(4))

# x = 5
# def outside():
#     y = 10
#     def inside():
#         z = 15
#         print('inside x: {}, y: {}, z: {}'.format(x, y, z))
#     inside()
#     print('outside x: {}, y: {}, z: {}'.format(x, y, 'z - недоступна'))
# outside()
# print('inside x: {}, y: {}, z: {}'.format(x, 'y, z - недоступна'))

# x = 5
# def wrapper():
#     def test1():
#         x = 10
#         print('test1 x = ', x)
#     def test2():
#         print('test2 x = ', x)
#     def test3():
#         global x
#         print('test3 x = ', x)
#         x = 25
#     test1()
#     test2()
#     test3()
# wrapper()
# print('after wrapper x = ', x)

# def average(*args):
#     summ = 0
#     for arg in args:
#         summ += arg
#     return summ / len(args)
#
#
# print(average(1, 2, 3))
#
#
# def format(**kwargs):
#     print('You name is %s %s. Your age is %s. And your address is: %s' %
#           (kwargs['name'], kwargs['surname'], kwargs['age'], kwargs['address']))
#
#
# format(name='Vasa', surname='Ivaniv', age='12', address='Poop.str 22')


# def welcome(name='Pool'):
#     print('Welcome, %s' % name)
#
#
# def prin(*args, sep='', end=''):
#     print('Иван,Иванович,иванов', sep='//', end='!!!')
#
#
# print(welcome('user'))
# print(welcome())


# a = [1, 2, 4]
# b = [3, 4]
# c = [5, 6, 0]
# for i in zip(a, b, c): # зип - итератор который генерирует серию множеств, содержащие элементы из каждой итерации
#     print(i)
# print(zip(a, b, c))

# print(list(map(lambda x: x * x, [2, 5, 12, -2]))) # map приеняется последовательно и возвращается в виде итератора

# filter - итератор с отфильтрованием элементов функцией filter_func
# print(list(filter(lambda x: x > 5, [2, 10, -10, 8, 2, 0, 14])))
# # отбрасываем все элементы с длиной НОЛЬ
# print(list(filter(len, ['', 'not null', 'bla','', '10'])))

# import os
# path = os.path.join('lesson1.py')  # хороший кроссплатформенный метод указания пути
# f = open(path, 'r', encoding='UTF-8')
# print(f.readlines())  # считываем все из файла
# f.close()

import os
path = os.path.join ('lesson1.py')
f = open(path, 'r', encoding='UTF-8')
wanted_symbol = '+'
for line in f:  # считываем файл построчно
    if wanted_symbol in line:   # пока не найдем нужную информацию
        print(line)
        break   # как нашли, заканчиваем чтение файла
# наиболее правильный способ работы с файлами
# по окончанию with, гарантированно закроется фалй
with open(path, 'r', encoding='UTF-8') as f:
    print(f.readlines())

my_file = open('lesson1.py', 'w')
my_file.write('мне нравится python')
my_file.close()