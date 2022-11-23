text = input().split()
final_text = ""
for el in text:
    final_text += el * len(el)
print(final_text)
