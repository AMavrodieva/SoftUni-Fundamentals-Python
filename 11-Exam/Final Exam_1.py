def replace(text, current_command):
    current_char = current_command[1]
    new_char = current_command[2]
    text = text.replace(current_char, new_char)
    print(text)
    return text


def remove(text, current_command):
    substring = current_command[1]
    text = text.replace(substring, "")
    print(text)
    return text


def includes(text, current_command):
    string = current_command[1]
    if string in text:
        print("True")
    else:
        print("False")
    return text


def change(text, current_command):
    sensitives = current_command[1]
    if sensitives == "Lower":
        text = text.lower()
    else:
        text = text.upper()
    print(text)
    return text


def reverse(text, current_command):
    start_index = int(current_command[1])
    end_index = int(current_command[2])
    if start_index in range(len(text)) and end_index in range(len(text)):
        text_to_reverse = text[start_index:end_index+1]
        reversed_text = text_to_reverse[::-1]
        #new_text = text[start_index] + reversed_text + text[end_index+1:]
        print(reversed_text)
    return text


text = input()
command = input()
while command != "Easter":
    current_command = command.split()
    action = current_command[0]
    if action == "Replace":
        text = replace(text, current_command)
    elif action == "Remove":
        text = remove(text, current_command)
    elif action == "Includes":
        text = includes(text, current_command)
    elif action == "Change":
        text = change(text, current_command)
    elif action == "Reverse":
        text = reverse(text, current_command)
    command = input()
