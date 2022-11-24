def add_stop(planned_stops, index, string):
    if index in range(len(planned_stops)):
        planned_stops = planned_stops[0:index] + string + planned_stops[index:]
    print(planned_stops)
    return planned_stops


def remove(planned_stops, start_index, end_index):
    if start_index in range(len(planned_stops)) and end_index in range(len(planned_stops)):
        planned_stops = planned_stops[0:start_index] + planned_stops[end_index+1:]
    print(planned_stops)
    return planned_stops

def switch(planned_stops, old_string, new_string):
    if old_string in planned_stops:
        planned_stops = planned_stops.replace(old_string, new_string)
    print(planned_stops)
    return planned_stops


planned_stops = input()
command = input()
while command != "Travel":
    current_command = command.split(":")
    if current_command[0] == "Add Stop":
        index = int(current_command[1])
        string = current_command[2]
        planned_stops = add_stop(planned_stops, index, string)
    if current_command[0] == "Remove Stop":
        start_index = int(current_command[1])
        end_index = int(current_command[2])
        planned_stops = remove(planned_stops, start_index, end_index)
    if current_command[0] == "Switch":
        old_string = current_command[1]
        new_string = current_command[2]
        planned_stops = switch(planned_stops, old_string, new_string)
    command = input()
print(f'Ready for world tour! Planned stops: {planned_stops}')
