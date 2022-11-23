word = input()
vowels = ['a', 'o', 'u', 'e', 'i']
new_word = [letter for letter in word if letter.lower() not in vowels]
print("".join(new_word))
