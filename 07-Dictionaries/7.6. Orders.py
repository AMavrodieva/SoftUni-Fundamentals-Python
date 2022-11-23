command = input()
products = {}

while command != "buy":
    product_name, price, quantity = command.split()
    price = float(price)
    quantity = int(quantity)
    if product_name not in products:
        products[product_name] = {'product_price': price, 'product_quantity': quantity}
    else:
        products[product_name]['product_quantity'] += quantity
        products[product_name]['product_price'] = price
    command = input()

for product_name, value in products.items():
    total_price = value['product_price'] * value['product_quantity']
    print(f'{product_name} -> {total_price:.2f}')