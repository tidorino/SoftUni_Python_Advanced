"""

5
4
- X V -
- S - V
- - - -
X - - -
up
right
down
right
Christmas morning

"""


def get_next_pos(row, col, position):
    if position == 'up':
        return row - 1, col
    if position == 'down':
        return row + 1, col
    if position == 'right':
        return row, col + 1
    if position == 'left':
        return row, col - 1


def is_inside(row, col, n):
    return 0 <= row < n and 0 <= col < n


def get_cookie(row, col, matrix):
    cookie_direction = [
        [row - 1, col],
        [row + 1, col],
        [row, col - 1],
        [row, col + 1]
    ]
    presents = 0
    count_v = 0
    for r, c in cookie_direction:
        if is_inside(r, c, size) and matrix[r][c] != '-':
            if matrix[r][c] == 'V':
                count_v += 1

            matrix[r][c] = '-'
            presents += 1
    return presents, matrix, count_v


numb_presents = int(input())
size = int(input())

neighborhood = [[x for x in input().split()] for _ in range(size)]
santa_row = 0
santa_col = 0
nice_kids = 0
total_nice_kids = 0
for row in range(size):
    for col in range(size):
        if neighborhood[row][col] == 'S':
            santa_row, santa_col = row, col
        if neighborhood[row][col] == 'V':
            nice_kids += 1
            total_nice_kids += 1
neighborhood[santa_row][santa_col] = '-'

while True:
    command = input()
    if command == 'Christmas morning':
        break
    elif command == 'up' or command == 'down' or command == 'left' or command == 'right':
        next_row, next_col = get_next_pos(santa_row, santa_col, command)
        if is_inside(next_row, next_col, size):
            if neighborhood[next_row][next_col] == '-':
                santa_row, santa_col = next_row, next_col

            elif neighborhood[next_row][next_col] == 'V':
                neighborhood[next_row][next_col] = '-'
                numb_presents -= 1
                nice_kids -= 1
                santa_row, santa_col = next_row, next_col
            elif neighborhood[next_row][next_col] == 'X':
                neighborhood[next_row][next_col] = '-'
                santa_row, santa_col = next_row, next_col
            elif neighborhood[next_row][next_col] == 'C':
                present, neighborhood, count_v = get_cookie(next_row, next_col, neighborhood)
                numb_presents -= present
                nice_kids -= count_v
                santa_row, santa_col = next_row, next_col

        if numb_presents == 0:
            break
neighborhood[santa_row][santa_col] = 'S'
if numb_presents == 0 and nice_kids > 0:
    print('Santa ran out of presents!')
for row in neighborhood:
    print(' '.join(row))
if nice_kids == 0:
    print(f'Good job, Santa! {total_nice_kids} happy nice kid/s.')
else:
    print(f'No presents for {nice_kids} nice kid/s.')









