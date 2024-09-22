string = input('Введите текст: ')

split_string = string.lower().split()
print(' '.join(split_string[::-1]))
