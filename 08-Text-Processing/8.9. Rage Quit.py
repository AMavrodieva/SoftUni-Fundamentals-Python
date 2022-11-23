text = input()
mid_list = []
final_list = []
multiplier = ''
upper_letter = [el.upper() if el.isalpha() else el for el in text]
for index in range(len(upper_letter)):
    symbol = upper_letter[index]
    if not symbol.isdigit():
        mid_list.append(symbol)
    if index != len(upper_letter) -1 and symbol.isdigit():
        multiplier += symbol
        if not upper_letter[index+1].isdigit():
            mid_list = mid_list * int(multiplier)
            final_list.extend(mid_list)
            mid_list = []
            multiplier = ''
    if index == len(upper_letter) - 1:
        multiplier += symbol
        mid_list *= int(multiplier)
        final_list.extend(mid_list)
unique_symbol = set(final_list)
print(f'Unique symbols used: {len(unique_symbol)}')
print(*final_list, sep='')

# втори вариант
text = input()
mid_list = ''
final_list = ''
multiplier = ""
for index in range(len(text)):
    symbol = text[index]
    if not symbol.isdigit():
        mid_list += symbol
    if index != len(text) - 1 and symbol.isdigit():
        multiplier += symbol
        if not text[index+1].isdigit():
            final_list += mid_list.upper() * int(multiplier)
            mid_list = ''
            multiplier = ""
    if index == len(text)-1:
        if symbol.isdigit():
            multiplier += symbol
            final_list += mid_list.upper() * int(multiplier)
        else:
            final_list += symbol
unique_symbol = set(final_list)
print(f'Unique symbols used: {len(unique_symbol)}')
print(*final_list, sep='')