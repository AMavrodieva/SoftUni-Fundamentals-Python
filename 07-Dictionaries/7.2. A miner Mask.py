data = input()
dictionary = {}

while data != "stop":
    resource = data
    value = int(input())
    if resource not in dictionary:
        dictionary[resource] = 0
    dictionary[resource] += value
    data = input()
for resource, value in dictionary.items():
    print(f"{resource} -> {value}")
