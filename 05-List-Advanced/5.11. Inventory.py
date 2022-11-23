def is_items_exist(item_list, item):
    if item in item_list:
        return True
    return False


def add(item_list, item):
    if not is_items_exist(item_list, item):
        item_list.append(item)
    return item_list


def remove(item_list, item):
    if is_items_exist(item_list, item):
        item_list.remove(item)
    return item_list


def renew(item_list, item):
    if is_items_exist(item_list, item):
        item_list.remove(item)
        item_list.append(item)
    return item_list


item_list = input().split(", ")
command = input()

while command != "Craft!":
    current_command, item = command.split(" - ")
    if current_command == "Collect":
        add(item_list, item)
    elif current_command == "Drop":
        remove(item_list, item)
    elif current_command == "Renew":
        renew(item_list, item)
    elif current_command == "Combine Items":
        old_item, new_item = item.split(":")
        if is_items_exist(item_list, old_item):
            current_position = int(item_list.index(old_item))
            item_list.insert(current_position+1, new_item)
    command = input()
print(f"{', '.join(item_list)}")
