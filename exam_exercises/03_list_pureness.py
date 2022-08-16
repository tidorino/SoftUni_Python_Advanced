from collections import deque


def best_list_pureness(*args):

    numbers = args[0]
    numbers = deque(numbers)
    n = args[1]
    pureness_value = 0
    pureness_value_dic = {}
    rotation = 0
    for i in range(0, n + 1):
        pureness_value = 0
        rotation = int(i)

        for idx, numb in enumerate(numbers):
            pureness_value += idx * numb

        pureness_value_dic[rotation] = pureness_value
        last_el_of_numbers = numbers.pop()
        numbers.appendleft(last_el_of_numbers)

    sorted_pureness = sorted(pureness_value_dic.items(), key=lambda x: -x[1])
    return f"Best pureness {sorted_pureness[0][1]} after {sorted_pureness[0][0]} rotations"

test = ([4, 3, 2, 6], 4)
result = best_list_pureness(*test)
print(result)

test = ([7, 9, 2, 5, 3, 4], 3)
result = best_list_pureness(*test)
print(result)

test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)
