import re

data = input()
pattern = r"\d+"
numbers = []
while data:
    numbers.extend(re.findall(pattern, data))
    data = input()
print(*numbers, sep=" ")
