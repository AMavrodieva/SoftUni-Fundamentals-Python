def is_item_exist(shopping, item, item_list):
    if item in item_list:
        return True
    return False


def add(shopping, current_command):
    store = current_command[1]
    list_of_items = current_command[2].split(",")
    if store not in shopping:
        shopping[store] = []
    for el in list_of_items:
        if is_item_exist(shopping, el, item_list):
            continue
        else:
            shopping[store].append(el)
            item_list.append(el)
    return shopping


def important(shopping, current_command):
    store = current_command[1]
    item = current_command[2]
    if not is_item_exist(shopping, item, item_list):
        if store not in shopping:
            shopping[store] = []
        important_item.append(item)
        #shopping[store].pop(0)
        shopping[store].insert(0, item)
    return shopping


def remove(shopping, current_command):
    store = current_command[1]
    is_exist = False
    for el in important_item:
        if el in shopping[store]:
            is_exist = True
            break
    if not is_exist:
        if store in shopping:
            shopping = shopping.pop(store)
            for element in shopping[store]:
                item_list.remove(element)
    return shopping


command = input()
item_list = []
important_item = []
shopping = {}

while command != "Go Shopping":
    current_command = command.split("->")
    try:
        if current_command[0] == "Add":
            shopping = add(shopping, current_command)
        if current_command[0] == "Important":
            shopping = important(shopping, current_command)
        if current_command[0] == "Remove":
            shopping = remove(shopping, current_command)
    except KeyError:
        command = input()
        continue
    command = input()

for store, item_list in shopping.items():
    print(f'{store}:')
    for el in item_list:
        print(f'- {el}')


