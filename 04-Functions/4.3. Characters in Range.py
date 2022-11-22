def characters_in_range(first_char, second_char):
    list_of_chars = []
    result = []
    for i in range(ord(first_char)+1, ord(second_char)):
        list_of_chars.append(i)
    for j in list_of_chars:
        result.append(chr(j))
    new_char = ' '.join(result)
    return new_char


first_char = input()
second_char = input()
print(characters_in_range(first_char, second_char))
