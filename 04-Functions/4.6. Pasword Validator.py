def is_password_valid(text):
    is_valid = True
    count_numbers = 0
    if len(text) < 6 or len(text) >10:
        is_valid = False
        print(f'Password must be between 6 and 10 characters')

    for el in text:
        if el.isdigit():
            count_numbers += 1

    if not text.isalnum():
        is_valid = False
        print(f'Password must consist only of letters and digits')

    if count_numbers < 2:
        is_valid = False
        print(f'Password must have at least 2 digits')

    return is_valid


text = input()
result = is_password_valid(text)
if result:
    print(f'Password is valid')



