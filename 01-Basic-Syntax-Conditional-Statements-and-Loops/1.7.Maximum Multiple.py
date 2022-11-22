import sys
divisor = int(input())
bound = int(input())
max_number = -sys.maxsize
for number in range(divisor+1, bound+1):
    if number % divisor == 0:
        if max_number < number:
            max_number = number
            continue
print(max_number)