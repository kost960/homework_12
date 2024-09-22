def get_expression_value(input_expression):
    input_expression = input_expression.replace(' ', '')

    actions = {'+': 1,
               '-': 1,
               '*': 2,
               '/': 2
               }

    def take_action(operators, values):
        operator = operators.pop()
        right = values.pop()
        left = values.pop()

        if operator == '+':
            values.append(left + right)
        elif operator == '-':
            values.append(left - right)
        elif operator == '*':
            values.append(left * right)
        elif operator == '/':
            values.append(left / right)

    def high_action(operator_1, operator_2):
        return actions[operator_1] > actions[operator_2]

    operators_stack = []
    values_stack = []

    i = 0
    while i < len(input_expression):
        if input_expression[i].isdigit():
            num = 0

            while i < len(input_expression) and input_expression[i].isdigit():
                num = num * 10 + int(input_expression[i])
                i += 1

            values_stack.append(num)
            continue

        if input_expression[i] in actions:
            while operators_stack and operators_stack[-1] in actions:
                if high_action(operators_stack[-1], input_expression[i]):
                    take_action(operators_stack, values_stack)
                else:
                    break
            operators_stack.append(input_expression[i])
        elif input_expression[i] == '(':
            operators_stack.append(input_expression[i])
        elif input_expression[i] == ')':
            while operators_stack and operators_stack[-1] != '(':
                take_action(operators_stack, values_stack)
            operators_stack.pop()

        i += 1

    while operators_stack:
        take_action(operators_stack, values_stack)

    return values_stack[0]


print(get_expression_value('2 + 3 * (4 - 1)'))
