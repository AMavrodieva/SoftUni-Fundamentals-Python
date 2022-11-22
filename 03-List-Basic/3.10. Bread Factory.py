initial_energy = 100
initial_coins = 100
events = input().split("|")
gained_energy = 0
current_energy = 0
gained_coins = 0
total_coins = 100
for text in events:
    current_text = text.split("-")
    event = current_text[0]
    number = current_text[1]
    if event == "rest":
        gained_energy = int(number)
        current_energy = initial_energy + gained_energy
        if current_energy > 100:
            current_energy = 100
            gained_energy = current_energy - 100
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {current_energy}.")
    elif event == "order":
        if current_energy >= 30:
            gained_coins = int(number)
            total_coins += gained_coins
            current_energy -= 30
            print(f"You earned {gained_coins} coins.")
        else:
            current_energy += 50
            print("You had to rest!")
    else:
        if total_coins >= int(number):
            initial_energy = current_energy
            total_coins -= int(number)
            print(f"You bought {event}.")
        else:
            print(f"Closed! Cannot afford {event}.")
            break
print("Day completed!")
print(f"Coins: {total_coins}")
print(f"Energy: {current_energy}")


