string = 'Сделал дело - гуляй смело'

count = 0
max_count = 0
for i in range(len(string)):
    if string[i] == ' ':
        count += 1
        max_count = max(count, max_count)
    else:
        count = 0

print(f'Максимальное кол-во идущих подряд пробелов: {max_count}')
