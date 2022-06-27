def shopping_cart(*args):
    shopping_products = {
        'Pizza': [],
        'Soup': [],
        'Dessert': [],
        }
    shopping_card = 0
    for parts in args:
        if parts == 'Stop':
            break

        key = parts[0]
        value = parts[1]
        shopping_card += 1
        # if key not in shopping_products:
        #     shopping_products[key] = []
        if key == 'Pizza':
            if value not in shopping_products[key] and len(shopping_products[key]) < 4:
                shopping_products[key].append(value)

        elif key == 'Soup':
            if value not in shopping_products[key] and len(shopping_products[key]) < 3:
                shopping_products[key].append(value)

        elif key == 'Dessert':
            if value not in shopping_products[key] and len(shopping_products[key]) < 2:
                shopping_products[key].append(value)

    sorted_cart = sorted(
        shopping_products.items(),
        key=lambda x: (- len(x[1]), x[0]),
        )
    result = ''
    if shopping_card == 0:
        print('No products in the cart!')
    else:
        for meal, product in sorted_cart:
            result += f"{meal}:\n"
            if product:
                for element in product:
                    result += f" - {element}\n"

    return result


print(shopping_cart(
    ('Pizza', 'ham'),    ('Soup', 'carrots'),
    ('Pizza', 'cheese'),
    ('Pizza', 'flour'),
    ('Dessert', 'milk'),
    ('Pizza', 'mushrooms'),
    ('Pizza', 'tomatoes'),
    'Stop',
))
print(shopping_cart(
    ('Pizza', 'ham'),
    ('Dessert', 'milk'),
    ('Pizza', 'ham'),
    'Stop',
))
print(shopping_cart(
    'Stop',
    ('Pizza', 'ham'),
    ('Pizza', 'mushrooms'),
))
