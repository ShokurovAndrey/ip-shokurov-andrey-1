
num = input('+/-: ')
i = 0
if num == '+':
    while i < 21:
        if i % 2 == 0:
            print(i, end=' ')
        i += 1
elif num == '-':
    while i < 21:
        if i % 2 == 1:
            print(i, end=' ')
        i += 1
else:
    print('Я не понимаю, что вы от меня хотите...')