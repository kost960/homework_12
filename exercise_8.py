string = 'Сделал дело - гуляй смело'

split_string = string.split()
length = len(split_string)
i = 0
while i < length:
    if not split_string[i].isalpha():
        split_string.pop(i)
        length -= 1
    i += 1

for i in range(len(split_string) - 1):
    for j in range(len(split_string) - i - 1):
        if len(split_string[j]) > len(split_string[j + 1]):
            split_string[j], split_string[j + 1] = split_string[j + 1], split_string[j]

print(' '.join(split_string))
