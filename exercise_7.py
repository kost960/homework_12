string = input('Введите текст: ')

split_string = string.split()
min_len = len(split_string[0])
for word in split_string:
    if len(word) < min_len and word.isalpha():
        min_len = len(word)

print(min_len)
