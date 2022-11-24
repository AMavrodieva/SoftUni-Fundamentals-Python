import re

data = input()
pattern = r"(^|(?<=\s))(\d+|-\d+)(\.\d+)?($|(?=\s))"
matched_numbers = [number.group() for number in re.finditer(pattern, data)]
print(*matched_numbers, sep=" ")
