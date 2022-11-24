import re

text = input()
pattern = r"(^|(?<=\s))[a-zA-Z0-9][A-Za-z0-9\._-]+@[a-z-]+\.[a-z]+(\.[a-z]+)?"

valid_mail = [mail.group() for mail in re.finditer(pattern, text)]
print(*valid_mail, sep="\n")
