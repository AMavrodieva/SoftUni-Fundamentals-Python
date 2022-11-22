numbers = input().split()
list_of_nums_ascending = list(sorted(numbers, key=lambda x: int(x), reverse=False))
list_of_nums = [int(el) for el in list_of_nums_ascending]
print(list_of_nums)


