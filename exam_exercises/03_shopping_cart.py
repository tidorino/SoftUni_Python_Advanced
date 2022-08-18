def check_if_is_valid_and_add(shopping_cart_dict, meal, product, product_len):

    if product not in shopping_cart_dict[meal] and len(shopping_cart_dict[meal]) < product_len:
        shopping_cart_dict[meal].append(product)

    return shopping_cart_dict


def shopping_cart(*args):
    shopping_cart_dict = {'Soup': [],
                          'Pizza': [],
                          'Dessert': []
                          }
    soup_len = 3
    pizza_len = 4
    dessert_len = 2

    for items in args:
        type_of_meal = items[0]
        product = items[1]
        if items == 'Stop':
            break

        elif type_of_meal == 'Soup':
            result = check_if_is_valid_and_add(shopping_cart_dict, type_of_meal, product, soup_len)
        elif type_of_meal == 'Pizza':
            result = check_if_is_valid_and_add(shopping_cart_dict, type_of_meal, product, pizza_len)
        elif type_of_meal == 'Dessert':
            result = check_if_is_valid_and_add(shopping_cart_dict, type_of_meal, product, dessert_len)

    for value in shopping_cart_dict.values():
        if len(value) > 0:
            break
    else:
        return 'No products in the cart!'

    sorted_cart = sorted(shopping_cart_dict.items(), key=lambda x: (-len(x[1]), x[0]))
    result = ''
    for item in sorted_cart:
        result += f"{item[0]}:\n"
        sorted_product = sorted(item[1])
        for el in sorted_product:
            result += f" - {el}\n"
    return result.strip()

# print(shopping_cart(
#     ('Pizza', 'ham'),
#     ('Soup', 'carrots'),
#     ('Pizza', 'cheese'),
#     ('Pizza', 'flour'),
#     ('Dessert', 'milk'),
#     ('Pizza', 'mushrooms'),
#     ('Pizza', 'tomatoes'),
#     'Stop',
# ))
print(shopping_cart(
    'Stop',
    ('Pizza', 'ham'),
   ('Pizza', 'mushrooms'),
))
# print(shopping_cart(
#     ('Pizza', 'ham'),
#     ('Dessert', 'milk'),
#     ('Pizza', 'ham'),
#     'Stop',
# ))
