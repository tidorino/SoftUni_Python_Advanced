def get_next_position(row, col, position):
    if position == 'up':
        return row - 1, col
    if position == 'down':
        return row + 1, col
    if position == 'right':
        return row, col + 1
    if position == 'left':
        return row, col - 1


n = int(input())
commands = input().split(' ')

matrix = [[x for x in input().split(' ')] for _ in range(n)]
shooter_row = 0
shooter_col = 0
coal_collector = 0
game_over = False

for row in range(n):
    for col in range(n):
        if matrix[row][col] == 's':
            shooter_row,shooter_col = row,col
        elif matrix[row][col] == 'c':
            coal_collector += 1

for command in commands:
    next_row, next_col = get_next_position(shooter_row, shooter_col, command)

    if next_row < 0 or next_col < 0 or next_row >= n or next_col >= n:
        continue

    shooter_row, shooter_col = next_row, next_col
    if matrix[shooter_row][shooter_col] == 'c':
        matrix[shooter_row][shooter_col] = '*'
        coal_collector -= 1
        if coal_collector == 0:
            break

    elif matrix[shooter_row][shooter_col] == 'e':
        game_over = True
        break

if coal_collector == 0:
    print(f'You collected all coal! ({shooter_row}, {shooter_col})')
elif game_over:
    print(f'Game over! ({shooter_row}, {shooter_col})')
else:
    print(f'{coal_collector} pieces of coal left. ({shooter_row}, {shooter_col})')






