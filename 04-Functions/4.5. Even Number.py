def even_numbers(x):
    if x % 2 == 0:
        return True
    return False


numbers = input().split()
int_number = [int(el) for el in numbers]
even = filter(even_numbers, int_number)
print(list(even))
