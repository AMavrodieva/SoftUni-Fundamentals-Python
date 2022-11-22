def smallest_number(first, second, third):
    searched_number = min(first, second, third)
    return searched_number


first = int(input())
second = int(input())
third = int(input())
searched_number = smallest_number(first, second, third)
print(searched_number)
