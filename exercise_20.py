d_units = {
    0: 'ноль',
    1: 'один',
    2: 'два',
    3: 'три',
    4: 'четыре',
    5: 'пять',
    6: 'шесть',
    7: 'семь',
    8: 'восемь',
    9: 'девять',
}

d_teens = {
    10: 'десять',
    11: 'одиннадцать',
    12: 'двенадцать',
    13: 'тринадцать',
    14: 'четырнадцать',
    15: 'пятнадцать',
    16: 'шестнадцать',
    17: 'семнадцать',
    18: 'восемнадцать',
    19: 'девятнадцать',
}

d_tens = {
    20: 'двадцать',
    30: 'тридцать',
    40: 'сорок',
    50: 'пятьдесят',
    60: 'шестьдесят',
    70: 'семьдесят',
    80: 'восемьдесят',
    90: 'девяносто',
}

d_hundreds = {
    100: 'сто',
    200: 'двести',
    300: 'триста',
    400: 'четыреста',
    500: 'пятьсот',
    600: 'шестьсот',
    700: 'семьсот',
    800: 'восемьсот',
    900: 'девятьсот',
}

d_large = {
    1000: ['одна тысяча', 'тысяч', 'тысячи'],
    10 ** 6: ['один миллион', 'миллионов', 'миллиона'],
    10 ** 9: ['один миллиард', 'миллиардов', 'миллиарда'],
}


def number_to_words(x):
    if x == 0:
        return d_units[0]

    parts = []
    previous_x = x

    billions = x // 10 ** 9
    if billions > 0:
        if billions == 1 and billions != 11:
            parts.append(d_large[10 ** 9][0])
        elif 2 <= billions <= 4:
            parts.append(number_to_words(billions) + ' ' + d_large[10**9][2])
        else:
            parts.append(number_to_words(billions) + ' ' + d_large[10**9][1])

    x %= 10 ** 9

    millions = x // 10 ** 6
    if millions > 0:
        if millions == 1 and millions != 11:
            parts.append(d_large[10 ** 6][0])
        elif 2 <= billions <= 4:
            parts.append(number_to_words(millions) + ' ' + d_large[10 ** 6][2])
        else:
            parts.append(number_to_words(millions) + ' ' + d_large[10 ** 6][1])

    x %= 10 ** 6

    thousands = x // 1000
    if thousands > 0:
        if thousands == 1 and thousands != 11:
            parts.append(d_large[1000][0])
        elif thousands % 10 == 1 and thousands != 11:
            parts.append(number_to_words(thousands) + ' ')
        elif 2 <= thousands <= 4:
            parts.append(number_to_words(thousands) + ' ' + d_large[1000][2])
        else:
            parts.append(number_to_words(thousands) + ' ' + d_large[1000][1])

    x %= 1000

    if x >= 100:
        z = (x // 100) * 100
        parts.append(d_hundreds[z])
        x %= 100

    if x >= 20:
        z = (x // 10) * 10
        parts.append(d_tens[z])
        x %= 10

    if x >= 10:
        parts.append(d_teens[x])
        x = 0

    if x > 0:
        if previous_x % 10 == 1 and 1000 <= x <= 999999:
            parts.append(d_large[1000][0])
        else:
            parts.append(d_units[x])

    return ' '.join(parts).strip()


print(number_to_words(451000))
