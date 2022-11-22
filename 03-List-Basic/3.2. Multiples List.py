factor = int(input())
count = int(input())
final_number = factor * count
first_list = []
for numbers in range(factor, final_number+1):
    if numbers % factor == 0:
        first_list.append(numbers)
print(first_list)
