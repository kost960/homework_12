secret_number = input('Введите загаданное число: ')
print('\n' * 25)

attempts = 10
guessed_numbers = []

while attempts > 0:
    tmp_secret_number = list(secret_number)
    bulls, cows = [], []

    guess_number = input('Введите число: ')
    if guess_number in guessed_numbers:
        print('Вы уже отгадывали это число. Попробуйте другое.')
        continue

    guessed_numbers.append(guess_number)

    for i in range(len(guess_number)):
        for j in range(len(tmp_secret_number)):

            if guess_number[i] == tmp_secret_number[j] and i == j:
                if j in bulls:
                    continue
                if j in cows:
                    cows.remove(j)
                bulls.append(j)
                break
            elif guess_number[i] == tmp_secret_number[j] and i != j:
                if j in cows or j in bulls:
                    continue
                cows.append(j)
                break

    attempts -= 1

    print(f'Быков: {len(bulls)}, Коров: {len(cows)}')

    if guess_number == secret_number:
        print('Победа!')
        break

else:
    print('Проигрыш! Загаданное число было:', secret_number)
