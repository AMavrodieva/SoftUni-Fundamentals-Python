import re

text = input()
pattern = r"(?<=\s_)[a-zA-Z0-9]+\b"

searched_word = [word.group() for word in re.finditer(pattern, text)]
print(*searched_word, sep=",")
