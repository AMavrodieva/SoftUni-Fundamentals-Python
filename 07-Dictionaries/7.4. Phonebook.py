data = input()
phone_list = {}
while "-" in data:
    name, phone = data.split("-")
    if name not in phone_list:
        phone_list[name] = 0
    phone_list[name] = phone
    data = input()
for i in range(0, int(data)):
    searched_name = input()
    if searched_name in phone_list:
            print(f"{searched_name} -> {phone_list[searched_name]}")
    else:
        print(f"Contact {searched_name} does not exist.")


