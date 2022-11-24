def move(text, number_of_letters):
    text = text[number_of_letters:] + text[0:number_of_letters]
    # вариант с лист
    # text = list(text)
    # for index in range(0, number_of_letters):
    #     text.append(text[index])
    # del text[0:number_of_letters]
    # text = "".join(text)
    return text

def insert(text, current_index, value):
    text = text[0:current_index] + value + text[current_index:]
    return text


def change_all(text, substring, replacement):
    text = text.replace(substring, replacement)
    return text


text = input()
command = input()

while command != "Decode":
    instruction = command.split("|")
    if instruction[0] == "Move":
        number_of_letters = int(instruction[1])
        text = move(text, number_of_letters)
    elif instruction[0] == "Insert":
        current_index = int(instruction[1])
        value = instruction[2]
        text = insert(text, current_index, value)
    elif instruction[0] == "ChangeAll":
        substring = instruction[1]
        replacement = instruction[2]
        text = change_all(text, substring, replacement)
    command = input()
print(f'The decrypted message is: {text}')