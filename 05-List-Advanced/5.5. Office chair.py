number_of_room = int(input())
are_chairs_enough = True
total_free_chairs = 0
for room in range(1, number_of_room + 1):
    chairs, n_people = input().split()
    n_people = int(n_people)
    difference = abs(len(chairs) - n_people)
    if len(chairs) < n_people:
        print(f"{difference} more chairs needed in room {room}")
        are_chairs_enough = False
    else:
        total_free_chairs += difference
if are_chairs_enough:
    print(f"Game On, {total_free_chairs} free chairs left")
