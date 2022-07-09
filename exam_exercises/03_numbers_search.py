import collections


def numbers_searching(*args):
    sort_numb = sorted(args)
    list_numb = []
    for n in range(sort_numb[0], sort_numb[-1] + 1):
        if n not in sort_numb:
            list_numb.append(n)

    list_numb.append([item for item, count in collections.Counter(sort_numb).items() if count > 1])
    return list_numb


# print(numbers_searching(1, 2, 4, 2, 5, 4))
# print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))
