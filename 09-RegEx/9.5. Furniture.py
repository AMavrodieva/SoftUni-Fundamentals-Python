import re

command = input()
pattern = r">>(?P<furniture>[A-Z][A-Za-z]+)<<(?P<price>[0-9]+(\.[0-9]+)?)\!(?P<quantity>\d+)"
total_cost = 0
list_of_furniture = []
while command != "Purchase":
    match = re.match(pattern, command)
    if match:
        current_furniture = match.groupdict()
        total_cost += float(current_furniture['price'])*int(current_furniture['quantity'])
        list_of_furniture.append(current_furniture['furniture'])
    command = input()
print(f'Bought furniture:')
if list_of_furniture:
    print(*list_of_furniture, sep="\n")
print(f'Total money spend: {total_cost:.2f}')


