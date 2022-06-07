"""
The knight game is played on a board with dimensions N x N.
You will receive a board with "K" for knights and "0" for empty cells.
Your task is to remove knights until no knights that can attack one another with one move are left.
Input
•	On the first line, you will receive integer N - the size of the board
•	On the following N lines, you will receive strings with "K" and "0"
Output
•	Print a single integer with the minimum number of knights that need to be removed
************
5
0K0K0
K000K
00K00
K000K
0K0K0

"""

def find_count(board, row, column):
    moves = [
        [row - 2, column - 1],
        [row - 2, column + 1],
        [row - 1, column - 2],
        [row - 1, column + 2],
        [row + 1, column - 2],
        [row + 1, column + 2],
        [row + 2, column - 1],
        [row + 2, column + 1]
    ]

    result = 0

    for (r, c) in moves:
        if 0 <= r < len(board) and 0 <= c < len(board) and board[r][c] == 'K':
            result += 1

    return result


n = int(input())

board = []
for _ in range(n):
    board.append(list(input()))
remove_knights_counter = 0

while True:
    knight_row = 0
    knight_col = 0
    best_count = 0

    for row in range(n):
        for column in range(n):
            if board[row][column] == '0':
                continue

            count = find_count(board, row, column)
            if count > best_count:
                best_count = count
                knight_row = row
                knight_col = column

    if best_count == 0:
        break

    board[knight_row][knight_col] = '0'
    remove_knights_counter += 1

print(remove_knights_counter)
