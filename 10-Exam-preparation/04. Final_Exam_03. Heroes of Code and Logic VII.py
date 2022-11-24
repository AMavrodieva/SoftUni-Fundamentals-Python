def castspeel(heroes, current_command):
    name = current_command[1]
    mp_needed = int(current_command[2])
    spell_name = current_command[3]
    if heroes[name]["MP"] >= mp_needed:
        heroes[name]["MP"] -= mp_needed
        print(f'{name} has successfully cast {spell_name} and now has {heroes[name]["MP"]} MP!')
    else:
        print(f'{name} does not have enough MP to cast {spell_name}!')
    return heroes


def takadamage(heroes, current_command):
    name = current_command[1]
    damage = int(current_command[2])
    attacker = current_command[3]
    heroes[name]["HP"] -= damage
    if heroes[name]["HP"] >0:
        print(f'{name} was hit for {damage} HP by {attacker} and now has {heroes[name]["HP"]} HP left!')
    else:
        print(f'{name} has been killed by {attacker}!')
        heroes.pop(name)
    return heroes


def recharge(heroes, current_command):
    name = current_command[1]
    amount = int(current_command[2])
    if heroes[name]["MP"] + amount <= 200:
        heroes[name]["MP"] += amount
        print(f'{name} recharged for {amount} MP!')
    else:
        amount = 200 - heroes[name]["MP"]
        heroes[name]["MP"] += amount
        print(f'{name} recharged for {amount} MP!')
    return heroes


def heal(heroes, current_command):
    name = current_command[1]
    amount = int(current_command[2])
    if heroes[name]["HP"] + amount <= 100:
        heroes[name]["HP"] += amount
        print(f'{name} healed for {amount} HP!')
    else:
        amount = 100 - heroes[name]["HP"]
        heroes[name]["HP"] += amount
        print(f'{name} healed for {amount} HP!')
    return heroes


number_of_heroes = int(input())
heroes = {}
for _ in range(number_of_heroes):
    hero_name, hit_points, mana_points = input().split()
    heroes[hero_name] = {'HP': int(hit_points), 'MP': int(mana_points)}
    if heroes[hero_name]["HP"] > 100:
        heroes[hero_name]["HP"] = 100
    if heroes[hero_name]["MP"] > 200:
        heroes[hero_name]["MP"] = 200
command = input()
while command != "End":
    current_command = command.split(" - ")
    if current_command[0] == "CastSpell":
        castspeel(heroes, current_command)
    if current_command[0] == "TakeDamage":
        takadamage(heroes, current_command)
    if current_command[0] == "Recharge":
        recharge(heroes, current_command)
    if current_command[0] == "Heal":
        heal(heroes, current_command)

    command = input()
for hero, value in heroes.items():
    print(hero)
    print(f'  HP: {value["HP"]}')
    print(f'  MP: {value["MP"]}')
