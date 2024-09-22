def justify_text(input_text, input_line_length):
    words = input_text.split()
    lines = []

    current_line = []
    current_length = 0

    for word in words:
        if current_length + len(word) + len(current_line) > input_line_length:
            lines.append(justify_line(current_line, input_line_length))
            current_line = []
            current_length = 0

        current_line.append(word)
        current_length += len(word)

    if current_line:
        lines.append(' '.join(current_line))

    return '\n'.join(lines)


def justify_line(input_line, input_line_length):
    if len(input_line) == 1:
        return input_line[0]

    total_spaces = input_line_length - sum(len(word) for word in input_line)
    spaces_needed = len(input_line) - 1

    if spaces_needed > 0:
        min_space = total_spaces // spaces_needed
        extra_space = total_spaces % spaces_needed
        spaces = [min_space + (1 if i < extra_space else 0) for i in range(spaces_needed)]
    else:
        spaces = []

    justified_line = []
    for i, word in enumerate(input_line):
        justified_line.append(word)
        if i < len(spaces):
            justified_line.append(' ' * (spaces[i] + 1))

    return ''.join(justified_line)


text = input('Введите текст: ')
line_length = int(input('Введите ширину строки: '))

justified_text = justify_text(text, line_length)
print(justified_text)
