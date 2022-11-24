message = input()
command = input()

while command != "Reveal":
    current_command = command.split(":|:")
    if current_command[0] == "InsertSpace":
        given_index = int(current_command[1])
        message = message[0:given_index] + " " + message[given_index:]
        print(message)
    if current_command[0] == "Reverse":
        substring = current_command[1]
        if substring in message:
            message = message.replace(substring, "", 1)
            message = message + substring[::-1]
            print(message)
        else:
            print(f'error')
    if current_command[0] == "ChangeAll":
        substring = current_command[1]
        replacement = current_command[2]
        message = message.replace(substring, replacement)
        print(message)
    command = input()
print(f'You have a new text message: {message}')
