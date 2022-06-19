def get_next_pos(row, col, direction, step):
    if direction == 'up':
        return row - step, col
    if direction == 'down':
        return row + step, col
    if direction == 'right':
        return row, col + step
    if direction == 'left':
        return row, col - step


def is_inside(row, col, size):
    return 0 <= row < size and 0 <= col < size


n = 5

matrix = [[x for x in input().split(' ')] for _ in range(n)]
shooter_row = 0
shooter_col = 0
target = 0

for row in range(n):
    for column in range(n):
        if matrix[row][column] == 'A':
            shooter_row = row
            shooter_col = column
        if matrix[row][column] == 'x':
            target += 1

matrix[shooter_row][shooter_col] = '.'
numb_of_commands = int(input())
hit_target = []

for _ in range(numb_of_commands):
    commands = input().split(' ')
    command = commands[0]
    direction = commands[1]

    if command == 'move':
        steps = int(commands[2])
        next_row, next_col = get_next_pos(shooter_row, shooter_col, direction, steps)
        if is_inside(next_row, next_col, n) and matrix[next_row][next_col] == '.':
            shooter_row, shooter_col = next_row, next_col
    else:
        bullet_row, bullet_col = get_next_pos(shooter_row, shooter_col, direction, 1)
        while is_inside(bullet_row, bullet_col, n):
            if matrix[bullet_row][bullet_col] == 'x':
                target -= 1
                matrix[bullet_row][bullet_col] = '.'
                hit_target.append([bullet_row, bullet_col])
                break
            bullet_row, bullet_col = get_next_pos(bullet_row, bullet_col, direction, 1)

        if target == 0:
            break

if target == 0:
    print(f'Training completed! All {len(hit_target)} targets hit.')
else:
    print(f'Training not completed! {target} targets left.')

print(*hit_target, sep="\n")
