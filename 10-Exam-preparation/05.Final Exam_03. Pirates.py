def plunder(cities, current_command):
    town = current_command[1]
    people = int(current_command[2])
    steal_gold = int(current_command[3])
    cities[town]['population'] -= people
    cities[town]['gold'] -= steal_gold
    print(f'{town} plundered! {steal_gold} gold stolen, {people} citizens killed.')
    if cities[town]['population'] <= 0 or cities[town]['gold'] <= 0:
        print(f'{town} has been wiped off the map!')
        cities.pop(town)
    return cities


def prosper(cities, current_command):
    town = current_command[1]
    given_gold = int(current_command[2])
    if given_gold < 0:
        print(f'Gold added cannot be a negative number!')
    else:
        cities[town]['gold'] += given_gold
        print(f'{given_gold} gold added to the city treasury. {town} now has {cities[town]["gold"]} gold.')
    return cities


command = input()
cities = {}
while command != "Sail":
    city, population, gold = command.split("||")
    if city not in cities:
        cities[city] = {"population": 0, "gold": 0}
    cities[city]['population'] += int(population)
    cities[city]['gold'] += int(gold)
    command = input()
second_command = input()
while second_command != "End":
    current_command = second_command.split("=>")
    if current_command[0] == "Plunder":
        cities = plunder(cities, current_command)
    if current_command[0] == "Prosper":
        cities = prosper(cities, current_command)
    second_command = input()
if len(cities) > 0:
    print(f'Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:')
    for city, value in cities.items():
        print(f'{city} -> Population: {value["population"]} citizens, Gold: {value["gold"]} kg')
else:
    print(f'Ahoy, Captain! All targets have been plundered and destroyed!')
