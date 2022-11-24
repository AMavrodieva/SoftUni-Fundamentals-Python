import re
string = input()
pattern = r"([@#])([a-zA-Z]{3})([a-zA-Z]+)?(\1)(\1)([a-zA-z]{3})([a-zA-Z]+)?(\1)"

matched_string = re.finditer(pattern, string)
matched_as_list = [matched.group() for matched in matched_string]
count_word_pairs = len(matched_as_list)
if count_word_pairs >0:
    print(f'{count_word_pairs} word pairs found!')
else:
    print(f"No word pairs found!")
valid_str = "".join(matched_as_list)
pattern_1 = r"(?<=[#@])[a-zA-Z]+(?=[#@])"
valid_string = re.finditer(pattern_1, valid_str)
valid_word = [valid.group() for valid in valid_string]
list_word_mirror_pairs = []
for i in range(0, len(valid_word), 2):
    first_word = valid_word[i]
    second_word = valid_word[i+1]
    if first_word == second_word[::-1]:
        mirror_word = first_word + " <=> " + second_word
        list_word_mirror_pairs.append(mirror_word)
if len(list_word_mirror_pairs) >0:
    print(f'The mirror words are:')
    print(*list_word_mirror_pairs, sep=", ")
else:
    print("No mirror words!")
