hint = input('Введите подсказку: ')
secret_word = input('Введите загаданное слово: ').lower()
print('\n' * 25)

attempts = 10
guessed_letters = []
current_progress = list('*' * len(secret_word))

print(f'Подсказка: {hint}')
print('Слово: ', end='')
print(*current_progress, sep='')

while attempts > 0:
    choice = input('Буква или слово (0 - буква, 1 - слово)? ')

    if choice == '0':
        letter = input('Введите букву: ').lower()
        if letter in guessed_letters:
            print('Вы уже отгадывали эту букву. Попробуйте другую.')
            continue

        guessed_letters.append(letter)

        if letter in secret_word:
            for i in range(len(secret_word)):
                if letter == secret_word[i].lower():
                    current_progress[i] = secret_word[i]
            print('Правильно!')
        else:
            attempts -= 1
            print('Неверно!')

    elif choice == '1':
        guess = input('Введите слово: ').lower()
        if guess == secret_word:
            print('Победа!')
            break
        else:
            attempts -= 1
            print('Неверно!')

    print('Слово: ', end='')
    print(*current_progress, sep='')

    if current_progress == secret_word:
        print('Победа!')
        break

else:
    print('Проигрыш! Загаданное слово было:', secret_word)
