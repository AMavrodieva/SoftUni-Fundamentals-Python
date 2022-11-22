list_of_integer = input().split(" ")
number_to_remove = int(input())
list_of_number = []
final_number = []
for num in list_of_integer:
    number = int(num)
    list_of_number.append(number)
for i in range(0, number_to_remove):
    min_number = min(list_of_number)
    list_of_number.remove(min_number)
for j in list_of_number:
    num_integer = str(j)
    final_number.append(num_integer)
print(", ".join(final_number))



