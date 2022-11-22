number_of_lines = int(input())
sum_of_liters = 0
while sum_of_liters < 250:
    for i in range(1, number_of_lines + 1):
        liters_of_water = int(input())
        sum_of_liters += liters_of_water
        if sum_of_liters > 255:
            print(f"Insufficient capacity!")
            sum_of_liters -= liters_of_water
            continue
    break
print(f"{sum_of_liters}")