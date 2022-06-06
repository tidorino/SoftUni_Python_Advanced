def get_children(matrix, row, column):
    possible_children_cords = [
        [row - 1, column - 1],
        [row - 1, column],
        [row - 1, column + 1],
        [row, column - 1],
        [row, column + 1],
        [row + 1, column - 1],
        [row + 1, column],
        [row + 1, column + 1],
    ]
    result = []
    for child_row, child_col in possible_children_cords:
        if 0 <= child_row < len(matrix) and 0 <= child_col < len(matrix) and matrix[child_row][child_col] > 0:
            result.append([child_row, child_col])

    return result


n = int(input())
matrix = [[int(x) for x in input().split(' ')] for _ in range(n)]
coordinates = input().split(' ')
for idx in coordinates:
    row, column = map(int, idx.split(','))
    power = matrix[row][column]
    if power <= 0:
        continue

    matrix[row][column] = 0

    children = get_children(matrix, row, column)
    for child_row, child_col in children:
        matrix[child_row][child_col] -= power

alive_cells_count = 0
alive_cells_sum = 0

for row in matrix:
    for el in row:
        if el > 0:
            alive_cells_count += 1
            alive_cells_sum += el

print(f'Alive cells: {alive_cells_count}')
print(f'Sum: {alive_cells_sum}')
for row in matrix:
    print(*row, sep=' ')


