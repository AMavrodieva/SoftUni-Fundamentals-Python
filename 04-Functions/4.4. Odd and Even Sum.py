def odd_even_numbers(number):
    odd_number = []
    even_number = []
    for el in number:
        el = int(el)
        if el % 2 == 0:
            even_number.append(el)
        else:
            odd_number.append(el)
    even = [int(el) for el in even_number]
    odd = [int(el) for el in odd_number]
    sum_even = sum(even)
    sum_odd = sum(odd)
    return [sum_odd, sum_even]


numbers = input()
result = odd_even_numbers(numbers)
print(f'Odd sum = {result[0]}, Even sum = {result[1]}')
