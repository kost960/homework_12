import keyword


def is_valid_name(string):
    if not string:
        return False

    if string in keyword.kwlist:
        return False

    if not (string[0].isalpha() or string[0] == '_'):
        return False

    if not (string[0].isalpha() or string[0] == '_'):
        return False

    for symbol in string[1:]:
        if not (symbol.isalnum() or symbol == '_'):
            return False

    return True


print('Может быть именем' if is_valid_name(input('Введите имя переменной: ')) else 'Не может быть именем')
