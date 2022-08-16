def is_not_inside(row, col, size):
    return row < 0 or col < 0 or row >= size or col >= size


def get_next_position(row, col, board, n, winner):

    positions = {
        'left_row': (0, - 1),
        'right_row': (0, 1),
        'up_row': (- 1, 0),
        'down_row': (1, 0),
        'up_right_row': (- 1, 1),
        'up_left_row': (- 1, - 1),
        'down_left_row': (1, -1),
        'down_right_row': (1, 1)
    }

    for position in positions:

        nex_row = row + positions[position][0]
        nex_col = col + positions[position][1]
        while not is_not_inside(nex_row, nex_col, n):
            if board[nex_row][nex_col] == 'Q':
                break
            if board[nex_row][nex_col] == 'K':
                winner.append([row, col])
                break
            nex_row += positions[position][0]
            nex_col += positions[position][1]

    return winner


n = 8
board = [[x for x in input().split(' ')] for _ in range(n)]

queens_position = []

for row in range(n):
    for col in range(n):
        if board[row][col] == 'Q':
            queens_position.append([row, col])
queen_winner = []

while True:
    if not queens_position:
        break
    queen_row, queen_col = queens_position.pop()

    queen_info = get_next_position(queen_row, queen_col, board, n, queen_winner)
    if not queen_info:
        continue

if not queen_winner:
    print('The king is safe!')

for item in queen_winner:
    print(item)
