def is_not_inside(row, col, size):
    return row < 0 or col < 0 or row >= size or col >= size


def get_next_position(row, col, position, size):
    if position == 'up':
        row -= 1
        if is_not_inside(row, col, size):
            return n - 1, col

        else:
            return row, col
    if position == 'down':
        row += 1
        if is_not_inside(row, col, size):
            return 0, col
        else:
            return row, col
    if position == 'right':
        col += 1
        if is_not_inside(row, col, size):
            return row, 0
        else:
            return row, col
    if position == 'left':
        col -= 1
        if is_not_inside(row, col, size):
            return row, n - 1
        else:
            return row, col


n = 6
matrix = [[x for x in input().split(' ')] for _ in range(n)]
rover_row = 0
rover_col = 0

for row in range(n):
    for column in range(n):
        if matrix[row][column] == 'E':
            rover_row = row
            rover_col = column

commands = input().split(', ')


water_deposit = False
metal_deposit = False
concrete_deposit = False

for command in commands:
    next_row, next_col = get_next_position(rover_row, rover_col, command, n)

    rover_row, rover_col = next_row, next_col

    if matrix[rover_row][rover_col] == 'W':
        water_deposit = True
        print(f'Water deposit found at {rover_row, rover_col}')
    elif matrix[rover_row][rover_col] == 'M':
        metal_deposit = True
        print(f'Metal deposit found at {rover_row, rover_col}')
    elif matrix[rover_row][rover_col] == 'C':
        concrete_deposit = True
        print(f'Concrete deposit found at {rover_row, rover_col}')
    elif matrix[rover_row][rover_col] == 'R':
        print(f'Rover got broken at {rover_row, rover_col}')
        break

if water_deposit and metal_deposit and concrete_deposit:
    print('Area suitable to start the colony.')
else:
    print('Area not suitable to start the colony.')


