data = input().split()

first_text = [ord(el) for el in data[0]]
second_text = [ord(el) for el in data[1]]
total_sum = 0
shorter_text = min(len(first_text), len(second_text))
for i in range(shorter_text):
    total_sum += first_text[i] * second_text[i]

longer_text = max(len(first_text), len(second_text))
for j in range(shorter_text, longer_text):
    if len(first_text) > len(second_text):
        total_sum += first_text[j]
    else:
        total_sum += second_text[j]

print(total_sum)


