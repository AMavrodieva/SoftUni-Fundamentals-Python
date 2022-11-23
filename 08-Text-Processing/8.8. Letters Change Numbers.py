data = input().split()
result = 0
alphabet = [chr(el) for el in range(ord('A'), ord('Z')+1)]
for el in data:
    first_letter = el[0]
    second_letter = el[-1]
    number = int(el[1:-1])
    if ord(first_letter) in range(ord('A'), ord('Z') + 1):
        position = alphabet.index(first_letter) + 1
        result += number / position
    else:
        position = alphabet.index(first_letter.upper()) + 1
        result += number * position
    if ord(second_letter) in range(ord('A'), ord('Z') + 1):
        position = alphabet.index(second_letter) + 1
        result -= position
    else:
        position = alphabet.index(second_letter.upper()) + 1
        result += position
print(f'{result:.2f}')


