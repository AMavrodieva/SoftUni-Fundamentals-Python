import re

text = input()

pattern = r"\b[A-Z][a-z]+ [A-Z][a-z]+\b"

matched_name = re.findall(pattern, text)
print(*matched_name)
