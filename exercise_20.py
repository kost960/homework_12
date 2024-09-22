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
    1000: ['тысяча', 'тысяч', 'тысячи'],
    10 ** 6: ['миллион', 'миллионов', 'миллиона'],
    10 ** 9: ['миллиард', 'миллиардов', 'миллиарда'],
}


def number_to_words(x):
    if x == 0:
        return d_units[0]

    parts = []

    for value in sorted(d_large.keys(), reverse=True):
        if x >= value:
            num = x // value
            x %= value
            if num % 10 == 1 and num % 100 != 11:
                parts.append(number_to_words(num) + ' ' + d_large[value][0])
            elif 2 <= num % 10 <= 4 and not (2 <= num % 100 <= 4):
                parts.append(number_to_words(num) + ' ' + d_large[value][2])
            else:
                parts.append(number_to_words(num) + ' ' + d_large[value][1])

    if x >= 100:
        z = (x // 100) * 100
        parts.append(d_hundreds[z])
        x %= 100

    if x >= 20:
        z = (x // 10) * 10
        parts.append(d_tens[z])
        x %= 10
    elif x >= 10:
        parts.append(d_teens[x])
        x = 0

    if x > 0:
        parts.append(d_units[x])

    return ' '.join(parts).strip()


print(number_to_words(121124000))