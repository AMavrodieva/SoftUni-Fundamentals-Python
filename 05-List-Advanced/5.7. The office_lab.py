employees = input().split(" ")
factor = int(input())
employees = list(map(lambda x: int(x) * factor, employees))
employees_happiness_above_average = list(filter(lambda x: x >= (sum(employees) / len(employees)), employees))
if len(employees_happiness_above_average) >= len(employees) / 2:
    print(f"Score: {len(employees_happiness_above_average)}/{len(employees)}. Employees are happy!")
else:
    print(f"Score: {len(employees_happiness_above_average)}/{len(employees)}. Employees are not happy!")