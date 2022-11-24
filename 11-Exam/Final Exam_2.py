import re

pattern = r"(?P<name>[A-Z][a-z]{2,}\s[A-Z][a-z]{2,})[#]{1,}(?P<position>[A-Z][A-Za-z]+((&[A-Z][A-Za-z]+)+)?)[\d]{2}" \
          r"(?P<company>[A-Z][A-Za-z0-9]+\s(JSC|Ltd\.))"

number = int(input())
for el in range(0, number):
    data = input()
    valid_name = re.match(pattern, data)
    if valid_name:
        employees = valid_name.groupdict()
        current_position = employees['position'].replace("&", " ")
        print(f'{employees["name"]} is {current_position} at {employees["company"]}')
