collection_of_items = input().split("|")
budget = float(input())
list_of_new_price = []
new_price = 0
profit = 0
new_budget = 0
for item in collection_of_items:
    current_item = item.split("->")
    type_of_item = current_item[0]
    price_of_item = float(current_item[-1])
    if type_of_item == "Clothes":
        if price_of_item > 50.00:
            continue
    elif type_of_item == "Shoes":
        if price_of_item > 35.00:
            continue
    elif type_of_item == "Accessories":
        if price_of_item > 20.50:
            continue
    else:
        continue
    if budget < price_of_item or budget <= 0:
        continue
    budget -= price_of_item
    new_price = price_of_item * 0.40 + price_of_item
    profit += price_of_item * 0.40
    new_price = f"{new_price:.2f}"
    list_of_new_price.append(new_price)
    new_budget += float(new_price)
print(" ".join(list_of_new_price))
print(f"Profit: {profit:.2f}")
new_budget = new_budget + profit
if new_budget >= 150.00:
    print("Hello, France!")
else:
    print("Not enough money.")
