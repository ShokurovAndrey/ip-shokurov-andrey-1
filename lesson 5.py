##### Передача аргументов по ссылке / значению

# n1 = 2
# n2 = n1
# n1 = 4
# print('n1 - ', n1, 'n2 - ', n2)
# неизменяемые объекты int float complex str tupl - Immutable object
# изменяемые объекты set list dict - Mutable object
# print(f'n1={n1} n2={n2}')
#
# sp1 = [1, 2, 3]
# sp2 = sp1
# sp2.append(4)
# print(f'sp1 = {sp1} sp2 = {sp2}')
# print(f'id(sp1) = {id(sp1)} id(sp2) = {id(sp2)}')


# def modify(lst):
#     lst.append('new')
#     return lst
#
#
# my_list = [1, 2, 3]
# # mod_list = modify(my_list[:])
# mod_list = modify(list(my_list))
# #функция вернула измененный список
# print('mod_list = ', mod_list, id(mod_list))
# # но исходный список тоже изменился, подобное неявное поведение нежелательно для функции
# print('mod_list = ', my_list, id(my_list))

# my_list = [1, -2, -4, 0, 5, -2]
# # удаляем все отрицательные элементы
# for el in my_list:
#     if el < 0:
#         my_list.remove(el)
# # не тот результат который ожидали
# print('1) my_list after remove ---> ', my_list)
#
# my_list = [1, -2, -4, 0, 5, -2]
# # итерируем по копии, а удаляем из оригинала
# for el in my_list[:]: # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#     if el < 0:
#         my_list.remove(el)
# # отлично
# print('1) my_list after remove ---> ', my_list)

# если нужно сделать полную копию со всеми вложенными изменяемыми объектами, используем copy
# import copy
# sp = [[2, 3], [4, 6, [7, 8]]]
# sp_copy = copy.deepcopy(sp)
# sp[0].append(10)
# print('sp_copy = ', sp_copy)
# print('sp - ', sp)
# #
# sp_copy = sp[:] # запись поверхностной копии sp
# print('sp = ', sp)
#
############################# матрицы \ список со списком \\\\ изменяемый объект

# matrix = [[1, 2, 3],
#           [4, 5, 6],
#           [7, 8, 9]]
# print('matrix = ', matrix)
#
# # делаем просто и красиво
# print('*************FOR************')
# for i, line in enumerate(matrix):
#     for j, el in enumerate(line):
#         print('matrix[{}][{}] = {}'.format(i, j, matrix[i][j]))
# ## Пример транспортирования (поворота) матрицы
# print('rotate_matrix = ', list(map(list,zip(*matrix))))

################ принцип работы операторов and or

# people = {}
# if people.get('name'):
#     name = people['name']
# else:
#     name = 'Безымянный'
# print(name)
# name = people.get('name') or 'Unknow'
#
# # тоже самое с помощью or
#
# print(people.get('name') or 'безымянный')
# # несмотря на несуществ. переменную u_var, код все равно выполняется, т.к. оператор or не проверяет операнд справа
# print(5 or u_var) # какая то дичь


############################ тернанрый оператор  -
# - истина if условие else иначе (d.get('name') if d.get('name') else 'безымянный')
#
# d = {'name': 'Вася'}
#
# if d.get('name'):
#     name = d['name']
# else:
#     name = 'безымянный'
# print(name)
# # или с поьощью if else
# print(d.get('name') if d.get('name') else 'безымянный')

################# оператор is - оператор - является

# c = [1, 2]
# d = c
# e = [1, 2]
# print(c is d)
# print(c is e)

#####################################  генераторы списков и словарей

# import random
# # Заполняем список произвольными целыми числами
# lst = []
# for _ in range(10): # на месте _ может быть, что угодно i и так далее, не заостряем внимания
#     lst.append(random.randint(-10, 10))
# print('lst = ', lst)
#
# #Тоже самое, но с помощью генератора списка
# #Компактнее код и выполняется быстрее
# lst_g = [random.randint(-10, 10) for _ in range(10)]
# print('lst_g = ', lst_g)
#
# # Отбрасываем все отрицательные элементы списка
# only_positive = [el for el in lst_g if el >= 0]
# print('only_positive = ', only_positive)

########## генераторы словари / словарь изменяемый

# keys = 'abcdefg'
# values = range(10)
# dict_g = {key: value for key, value in zip(keys, values)}
# #подробнее о зип в след. примере
# print('dict_g = ', dict_g)
# # более прсотой пример создания словаря
# dict2_g = {el: el+4 for el in [1, 4, 6, 8]}
# print('dict2_g = ', dict2_g)

########################################## регулярные выражения
#
# print('hello \t world') # tab
# print(r'Hello \t world') # видим все

# RE.MATCH
import re
# string = 'This is a simple test message for test'
# string2 = 'test'
# pattern1 = 'test$'
# pattern2 = '^test'
# pattern3 = '^test$'
# print(re.search(pattern1, string) is None)  # строка заканчивается на 'test'
# print(re.match(pattern2, string) is None)  # строка не заканчивается на 'test'
# print(re.match(pattern3, string) is None)  # строка не является строкой 'test'
# print(re.match(pattern3, string2) is None)  # строка является строкой 'test'
#
# found = re.findall(r'test', string)
# print(found)

# REGEXP
# найти все цифры в тексте
# pattern = '[0-9]+k'
# string = 'if 300 spartans were so brave, so 500 spartans`' \
#     'could destroy more than 10k warriors of Darius, but 15k and even 20k'
# print(re.findall(pattern, string))
# # найти все диапазоны
# pattern2 = '[0-9]+ *-*[0-9]+'
# string2 = ' 10 adajksh 15- 10 oiyqhweq (4-9C) -5'
# print(re.findall(pattern2, string2))
#
# # извлечем из html-кода только теги
# html = '<p style="margin-left:10px;"text'\
#     '<b class="super-bold">bold text</b>.</p>'
# pattern = '<[^>]+>'
# print(re.findall(pattern, html))
