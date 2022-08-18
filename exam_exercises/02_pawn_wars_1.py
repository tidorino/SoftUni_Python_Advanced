def is_not_inside(row, col, size):
    if row < 0 or col < 0 or row >= size or col >= size:
        return True
    return False


def check_diagonals(row, col, board, n, is_capture, move_when_captured):
    if board[row][col] == 'w':
        positions = {
            'up_left': (-1, -1),
            'up_right': (- 1, 1)
        }

        for position in positions:
            next_row = row + positions[position][0]
            next_col = col + positions[position][1]
            if is_not_inside(next_row, next_col, n):
                break
            if board[next_row][next_col] == 'b':
                is_capture = True
                move_when_captured.append([next_row, next_col])
                board[next_row][next_col] = 'w'
                break
            else:
                is_capture = False

        if is_capture:
            for item in move_when_captured:
                row = item[0]
                col = item[1]
            board[row][col] = 'w'
            return row, col, is_capture, move_when_captured

        board[row - 1][col] = 'w'
        return row - 1, col, is_capture, move_when_captured

    if board[row][col] == 'b':
        positions = {
            'up_left': (1, -1),
            'up_right': (1, 1)
        }
        for position in positions:
            next_row = row + positions[position][0]
            next_col = col + positions[position][1]
            if is_not_inside(next_row, next_col, n):
                break
            if board[next_row][next_col] == 'w':
                is_capture = True
                move_when_captured.append(next_row, next_col)
                board[next_row][next_col] = 'b'
            else:
                is_capture = False

        board[row + 1][col] = 'b'
        return row + 1, col, is_capture, move_when_captured


def find_square(row, col):
    row_position = {
        '8': 0,
        '7': 1,
        '6': 2,
        '5': 3,
        '4': 4,
        '3': 5,
        '2': 6,
        '1': 7,
    }
    col_position = {
        'a': 0,
        'b': 1,
        'c': 2,
        'd': 3,
        'e': 4,
        'f': 5,
        'g': 6,
        'h': 7,
    }
    result = ''
    for el, c_num in col_position.items():
        if col == c_num:
            result += el

    for el, r_num in row_position.items():
        if row == r_num:
            result += el

    return result


n = 8
board = [[el for el in input().split(' ')] for _ in range(n)]

white_pawn_row = 0
white_pawn_col = 0
black_pawn_row = 0
black_pawn_col = 0
for r in range(n):
    for c in range(n):
        if board[r][c] == 'w':
            white_pawn_row = r
            white_pawn_col = c
        if board[r][c] == 'b':
            black_pawn_row = r
            black_pawn_col = c
player1 = white_pawn_row, white_pawn_col
player2 = black_pawn_row, black_pawn_col


is_capture = False
move_when_captured = []


while True:
    white_pawn = player1
    black_pawn = player2

    player1 = white_pawn
    player2 = black_pawn

    next_row, next_col, is_capture, move_when_captured = \
        check_diagonals(white_pawn[0], white_pawn[1], board, n, is_capture, move_when_captured)
    if is_capture:
        square = find_square(next_row, next_col)
        if board[next_row][next_col] == 'w':
            print(f'Game over! White win, capture on {square}.')
            break
        else:
            print(f'Game over! Black win, capture on {square}.')
            break

    if is_not_inside(next_row, next_col, n):
        square = find_square(white_pawn[0], white_pawn[1])
        if board[next_row][next_col] == 'w':
            print(f'Game over! White pawn is promoted to a queen at {square}.')
            break
        else:
            print(f'Game over! Black pawn is promoted to a queen at {square}.')
            break

    player1 = next_row, next_col
    player1, player2 = player2, player1

