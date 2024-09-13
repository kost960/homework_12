lucky_ticket = False
ticket_number = 1
while not lucky_ticket:
    input_ticket = input('Введите номер билета: ').strip()
    number_half = len(input_ticket) // 2

    if len(input_ticket) % 2 == 0:
        first_half_sum = sum([int(digit) for digit in input_ticket[0:number_half]])
        second_half_sum = sum([int(digit) for digit in input_ticket[number_half:]])
        if first_half_sum == second_half_sum:
            lucky_ticket = True
            print(f'Номер счастливого билета: {ticket_number}')

    ticket_number += 1
