def word(letters, counts):
    return letters * counts


string = input()
counter = int(input())
print(word(string, counter))

# втори вариант
string = input()
counter = int(input())
repeat_string = lambda a, b: a * b

print(repeat_string(string, counter))
