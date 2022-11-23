def is_house_exist(text, current_index):
    if current_index in range(0, len(text)):
        return True
    return False


house_hearth = [int(el) for el in input().split("@")]
command = input()
current_position = 0
current_index = 0
while command != "Love!":
    jump = command.split()
    jump_lenght = int(jump[1])
    current_index = current_index + jump_lenght
    current_position = current_index
    if is_house_exist(house_hearth, current_index):
        if house_hearth[current_index] > 0:
            house_hearth[current_index] -= 2
            if house_hearth[current_index] == 0:
                print(f"Place {current_position} has Valentine's day.")
        elif house_hearth[current_index] == 0:
            print(f"Place {current_position} already had Valentine's day.")
    else:
        current_index = 0
        current_position = current_index
        if house_hearth[current_index] > 0:
            house_hearth[current_index] -= 2
            if house_hearth[current_index] == 0:
                print(f"Place {current_position} has Valentine's day.")
        elif house_hearth[current_index] == 0:
            print(f"Place {current_position} already had Valentine's day.")
    command = input()
print(f"Cupid's last position was {current_position}.")
final_heart = [str(el) for el in house_hearth if int(el) != 0]
final_heart = list(final_heart)
# final_heart = list(set(house_hearth))
if len(final_heart) > 0:
    print(f"Cupid has failed {len(final_heart)} places.")
else:
    print(f"Mission was successful.")
