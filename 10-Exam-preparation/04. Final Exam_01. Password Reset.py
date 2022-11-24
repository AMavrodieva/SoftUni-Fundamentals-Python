password = input()
command = input()
while command != "Done":
    if command == "TakeOdd":
        new_str = ""
        for i in range(0, len(password)):
            if i % 2 == 1:
                new_str += password[i]
        password = new_str
        print(password)
    if command != "TakeOdd":
        command = command.split()
        if command[0] == "Cut":
            current_index = int(command[1])
            length = int(command[2])
            password = password[0:current_index] + password[current_index + length:]
            print(password)
        if command[0] == "Substitute":
            substring = command[1]
            susbstitute = command[2]
            if substring in password:
               password = password.replace(substring, susbstitute)
               print(password)
            else:
                print(f'Nothing to replace!')
    command = input()
print(f'Your password is: {password}')

