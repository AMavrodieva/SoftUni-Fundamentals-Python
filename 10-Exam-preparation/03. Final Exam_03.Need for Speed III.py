def drive(cars, current_command):
    current_car = current_command[1]
    distance = int(current_command[2])
    needed_fuel = int(current_command[3])
    if cars[current_car]['fuel'] >= needed_fuel:
        cars[current_car]['fuel'] -= needed_fuel
        cars[current_car]['mileage'] += distance
        print(f'{current_car} driven for {distance} kilometers. {needed_fuel} liters of fuel consumed.')
    else:
        print(f'Not enough fuel to make that ride')
    if cars[current_car]['mileage'] >= 100000:
        print(f'Time to sell the {current_car}!')
        cars.pop(current_car)
    return cars


def refuel(cars, current_command):
    current_car = current_command[1]
    litters_fuel = int(current_command[2])
    if cars[current_car]['fuel'] + litters_fuel >= 75:
        litters_fuel = 75 - cars[current_car]['fuel']
        cars[current_car]['fuel'] += litters_fuel
    else:
        cars[current_car]['fuel'] += litters_fuel
    print(f'{current_car} refueled with {litters_fuel} liters')
    return cars


def revert(cars, current_command):
    current_car = current_command[1]
    kilometers = int(current_command[2])
    if cars[current_car]['mileage'] - kilometers < 10000:
        cars[current_car]['mileage'] = 10000
    else:
        cars[current_car]['mileage'] -= kilometers
        print(f'{current_car} mileage decreased by {kilometers} kilometers')
    return cars


number_of_cars = int(input())
cars = {}
for i in range(number_of_cars):
    car, mileage, fuel = input().split("|")
    cars[car] = {'mileage': int(mileage), 'fuel': int(fuel)}
command = input()
while command != "Stop":
    current_command = command.split(" : ")
    if current_command[0] == "Drive":
        drive(cars, current_command)
    if current_command[0] == "Refuel":
        refuel(cars, current_command)
    if current_command[0] == "Revert":
        revert(cars, current_command)
    command = input()
for car, value in cars.items():
    print(f'{car} -> Mileage: {value["mileage"]} kms, Fuel in the tank: {value["fuel"]} lt.')
