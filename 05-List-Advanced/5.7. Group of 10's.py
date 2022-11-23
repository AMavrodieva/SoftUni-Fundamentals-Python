number = [int(num) for num in input().split(", ")]
group = 10

while number:
    nums_group = []
    for nums in number:
        if nums in range(group-10, group+1):
            nums_group.append(nums)
    for nums in nums_group:
        number.remove(nums)
    print(f"Group of {group}'s: {nums_group} ")
    group += 10
