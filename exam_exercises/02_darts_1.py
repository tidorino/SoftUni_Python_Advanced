def in_range(val, max_value):
    return 0 <= val < max_value


def get_value(matrix, row, col, n):
    if not in_range(row, n) or not in_range(col, n):
        return 0

    target = matrix[row][col]

    if target.isdigit():
        return int(target)

    value = int(matrix[row][0]) + int(matrix[row][-1]) + int(matrix[0][col]) + int(matrix[-1][col])

    if target == 'T':
        return value * 3

    elif target == 'D':
        return value * 2

    elif target == 'B':
        return 501


def solve(player_names, board, n):
    current_player = player_names[0], 501, 0
    other_player = player_names[1], 501, 0

    while True:
        name, total_points, turns = current_player
        position = input().strip('()').split(', ')
        next_row, next_col = int(position[0]), int(position[1])

        total_points -= get_value(board, next_row, next_col, n)
        turns += 1
        current_player = name, total_points, turns

        if total_points <= 0:
            break

        current_player, other_player = other_player, current_player

    (name, _, turns) = current_player
    print(f'{name} won the game with {turns} throws!')


player_names = input().split(', ')
n = 7
board = [[x for x in input().split(' ')] for _ in range(n)]
solve(player_names, board, n)



