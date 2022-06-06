rows, columns = [int(x) for x in input().split()]

string = input()
indx = 0

for row in range(rows):
    elements = [None] * columns
# Other solution #
#     if row % 2 == 0:
#         for column in range(columns):
#             elements[column] = string[indx % len(string)]
#             indx += 1
#
#     else:
#         for column in range(columns - 1, - 1, -1):
#             elements[column] = string[indx % len(string)]
#             indx += 1
    start, end, step = (0, columns, 1) if row % 2 == 0 else (columns - 1, -1, -1)
    for column in range(start, end, step):
        elements[column] = string[indx % len(string)]
        indx += 1

    print(''.join(elements))



