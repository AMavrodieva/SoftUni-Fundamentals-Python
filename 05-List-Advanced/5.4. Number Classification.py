numbers = input().split(", ")
even = []
odd = []
positive = [el for el in numbers if int(el) >= 0]
negative = [el for el in numbers if int(el) < 0]
number = [even.append(el) if int(el) % 2 == 0 else odd.append(el) for el in numbers]
positive = ", ".join(positive)
negative = ", ".join(negative)
even = ", ".join(even)
odd = ", ".join(odd)
print(f"Positive: {positive}")
print(f"Negative: {negative}")
print(f"Even: {even}")
print(f"Odd: {odd}")


