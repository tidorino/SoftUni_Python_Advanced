def get_next_position_white(current_row, current_col, board):
    if current_col - 1 >= 0:
        if board[current_row - 1][current_col - 1] == 'b':
            return current_row - 1, current_col - 1, 'captured'
    if current_col + 1 < len(board):
        if board[current_row - 1][current_col + 1] == 'b':
            return current_row - 1, current_col + 1, 'captured'

    return current_row - 1, current_col, ''


def get_next_position_black(current_row, current_col, board):
    if current_col - 1 >= 0:
        if board[current_row + 1][current_col - 1] == 'w':
            return current_row + 1, current_col - 1, 'captured'
    if current_col + 1 < len(board):
        if board[current_row + 1][current_col + 1] == 'w':
            return current_row + 1, current_col + 1, 'captured'

    return current_row + 1, current_col, ''


chess_board_size = 8

chess_board = []

white_row, white_col = 0, 0
black_row, black_col = 0, 0

for i in range(chess_board_size):
    new_row = [x for x in input().split()]
    for j in range(len(new_row)):
        if new_row[j] == 'w':
            white_row, white_col = i, j
        if new_row[j] == 'b':
            black_row, black_col = i, j
    chess_board.append(new_row)

move_counter = 1
winner = ''
winner_row, winner_col = 0, 0
condition = ''
while True:
    next_row, next_col = 0, 0
    current_player = 'White' if move_counter % 2 != 0 else 'Black'

    if current_player == 'White':
        next_row, next_col, condition = get_next_position_white(white_row, white_col, chess_board)
        chess_board[white_row][white_col] = '-'
        chess_board[next_row][next_col] = 'w'
        white_row, white_col = next_row, next_col
        if white_row == 0:
            condition = 'promoted'

    if current_player == 'Black':
        next_row, next_col, condition = get_next_position_black(black_row, black_col, chess_board)
        chess_board[black_row][black_col] = '-'
        chess_board[next_row][next_col] = 'b'
        black_row, black_col = next_row, next_col
        if black_row == chess_board_size - 1:
            condition = 'promoted'

    if condition != '':
        winner_row, winner_col = next_row, next_col
        winner = current_player
        break
    move_counter += 1

winner_position = [[8, 7, 6, 5, 4, 3, 2, 1], ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']]

if condition == 'promoted':
    print(f"Game over! {winner} pawn is promoted to a queen at "
          f"{winner_position[1][winner_col]}{winner_position[0][winner_row]}.")
else:
    print(f"Game over! {winner} win, capture on "
          f"{winner_position[1][winner_col]}{winner_position[0][winner_row]}.")
