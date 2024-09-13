strings = ('Python\n'
           'Hello\n'
           'World\n')

string_1, string_2, string_3 = strings.lower().split()

for symbol in string_1:
    if symbol in string_1 and symbol not in string_2 and symbol not in string_3:
        print(symbol)

for symbol in string_2:
    if symbol in string_2 and symbol not in string_1 and symbol not in string_3:
        print(symbol)

for symbol in string_3:
    if symbol in string_3 and symbol not in string_1 and symbol not in string_2:
        print(symbol)
