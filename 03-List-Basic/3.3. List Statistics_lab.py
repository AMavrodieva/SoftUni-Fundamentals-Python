number_integers = int(input())
positive_numbers = []
negative_numbers = []
for i in range(1, number_integers+1):
    number = int(input())
    if number >= 0:
        positive_numbers.append(number)
    else:
        negative_numbers.append(number)
print(positive_numbers)
print(negative_numbers)
print(f"Count of positives: {len(positive_numbers)}. Sum of negatives: {sum(negative_numbers)}")
