def is_not_inside(row, col, size):
    return row < 0 or col < 0 or row >= size or col >= size


def check_position(row, col, n, field):
    position = [
        (row, col - 1),
        (row, col + 1),
        (row - 1, col - 1),
        (row - 1, col),
        (row - 1, col + 1),
        (row + 1, col - 1),
        (row + 1, col),
        (row + 1, col + 1)
    ]
    for r, c in position:
        if is_not_inside(r, c, n):
            continue
        if field[r][c] == '*':
            continue
        field[r][c] += 1
    return field


n = int(input())
bombs = int(input())
field = []
for r in range(n):
    elements = [0] * n
    field.append(elements)

for bomb in range(bombs):
    position = input().strip('()').split(', ')
    row, col = int(position[0]), int(position[1])
    field[row][col] = '*'
    field = check_position(row, col, n, field)

for item in field:
    print(*item)

# print(' '.join([str(x) for x in field]), sep="\n")
