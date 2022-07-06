def stock_availability(inventory_list, command, *args):

    if command == 'delivery':
        return inventory_list + list(args)

    if not args:
        return inventory_list[1:]

    if isinstance(args[0], int):
        count = int(args[0])
        return inventory_list[count:]

    sold_items = set(args)
    # other solution:
    # result = []
    # for item in inventory_list:
    #     if item not in sold_items:
    #         result.append(item)
    # return result

    return [item for item in inventory_list if item not in sold_items]


print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie","banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
