def get_next_position(row, col, position):
    if position == 'up':
        return row - 1, col
    if position == 'down':
        return row + 1, col
    if position == 'right':
        return row, col + 1
    if position == 'left':
        return row, col - 1


n = 6
board = [[x for x in input().split(' ')] for _ in range(n)]
first_move = input().strip('()').split(', ')
first_row, first_col = int(first_move[0]),  int(first_move[1])

while True:
    command = input()
    if command == 'Stop':
        break

    new_command = command.split(', ')
    if new_command[0] == 'Create':
        direction = new_command[1]
        value = new_command[2]
        next_row, next_col = get_next_position(first_row, first_col, direction)
        if board[next_row][next_col] == '.':
            board[next_row][next_col] = value
        first_row, first_col = next_row, next_col
    elif new_command[0] == 'Update':
        direction = new_command[1]
        value = new_command[2]
        next_row, next_col = get_next_position(first_row, first_col, direction)
        if board[next_row][next_col].isdigit() or board[next_row][next_col].isalpha():
            board[next_row][next_col] = value
        first_row, first_col = next_row, next_col

    elif new_command[0] == 'Delete':
        direction = new_command[1]
        next_row, next_col = get_next_position(first_row, first_col, direction)
        if board[next_row][next_col].isdigit() or board[next_row][next_col].isalpha():
            board[next_row][next_col] = '.'
        first_row, first_col = next_row, next_col

    elif new_command[0] == 'Read':
        direction = new_command[1]
        next_row, next_col = get_next_position(first_row, first_col, direction)
        if board[next_row][next_col].isdigit() or board[next_row][next_col].isalpha():
            print(f'{board[next_row][next_col]}')
        first_row, first_col = next_row, next_col

for row in board:
    print(' '.join(row))
