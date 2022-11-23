banner_list = input().split(", ")
text = input()

for banner_word in banner_list:
    text = text.replace(banner_word, "*" * len(banner_word))
print(text)