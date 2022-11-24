import re
pattern = r"[@][#]+[A-Z][A-Za-z0-9]{4}([A-Za-z0-9]+)?[A-Z][@][#]+"
pattern_1 = r"(?<=[@#A-Za-z])\d+(?=[@#A-Za-z])"

n = int(input())
for index in range(n):
    barcode = input()
    valid_barcode = re.match(pattern, barcode)
    if not valid_barcode:
        print("Invalid barcode")
        continue
    else:
        valid_barcode = valid_barcode.group()
        number_of_group = re.findall(pattern_1, valid_barcode)
        if len(number_of_group) > 0:
            print(f"Product group: {''.join(number_of_group)}")
        else:
            print(f'Product group: 00')

