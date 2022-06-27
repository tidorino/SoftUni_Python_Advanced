def inside(w_row, w_col, b_row, b_col, n):
    return 0 <= w_row < n and 0 <= w_col < n and 0 <= b_row < n and 0 <= b_col < n


def diagonal_move_right(row, col, matrix):
    if matrix[row - 1][col + 1] == 'b':
        return row - 1, col + 1
    if matrix[row - 1][col - 1] == 'b':
        return row - 1, col - 1
    if matrix[row + 1][col - 1] == 'w':
        return row + 1, col - 1
    if matrix[row + 1][col + 1] == 'w':
        return row + 1, col + 1


n = 8
chessboard = [[x for x in input().split(' ')] for _ in range(n)]
white_pawn_row = 0
white_pawn_col = 0
black_pawn_row = 0
black_pawn_col = 0

position_row = {
    0: "8",
    1: "7",
    2: "6",
    3: "5",
    4: "4",
    5: "3",
    6: "2",
    7: "1",
}
positions_col = {
    0: "a",
    1: "b",
    2: "c",
    3: "d",
    4: "e",
    5: "f",
    6: "g",
    7: "h",
}

for row in range(n):
    for col in range(n):
        if chessboard[row][col] == 'w':
            white_pawn_row, white_pawn_col = row, col
        if chessboard[row][col] == 'b':
            black_pawn_row, black_pawn_col = row, col


while True:
    if not inside(white_pawn_row, white_pawn_col, black_pawn_row, black_pawn_col, n):
        break
    white_p_next_move = white_pawn_row - 1, white_pawn_col
    black_p_next_move = black_pawn_row + 1, black_pawn_col
    if white_p_next_move == 'b':
        diagonal_white_move = diagonal_move_right(white_pawn_row, white_pawn_col, chessboard)
        white_pawn_row, white_pawn_col = diagonal_white_move
        print(f"Game over! White win, capture on {''}.")
        break
    if black_p_next_move == 'w':
        diagonal_white_move = diagonal_move_right(black_pawn_row, black_pawn_col, chessboard)
        black_pawn_row, black_pawn_col = black_p_next_move
        print(f"Game over! Black win, capture on {''}.")
        break
    white_pawn_row, white_pawn_col = white_p_next_move
    black_pawn_row, black_pawn_col = black_p_next_move

if chessboard[white_pawn_row][white_pawn_col] is not inside(white_pawn_row, white_pawn_col, black_pawn_row, black_pawn_col, n):
    position = positions_col[white_pawn_col] + position_row[white_pawn_row + 1]
    print(f"Game over! White pawn is promoted to a queen at {position}.")
else:
    position = positions_col[black_pawn_col] + position_row[black_pawn_row + 1]
    print(f"Game over! Black pawn is promoted to a queen at {position}.")
