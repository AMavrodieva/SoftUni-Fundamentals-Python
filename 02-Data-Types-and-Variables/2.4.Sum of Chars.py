number_of_char = int(input())
sum_of_chars = 0
for i in range(1, number_of_char+1):
    sum_of_chars += ord(input())
print(f"The sum equals: {sum_of_chars}")
