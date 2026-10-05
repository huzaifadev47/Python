items = []
prices = []

while True:
    item = input("Enter item to buy (q to quit): ")
    if item.lower() == 'q':
        break

    price = float(input("Enter price of the item: "))
    items.append(item)
    prices.append(price)

for item, price in zip(items, prices):
    print(item, "-", price)

print("Total:", sum(prices))