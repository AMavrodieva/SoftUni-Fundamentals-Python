command = input()
products = {}
while command != "statistics":
    product, quantity = command.split(": ")
    quantity = int(quantity)
    if product not in products:
        products[product] = 0
    products[product] += quantity
    command = input()
print(f"Products in stock:")
for product, quantity in products.items():
    print(f"- {product}: {quantity}")
print(f"Total Products: {len(products.keys())}")
print(f"Total Quantity: {sum(products.values())}")

#[print(f"-{key}:{value}") for key, value in product]

# втори вариант
command = input()
products = {}
while command != "statistics":
    product, quantity = command.split(": ")
    quantity = int(quantity)
    if product not in products:
        products[product] = quantity
    else:
        products[product] += quantity
    command = input()
print(f"Products in stock:")
for product, quantity in products.items():
    print(f"- {product}: {quantity}")
print(f"Total Products: {len(products.keys())}")
print(f"Total Quantity: {sum(products.values())}")