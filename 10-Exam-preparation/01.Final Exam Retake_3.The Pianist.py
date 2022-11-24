def add(piece, composer, key):
    if piece in piece_list:
        print(f'{piece} is already in the collection!')
    else:
        piece_list[piece] = {'Composer': composer, 'key': key}
        print(f'{piece} by {composer} in {key} added to the collection!')
    return piece_list


def remove(piece):
    if piece in piece_list:
        print(f'Successfully removed {piece}!')
        piece_list.pop(piece)
    else:
        print(f'Invalid operation! {piece} does not exist in the collection.')
    return piece_list


def changekey(piece, new_key):
    if piece in piece_list:
        print(f'Changed the key of {piece} to {new_key}!')
        piece_list[piece]['key'] = new_key
    else:
        print(f'Invalid operation! {piece} does not exist in the collection.')
    return piece_list


number = int(input())
piece_list = {}
for i in range(number):
    piece, composer, key_piece = input().split("|")
    if piece not in piece_list:
        piece_list[piece] = {'Composer': composer, 'key': key_piece}
    else:
        continue
command = input()
while command != "Stop":
    current_command = command.split("|")
    if current_command[0] == "Add":
        piece = current_command[1]
        composer = current_command[2]
        key_piece = current_command[3]
        piece_list = add(piece, composer, key_piece)
    if current_command[0] == "Remove":
        piece = current_command[1]
        piece_list = remove(piece)
    if current_command[0] == "ChangeKey":
        piece = current_command[1]
        new_key = current_command[2]
        piece_list = changekey(piece, new_key)
    command = input()
for piece, value in piece_list.items():
    composer = value['Composer']
    key_piece = value['key']
    print(f'{piece} -> Composer: {composer}, Key: {key_piece}')
