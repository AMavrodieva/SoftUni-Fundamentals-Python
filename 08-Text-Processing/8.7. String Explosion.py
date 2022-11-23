data = input()
final_text = []
strength = 0
for index in range(len(data)):
    element = data[index]
    if element != ">":
        if not element.isdigit():
            if strength == 0:
                final_text.append(element)
            else:
                strength -= 1
                continue
        else:
            if int(element) > 1:
                strength += int(element) - 1
            continue
    else:
        final_text.append(element)
        continue
print(*final_text, sep='')


