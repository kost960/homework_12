def get_symbol_count(string):
    string_set = set(string.lower())

    count = 0
    for e in string_set:
        if e.isalpha():
            count += 1
        else:
            continue

    return count


print(f'Кол-во различных букв: {get_symbol_count('Сделал дело - гуляй смело')}')
