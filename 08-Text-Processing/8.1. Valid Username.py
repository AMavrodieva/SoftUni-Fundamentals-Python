usernames = input().split(", ")
valid_username = []
is_username_valid = False
valid_symbols = ["-", "_"]

for user in usernames:
    if 3 <= len(user) <= 16:
        is_username_valid = True
    else:
        continue
    for char in user:
        if not char.isdigit() and not char.isalpha() and char not in valid_symbols:
            is_username_valid = False
            break
    if is_username_valid:
        valid_username.append(user)
print('\n'.join(valid_username))


