number = int(input())
word = input()
string = []
for i in range(1, number+1):
    current_word = input()
    string.append(current_word)
print(string)
for j in range(len(string)-1, -1, -1):
    element = string[j]
    if word not in element:
        string.remove(element)
print(string)

