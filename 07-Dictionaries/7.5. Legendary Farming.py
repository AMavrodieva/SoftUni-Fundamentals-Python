data = input()
key_materials = ["shards", "fragments", "motes"]
dict_of_key_materials = {}
dict_of_other_materials = {}
found = False
while not found:
    data = [i.lower() for i in data.split()]
    for index in range(0, len(data), 2):
        quantity = int(data[index])
        material = data[index + 1]
        if material in key_materials and quantity < 250:
            if material not in dict_of_key_materials:
                dict_of_key_materials[material] = 0
            dict_of_key_materials[material] += quantity
            if dict_of_key_materials[material] >= 250:
                found = True
                break
        elif material in key_materials and quantity >= 250:
            if material not in dict_of_key_materials:
                dict_of_key_materials[material] = 0
            dict_of_key_materials[material] += quantity
            found = True
            break
        else:
            if material not in dict_of_other_materials:
                dict_of_other_materials[material] = 0
            dict_of_other_materials[material] += quantity
    if found == True:
        break
    data = input()
for key, value in dict_of_key_materials.items():
    if value >= 250 and key == "shards":
        print("Shadowmourne obtained!")
        dict_of_key_materials[material] -= 250
    elif value >= 250 and key == "fragments":
        print("Valanyr obtained!")
        dict_of_key_materials[material] -= 250
    elif value >=  250 and key == "motes":
        print("Dragonwrath obtained!")
        dict_of_key_materials[material] -= 250
if "shards" in dict_of_key_materials:
    print(f"shards: {dict_of_key_materials['shards']}")
else:
    print(f"shards: 0")
if "fragments" in dict_of_key_materials:
    print(f"fragments: {dict_of_key_materials['fragments']}")
else:
    print("fragments: 0")
if "motes" in dict_of_key_materials:
    print(f"motes: {dict_of_key_materials['motes']}")
else:
    print('motes: 0')
for key, value in dict_of_other_materials.items():
    print(f"{key}: {value}")

