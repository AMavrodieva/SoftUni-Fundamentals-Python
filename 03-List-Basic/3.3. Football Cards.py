card_input = input().split()
teamA = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
teamB = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
count_A = 11
count_B = 11
is_remain_players = True
for players in card_input:
    card_info = players.split("-")
    team_name = card_info[0]
    player_number = int(card_info[1])
    if team_name == "A":
        if player_number in teamA:
            teamA.remove(player_number)
            count_A -= 1
        else:
            continue
    elif team_name == "B":
        if player_number in teamB:
            teamB.remove(player_number)
            count_B -= 1
        else:
            continue
    if count_A < 7 or count_B < 7:
        is_remain_players = False
        break
if not is_remain_players:
    print(f"Team A - {count_A}; Team B - {count_B}")
    print(f"Game was terminated")
else:
    print(f"Team A - {count_A}; Team B - {count_B}")

# вариант 2
team_A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
team_B = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
cards = input().split(" ")
team_a = 11
team_b = 11
is_remain_players = True
for players in cards:
    card_info = players.split("-")
    team_name = card_info[0]
    player_number = int(card_info[1])
    if team_name == "A":
        if player_number in team_A:
            team_A.remove(player_number)
            team_a -= 1
        else:
            continue
        if team_a < 7:
            is_remain_players = False
            break
    if team_name == "B":
        if player_number in team_B:
            team_B.remove(player_number)
            team_b -= 1
        else:
            continue
        if team_b < 7:
            is_remain_players = False
            break
print(f"Team A - {team_a}; Team B - {team_b}")
if not is_remain_players:
    print("Game was terminated")