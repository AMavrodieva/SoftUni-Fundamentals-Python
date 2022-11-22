all_value = input().split("#")
amount_of_water = int(input())
total_effort = 0
total_fire = 0
value_cells = []
for cell in all_value:
    current_cell = cell.split(" = ")
    type_of_fire = current_cell[0]
    cell_value = int(current_cell[-1])
    if type_of_fire == "High":
        if not 81 <= cell_value <= 125:
            continue
    elif type_of_fire == "Medium":
        if not 51 <= cell_value <= 80:
            continue
    elif type_of_fire == "Low":
        if not 1 <= cell_value <= 50:
            continue
    if amount_of_water < cell_value:
        continue
    value_cells.append(cell_value)
    amount_of_water -= cell_value
    total_effort += cell_value * 0.25
    total_fire += cell_value
print("Cells:")
for cell in value_cells:
    print(f" - {cell}")
print(f"Effort: {total_effort:.2f}")
print(f"Total Fire: {total_fire}")
