def add_and_subtract(first, second, third):
    sum_n = first + second
    result = sum_n - third
    return result

first = int(input())
second = int(input())
third = int(input())

result = add_and_subtract(first, second, third)
print(result)
