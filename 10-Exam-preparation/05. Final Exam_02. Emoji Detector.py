import re
text = input()
pattern_1 = r"[\d]"
digit = re.findall(pattern_1, text)
digit = [int(el)for el in digit]
threshold = 1
for el in digit:
    threshold *= el
# pattern = r'(^|(?<=\s))([:*]{2})[A-Z][a-z]{2}([a-z]+)?(\2)($|(?=[\s,.]))'
pattern = r'(\:\:|\*\*)[A-Z][a-z]{2,}(\1)'
valid_emojis = re.finditer(pattern, text)
emojis = [emoji.group() for emoji in valid_emojis ]
matched_emojis = []
coolness = 0
for el in emojis:
    current_emojii = [ord(i) for i in el if i.isalpha()]
    coolness = sum(current_emojii)
    if coolness >= threshold:
        matched_emojis.append(el)
print(f'Cool threshold: {threshold}')
print(f'{len(emojis)} emojis found in the text. The cool ones are:')
if len(matched_emojis) > 0:
    print(*matched_emojis, sep='\n')
