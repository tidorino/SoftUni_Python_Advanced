def even_odd(*args):
    command = args[-1]
    result = []
    for idx in range(len(args) - 1):
        numb = args[idx]

        if command == 'even' and numb % 2 == 0:   # could be made with : parity = 0 if command == 'even' else 1
            result.append(numb)                   # if numb % 2 = parity

        elif command == 'odd' and numb % 2 != 0:   # could be made with : parity = 0 if command == 'even' else 1
            result.append(numb)                    # if numb % 2 = parity

    return result


# print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
