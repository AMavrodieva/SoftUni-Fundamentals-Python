def check_index_exist(target_list, current_index):
    if current_index in range(0, len(target_list)):
        return True
    return False


target = [int(el) for el in input().split()]
command = input()
while command != "End":
    current_command, index_value, value = command.split()
    current_index = int(index_value)
    if current_command == "Shoot":
        if check_index_exist(target, current_index):
            power = int(value)
            current_target = target[current_index]
            if current_target <= power:
                target.remove(current_target)
            else:
                target[current_index] -= power
        else:
            command = input()
            continue
    elif current_command == "Add":
        if check_index_exist(target, current_index):
            value = int(value)
            target.insert(current_index, value)
        else:
            print("Invalid placement!")
    elif current_command == "Strike":
        radius = int(value)
        if check_index_exist(target, int(current_index)):
            start_index = int(current_index) - int(radius)
            end_index = int(current_index) + int(radius)
            if start_index in range(len(target)) and end_index in range(len(target)):
                del target[start_index:end_index + 1]
            else:
                print("Strike missed!")
                command = input()
                continue
        else:
            print("Strike missed!")

    command = input()
target = [str(el) for el in target]
print(f"{'|'.join(target)}")
