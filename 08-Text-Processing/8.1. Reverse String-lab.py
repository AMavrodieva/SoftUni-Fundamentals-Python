word = input()

while word != "end":
    reversed_word = word[::-1]
    print(f'{word} = {reversed_word}')
# print(f"{word} = {word[::-1]}")
    word = input()

