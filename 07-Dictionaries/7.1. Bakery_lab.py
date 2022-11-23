text = input().split()
bakery = {}

for index in range(0, len(text), 2):
    key = text[index]
    value = int(text[index+1])
    bakery[key] = value
print(bakery)

