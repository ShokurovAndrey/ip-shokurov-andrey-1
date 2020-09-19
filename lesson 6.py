# Задача-1:
# Следующая программа написана верно, однако содержит места потенциальных ошибок.
# используя конструкцию try добавьте в код обработку соответствующих исключений.
# Пример.
# Исходная программа:

def avg(a, b):
    """Вернуть среднее геометрическое чисел 'a' и 'b'.

    Параметры:
        - a, b (int или float).

    Результат:
        - float.
    """
    if a * b > 0:
        return (a * b) ** 0.5
    else:
        raise ValueError("Невозможно определить")


try:
    a = float(input("a = "))
    b = float(input("b = "))
    c = avg(a, b)
    print("Среднее геометрическое = {:.2f}".format(c))
except ValueError as ve:
    print('Ошибка: ', ve, 'Проверьте данные !')

# Задача-2:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
import os

try:
    for i in range(1, 10):
        os.mkdir("dir_" + str(i))
except:
    print("Already exist")
a = input("enter something ")
print(a)

try:
    for i in range(3, 8):
        os.rmdir("dir_" + str(i))
except:
    print("Already removed")

# Задача-3:
# Напишите скрипт, отображающий папки текущей директории.

list1 = os.listdir()
for i in list1:
    print(i)
