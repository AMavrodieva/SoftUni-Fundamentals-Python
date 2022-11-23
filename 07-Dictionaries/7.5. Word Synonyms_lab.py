number_of_words = int(input())
dictionary = {}
for _ in range(0, number_of_words):
    words = input()
    synonyms = input()
    if words not in dictionary:
        dictionary[words] = []
    dictionary[words].append(synonyms)
for key, value in dictionary.items():
    #list_value = ", ".join(value)
    #print(f"{key} - {list_value}")
    print(f"{key} - {', '.join(value)}")