def get_symbol_count(string):
    count = 1
    max_count = 1
    if len(string) == 0:
        return 0

    for i in range(len(string) - 1):
        if string[i] == string[i + 1]:
            count += 1
            max_count = max(count, max_count)
        else:
            count = 1
    return max_count


print(f'Максимальное кол-во идущих подряд символов: {get_symbol_count('Сделал дело - гуляй смело')}')
