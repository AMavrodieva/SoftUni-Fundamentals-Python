number_string = input().split(", ")
count_of_beggars = int(input())
number = []
for num in number_string:
    number.append(num)
result_sum = [0] * count_of_beggars

for i in range(len(number)):
    index = i % count_of_beggars
    result_sum[index] += int(number[i])
print(result_sum)

# вариант 2

list_of_number = input().split(", ")
beggars = int(input())
result = [0] * beggars
for i in range(len(list_of_number)):
    index = i % beggars
    result[index] += int(list_of_number[i])
print(result)