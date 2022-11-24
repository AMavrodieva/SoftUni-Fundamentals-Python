def flip(activation_key, current_command):
    sensitive = current_command[1]
    start_index = int(current_command[2])
    end_index = int(current_command[3])
    if sensitive == "Upper":
        activation_key= activation_key[0:start_index] + (activation_key[start_index:end_index]).upper()\
                           + activation_key[end_index:]
        print(activation_key)
    if sensitive == "Lower":
        activation_key = activation_key[0:start_index] + (activation_key[start_index:end_index]).lower() \
                            + activation_key[end_index:]
        print(activation_key)
    return activation_key


def slice(activation_key, current_command):
    start_index = int(current_command[1])
    end_index = int(current_command[2])
    activation_key = activation_key[0:start_index] + activation_key[end_index:]
    print(activation_key)
    return activation_key


activation_key = input()
command = input()
while command != "Generate":
    current_command = command.split(">>>")
    if current_command[0] == "Contains":
        substring = current_command[1]
        if substring in activation_key:
            print(f'{activation_key} contains {substring}')
        else:
            print(f'Substring not found!')
    elif current_command[0] == "Flip":
        activation_key = flip(activation_key, current_command)
    elif current_command[0] == "Slice":
        activation_key = slice(activation_key, current_command)
    command = input()
print(f'Your activation key is: {activation_key}')
