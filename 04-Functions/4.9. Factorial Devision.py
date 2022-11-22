# factorial от 5 = 5! Изчислява се по следния начин:
# 5! = 5*4*3*2*1 = 120

def factorial_devision(first_number, second_number):
    factorial_1 = 1
    factorial_2 = 1
    for number in range(1, first_number + 1):
        factorial_1 = factorial_1 * number
    for number in range(1, second_number + 1):
        factorial_2 = factorial_2 * number
    return [factorial_1, factorial_2]


first_number = int(input())
second_number = int(input())
result = factorial_devision(first_number, second_number)
divide_result = result[0] / result[1]
print(f'{divide_result:.2f}')