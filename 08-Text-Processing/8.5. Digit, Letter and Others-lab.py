text = input()
digit = ""
letters = ""
symbols = ""
for char in text:
    if char.isdigit():
        digit += char
    elif char.isalpha():
        letters += char
    else:
        symbols += char
print(digit)
print(letters)
print(symbols)
