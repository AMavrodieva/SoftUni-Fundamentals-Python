list_of_gift = input().split(" ")
command = input()
final_list = []
while command != "No Money":
    current_command = command.split()
    current_gift = current_command[1]
    if current_command[0] == "OutOfStock":
        for index in range(len(list_of_gift)):
           if list_of_gift[index] == current_gift:
               list_of_gift[index] = "None"
    elif current_command[0] == "Required":
        index = int(current_command[2])
        if 0 < index < len(list_of_gift):
            list_of_gift[index] = current_gift
    elif current_command[0] == "JustInCase":
        list_of_gift[-1] = current_gift
    command = input()
for gift in list_of_gift:
    if gift != "None":
      final_list.append(gift)
print(" ".join(final_list), end="")


