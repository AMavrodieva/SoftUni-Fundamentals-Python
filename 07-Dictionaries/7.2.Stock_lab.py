date = input().split()
products = {}
searched_item = input().split()

for i in range(0, len(date), 2):
    product = date[i]
    quantity = int(date[i+1])
    products[product] = quantity
for s_p in searched_item:
    if s_p in products:
        print(f"We have {products[s_p]} of {s_p} left")
    else:
        print(f"Sorry, we don't have {s_p}")
