number = float(input())
if number == 0:
    print("zero")
elif number < 0:
    if 0 > number > -1:
        print("small negative")
    elif number > - 1000000:
        print("negative")
    else:
        print("large negative")
elif number > 0:
    if 0 < number < 1:
        print("small positive")
    elif number < 1000000:
        print("positive")
    else:
        print("large positive")
