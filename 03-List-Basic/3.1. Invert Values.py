numbers_string = input().split(" ")
numbers_inversed = []
for number in numbers_string:
    element = int(number)
    element *= -1
    numbers_inversed.append(element)
print(numbers_inversed)

