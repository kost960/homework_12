towns = input('Введите города через пробел: ')

split_towns = towns.split()
winner_position = 0
for i in range(len(split_towns) - 1):
    if split_towns[i].lower()[-1] not in 'ъыь' and split_towns[i].lower()[-1] == split_towns[i + 1].lower()[0]:
        winner_position += 1
    elif split_towns[i].lower()[-2] == split_towns[i + 1].lower()[0]:
        winner_position += 1
    else:
        break

print('Победитель: Петя' if winner_position % 2 == 0 else 'Победитель: Вася')
