import re

text = input()
pattern = r"w{3}\.[a-zA-Z0-9-]+(\.[a-z]+)+"

while text:
    valid_site = [site.group() for site in re.finditer(pattern, text)]
    if valid_site:
        print(*valid_site, sep="\n")
    text = input()
