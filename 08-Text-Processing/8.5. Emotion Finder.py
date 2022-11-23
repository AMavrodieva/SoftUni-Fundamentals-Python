text = input()
emotions = []
for index in range(len(text)):
    if text[index] == ":":
        emotions.append(text[index] + text[index+1])
print('\n'.join(emotions))

# Вариант 2 с list comprehension
#emotion = [text[index] + text[index+1] for index in range(len(text)) if text[index] == ":"]
#print('\n'.join(emotion))
