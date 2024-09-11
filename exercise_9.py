string = 'Сделал дело - делай дело'

split_string = string.split()
for word in split_string:
    if word.isalpha() and split_string.count(word) == 2:
        print(word)
