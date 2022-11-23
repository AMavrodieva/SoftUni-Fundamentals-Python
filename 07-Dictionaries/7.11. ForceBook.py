def user_exist(sides:dict, force_user: str):
    for user_list in sides.values():
        if force_user in user_list:
            return True
    return False

def remove_user(sides:dict, force_user: str):
    for force_side, users in sides.items():
        if force_user in users:
            sides[force_side].remove(force_user)


def command_pipe(sides:dict, force_side: str, force_user:str):
    if force_side not in sides and not user_exist(sides, force_user):
        sides[force_side] = []
        sides[force_side].append(force_user)
    elif not user_exist(sides, force_user):
        sides[force_side].append(force_user)



def command_arrow(sides:dict, force_side: str, force_user:str):
    if force_side not in sides and not user_exist(sides, force_user):
        sides[force_side] = []
        sides[force_side].append(force_user)
    elif not user_exist(sides, force_user):
        if force_side not in sides:
            sides[force_side] = []
        sides[force_side].append(force_user)
    elif user_exist(sides, force_user):
        remove_user(sides, force_user)
        sides[force_side].append(force_user)

command = input()
sides = {}

while command != "Lumpawaroo":
    if "|" in command:
        force_side, force_user = command.split(" | ")
        command_pipe(sides, force_side, force_user)
    elif "->" in command:
        force_user, force_side = command.split(" -> ")
        command_arrow(sides, force_side, force_user)
        print(f'{force_user} joins the {force_side} side!')
    command = input()

for force_side, force_user in sides.items():
    if len(force_user) >= 1:
        print(f'Side: {force_side}, Members: {len(force_user)}')
        for i in range(0, len(force_user)):
            print(f'! {force_user[i]}')
