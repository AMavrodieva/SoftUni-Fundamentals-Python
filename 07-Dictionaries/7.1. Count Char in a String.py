words = input().split()
chars = {}
for word in words:
    for letter in word:
        if letter not in chars:
            chars[letter] = 0
        chars[letter] += 1
for key, value in chars.items():
    print(f"{key} -> {value}")
