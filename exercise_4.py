string = input('Введите текст: ')

for e in string:
    if string.count(e) == 3:
        print(e)
        break
