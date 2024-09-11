def check_identical_letters(word):
    letters_list = []
    for letter in word:
        if letter in letters_list:
            return False

    return True


string = 'Сделал дело - гуляй смело!'

split_string = string[:-1].split()
for i in range(1, len(split_string)):
    if check_identical_letters(split_string[i]) and split_string[i].isalpha() and split_string[0] != split_string[i]:
        print(split_string[i])
