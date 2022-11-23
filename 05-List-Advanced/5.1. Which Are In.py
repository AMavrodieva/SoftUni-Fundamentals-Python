substring_list = input().split(", ")
string_list = input().split(", ")

new_list = [substr for substr in substring_list for word in string_list if substr in word]
print(sorted(set(new_list), key=new_list.index))
