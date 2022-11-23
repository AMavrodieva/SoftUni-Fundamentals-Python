wagon = int(input())
train = [0] * wagon
command = input()

while command != "End":
    current_text = command.split(" ")
    current_command = current_text[0]
    if current_command == "add":
        train[-1] += int(current_text[1])
    elif current_command == "insert":
        index = int(current_text[1])
        train[index] += int(current_text[2])
    elif current_command == "leave":
        index = int(current_text[1])
        train[index] -= int(current_text[2])
    command = input()

print(train)
