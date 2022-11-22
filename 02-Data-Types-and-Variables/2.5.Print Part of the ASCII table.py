start_char_index = int(input())
last_char_index = int(input())
for i in range(start_char_index, last_char_index+1):
    chars = chr(i)
    print(f"{chars}", end=" ")
