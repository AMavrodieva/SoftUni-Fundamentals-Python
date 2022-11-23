number_of_electrons = int(input())
electron = []
shell_number = 1
while number_of_electrons > 0:
    max_electron_in_current_shell = 2 * shell_number ** 2
    if max_electron_in_current_shell > number_of_electrons:
        electron.append(number_of_electrons)
        number_of_electrons -= max_electron_in_current_shell
    else:
        electron.append(max_electron_in_current_shell)
        number_of_electrons -= max_electron_in_current_shell
    shell_number += 1
print(electron)

