def check(input_text):
    stack = []
    brackets_open = ('(', '{', '[')
    brackets_closed = (')', '}', ']')
    for symbol in input_text:
        if symbol in brackets_open:
            stack.append(symbol)
        if symbol in brackets_closed:
            if len(stack) == 0:
                return False
            index = brackets_closed.index(symbol)
            open_bracket = brackets_open[index]
            if stack[-1] == open_bracket:
                stack.pop(-1)
            else:
                return False

    if len(stack) == 0:
        return True

    return False


print(check('Я устал (очень)'))
