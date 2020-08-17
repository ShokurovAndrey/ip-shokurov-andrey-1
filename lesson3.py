# 1 операции со строками

str = 'hello'
str_1 = 'lololololololotttololo'
a = 'Start'
b = 'Stop'
c = 'Step'
# str[a:b:c] индексация начинается с нуля
# .title(), .upper(), .lower(), find(), and etc.

# metod string
# print(str_1.find('ttt'), len(str_1))
#
# # format str
# name = 'Eric'
# surname = 'Smith'
# print('Welcome' + name + '' + surname + '!')
# # old ver format
# print('Welcome %s %s !' % (name, surname))
# # py.3.6
# print('Welcome {} {} !'.format(name,surname))
# # new ver format
# print('Welcome {1} {0} !'.format(name, surname))
# # форматирование строк
# print(f'welcome {name} {surname} !')
#
#
# # списки
#
# empty_list = []
# my_list = [1, 3, 5, 3.45, 'ddd', 's', 333]
# print('my_list = ', my_list)

# print(my_list[0])
# print(my_list[1])
# срезы
# print(my_list[0:-3])  # 3 последних элемента списка
# конкантенация
# print(my_list[0:3] + [7, 8, 9])
# print(my_list * 3)
# print(my_list[1] * 3)
# my_list[4] = 2
# print(my_list)

# my_list = [1, [1, [3]]]
# print(my_list[1][1][0])
#
# my_list.append(['1', 3.2])
# print(my_list)
# my_list[1][1].append(['1', 3.2])
# print(my_list)
#
#
# lst = [1, 2, 3]
# lst.append(4) # добавить в конец списка
# lst.pop() # Удалить последний элемент
# lst.pop(1) # Удалить элемент с индексом 1
# delet
# x = [1,2,3]
# print(x)
# print(x.pop())
# print(x)
# del x[0]
# print(x)
#
#
# # Кортежи
#
# t = ()
# t11 = (2,)
# t1 = 2,
# print(t, t11, t1)

# for in  для последовательностей
# fruits = ['apple', 'banana', 'mango']
# i = 0
# while len(fruits) > i:
#     print('fruit = ', fruits[i])
#     i += 1
#
# # # # # # # # # # # # # # # # # # # # # #
# fruits = ['apple', 'banana', 'mango']
# for fruit in fruits:
#     print('fruit = ', fruit)
#
# # # # # # # # # # # # # # # # # # # # #
# for el in 'Hello':
#     print('el = ', el)
# print()
# for t_el in 1,2,3,4,5,10:
#     print('--------')
#     print('t_el = ', t_el)
# print()

# СЛОВАРИ

# x = {'x', 'y', 'a'}
# # # { key : znachenie}
# print(x)
# x['y'] = '1'
# print(x)
# x['y'] = {'1': 1}
# print(x)

# metod slovarey
# cikl po slovar
# for key, value in f.items():
#     print(key, value)
# for key in f.keys():
#     print(key)
# for value in f.values():
#     print(value)
# # удаляет элемент С и возвращает его значение
# print(f.pop('c'))
# print(f)
# # удаляет и возвращает произвольную пару (ключ, значение)
# print(f.popitem)
#
# print(x.items()) # возвращает пары ключ-значение
# print(x.keys()) # возвращает список ключей
# print(x.values()) # возвращает список значения
# print(x.pop('y')) #
# print(x.popitem()) #
# print(x)
# x = {'y': [], 'z': 1}
# print(x)
# x.pop('y')
# print(x)
#
# x['y'] = 1
# print(x)

# a = set()
# print('a = ', a) # set()
# b = set(['a', 'b', 'c', 'c', 'a', 'e'])
# print('b = ', b)
# c = set('hello')
# print('c = ', c)
# d = {'a', 'b', 'c', 'd'}
# print('d = ', d)
# f = {} #  так получается словарь
# print('type({}) ---> ', type(f)) # <class 'dict'>
# # Операции с множествами
# # print(len(e))
# print("'b' in b ---> ", 'b' in b)
# # s == t
# c1 = {'e', 'l', 'o', 'h'}
# print(c == c1)
# # s.issubset(t)   s <= t
# print(c <= c1)
# # s.issuperset(t)s >=  t
# print(c >= {'h'})
# # s.union(t,...) s | t
# print(b | d)
# # s.intersection(t, ...) s & t
# print(b & d)
# # s.difference(t, ...) s - t
# print(d - b)
# # s.symmetric_difference(t) s^t
# print(d^b)

# a = set(['a', '3', '5'])
# b = set(['a', '3'])
# print(a)
# print(b.issuperset(a))
# myset = {1, 2, 3}
# print(myset.issuperset([1, 2]))
# print(myset.issuperset([1, 2, 3]))
# print(myset.issuperset([1, 2, 3, 4]))

d = dict.fromkeys(['a', 'b'])
print(d)
d['a'] = 'aa'
print(d)
d.update({'c': ['1'], 'b': 1})
print(d)