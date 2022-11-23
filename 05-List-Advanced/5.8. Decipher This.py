secret_message = input().split()
for word in secret_message:
    number = ""
    for char in word:
        if char.isdigit():
            number += char
    first_letter = chr(int(number))
    current_word = list(first_letter + word[len(number):])
    current_word[1], current_word[-1] = current_word[-1], current_word[1]
    print(f"{''.join(current_word)}", end=" ")
