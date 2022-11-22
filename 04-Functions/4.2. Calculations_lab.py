def parameters(operator, num_1, num_2):
    if operator == "multiply":
        return num_1 * num_2
    elif operator == "divide":
        return num_1 / num_2
    elif operator == "add":
        return num_1 + num_2
    elif operator == "subtract":
        return num_1 - num_2


used_operator = input()
number_1 = int(input())
number_2 = int(input())

result = parameters(used_operator, number_1, number_2)
print(f"{result:.0f}")
