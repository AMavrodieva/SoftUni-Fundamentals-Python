def orders(products, counts):
    if products == "coffee":
        return counts * 1.50
    elif products == "water":
        return counts * 1.00
    elif products == "coke":
        return counts * 1.40
    elif products == "snacks":
        return  counts * 2.00


product = input()
number = int(input())
result = orders(product, number)
print(f"{result:.2f}")
