def rate(plants_info, activity):
    plant_name, rating = activity.split(" - ")
    rating = int(rating)
    if plant_name in plants_info:
        plants_info[plant_name]['plant_rating'].append(rating)
    return plants_info


def update(plants_info, activity):
    current_plant, new_rarity = activity.split(" - ")
    new_rarity = int(new_rarity)
    #current_plant = current_plant.strip()
    if current_plant in plants_info:
        plants_info[current_plant]['plant_rarity'] = new_rarity
    return plants_info


def reset(plants_info, activity):
    current_plant = activity.strip()
    if current_plant in plants_info:
        plants_info[current_plant]['plant_rating'].clear()
    return plants_info


number = int(input())
plants_info = {}
for i in range(number):
    plant, plant_rarity = input().split("<->")
    plant_rarity = int(plant_rarity)
    plants_info[plant] = {"plant_rarity": plant_rarity, "plant_rating": []}
command = input()
while command != "Exhibition":
    current_command, activity = command.split(": ")
    if current_command == "Rate":
        plants_info = rate(plants_info, activity)
    if current_command == "Update":
        plants_info = update(plants_info, activity)
    if current_command == "Reset":
        plants_info = reset(plants_info, activity)
    command = input()

for plant, value in plants_info.items():
    if value['plant_rating']:
        average_rating = sum(value['plant_rating']) / len(value['plant_rating'])
    else:
        average_rating = 0
    plants_info[plant]['average_rating'] = average_rating
sorted_plant = sorted(plants_info.items(), key=lambda kvp: (-kvp[1]['plant_rarity']))
#sorted_plant = sorted(plants_info.items(), key=lambda kvp: (kvp, -kvp[1]['plant_rarity'], -kvp[1]['average_rating']), reverse=False)
print(f'Plants for the exhibition:')
for plant, value in sorted_plant:
    print(f'- {plant}; Rarity: {value["plant_rarity"]}; Rating: {value["average_rating"]:.2f}')
