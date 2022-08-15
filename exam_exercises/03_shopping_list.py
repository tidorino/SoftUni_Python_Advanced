def shopping_list(number, **kwargs):
    budget = number

    if budget < 100:
        return 'You do not have enough budget.'

    basket = set()
    products = []
    for product, product_data in kwargs.items():
        if len(basket) == 5:
            break
        price_product = product_data[0] * product_data[1]
        if budget >= price_product:

            basket.add(product)
            products.append(f"You bought {product} for {price_product:.2f} leva.")
            budget -= price_product
    return '\n'.join(products)



# print(shopping_list(100,
#                     microwave=(70, 2),
#                     skirts=(15, 4),
#                     coffee=(1.50, 10),
#                     ))
print(shopping_list(20,
                    jeans=(19.99, 1),
                    ))
print(shopping_list(104,
                    cola=(1.20, 2),
                    candies=(0.25, 15),
                    bread=(1.80, 1),
                    pie=(10.50, 5),
                    tomatoes=(4.20, 1),
                    milk=(2.50, 2),
                    juice=(2, 3),
                    eggs=(3, 1),
                    ))


