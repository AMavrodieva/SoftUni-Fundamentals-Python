card_string = input().split(" ")
count_of_faro_shuffles = int(input())
half_size = len(card_string) // 2


for i in range(count_of_faro_shuffles):
    left_side = card_string[0:half_size]
    right_side = card_string[half_size:]
    faro_card = []
    for j in range(len(left_side)):
        faro_card.append(left_side[j])
        faro_card.append(right_side[j])

    card_string = faro_card

print(card_string)

# вариант 2

number_string = input().split(" ")
number_card = len(number_string)
count_of_shuffles = int(input())
number_of_each_side = number_card // 2

for i in range(count_of_shuffles):
    left_side = number_string[0:number_of_each_side]
    right_side = number_string[number_of_each_side:]
    faro_shuffle = []
    for j in range(len(left_side)):
        faro_shuffle.append(left_side[j])
        faro_shuffle.append(right_side[j])

    number_string = faro_shuffle

print(number_string)
