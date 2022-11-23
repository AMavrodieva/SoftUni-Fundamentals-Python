number_of_commands = int(input())
database = {}
for _ in range(0, number_of_commands):
    command = input().split()
    user_name = command[1]
    if len(command) == 3:
        license_plate_number = command[2]
        if user_name not in database:
            database[user_name] = license_plate_number
            print(f'{user_name} registered {license_plate_number} successfully')
        else:
            print(f'ERROR: already registered with plate number {license_plate_number}')
    else:
        if user_name not in database:
            print(f'ERROR: user {user_name} not found')
        else:
            database.pop(user_name)
            print(f'{user_name} unregistered successfully')
for user_name, license_plate_number in database.items():
    print(f'{user_name} => {license_plate_number}')
