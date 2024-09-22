def check(input_text):
    stack = []
    for symbol in input_text:
        if symbol == '(':
            stack.append(symbol)

        if symbol == ')':
            if len(stack) == 0:
                return False

            if stack[-1] == '(':
                stack.pop(-1)
            else:
                return False

    if len(stack) == 0:
        return True

    return False


print('Верно' if check('Я устал (очень)') else 'Неверно')
