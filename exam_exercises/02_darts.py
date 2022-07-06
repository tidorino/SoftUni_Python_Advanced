from collections import deque


def in_range(val, max_value):
    return 0 <= val < max_value


def throw(player, throw):
    result = throw + 1
    return result


def corresponding_numbers(row, col, matrix):
    value = int(matrix[row][0]) + int(matrix[row][-1]) + int(matrix[0][col]) + int(matrix[-1][col])
    return value

    # other solution :
    # result = []
    # for c in range(col, n):
    #     if matrix[row][c] != 'T' and matrix[row][c] != 'B' and matrix[row][c] != 'D':
    #         result.append(int(matrix[row][c]))
    # for c in range(col, - 1, - 1):
    #     if matrix[row][c] != 'T' and matrix[row][c] != 'B' and matrix[row][c] != 'D':
    #         result.append(int(matrix[row][c]))
    #
    # for r in range(row, n):
    #     if matrix[r][col] != 'T' and matrix[r][col] != 'B' and matrix[r][col] != 'D':
    #         result.append(int(matrix[r][col]))
    # for r in range(row, - 1, - 1):
    #     if matrix[r][col] != 'T' and matrix[r][col] != 'B' and matrix[r][col] != 'D':
    #         result.append(int(matrix[r][col]))
    #
    # return sum(result)


first_player, second_player = input().split(', ')

n = 7
dartboard = [[x for x in input().split(' ')] for _ in range(n)]
player_move = deque([first_player, second_player])
first_score = 501
second_score = 501
first_throw_counts = 0
second_throw_counts = 0


while True:
    position = input().strip('()').split(', ')
    next_row, next_col = int(position[0]), int(position[1])
    current_player = player_move.popleft()
    if not in_range(next_row, n) or not in_range(next_col, n):
        if first_player == current_player:
            first_throw_counts = throw(current_player, first_throw_counts)
        else:
            second_throw_counts = throw(current_player, second_throw_counts)
        continue

    if dartboard[next_row][next_col] == 'B':
        if first_player == current_player:
            first_throw_counts = throw(current_player, first_throw_counts)
            print(f'{current_player} won the game with {first_throw_counts} throws!')
        else:
            second_throw_counts = throw(current_player, second_throw_counts)
            print(f'{current_player} won the game with {second_throw_counts} throws!')

        break

    if dartboard[next_row][next_col] == 'D':
        if first_player == current_player:
            first_throw_counts = throw(current_player, first_throw_counts)
            first_score -= corresponding_numbers(next_row, next_col, dartboard) * 2
        else:
            second_throw_counts = throw(current_player, second_throw_counts)
            second_score -= corresponding_numbers(next_row, next_col, dartboard) * 2

    if dartboard[next_row][next_col] == 'T':
        if first_player == current_player:
            first_throw_counts = throw(current_player, first_throw_counts)
            first_score -= corresponding_numbers(next_row, next_col, dartboard) * 3
        else:
            second_throw_counts = throw(current_player, second_throw_counts)
            second_score -= corresponding_numbers(next_row, next_col, dartboard) * 3

    # other solution:
    # if dartboard[next_row][next_col] != 'T' and dartboard[next_row][next_col] != 'B'\
    #         and dartboard[next_row][next_col] != 'D':

    if dartboard[next_row][next_col].isdigit():
        if first_player == current_player:
            first_score -= int(dartboard[next_row][next_col])
            first_throw_counts = throw(current_player, first_throw_counts)
        else:
            second_score -= int(dartboard[next_row][next_col])
            second_throw_counts = throw(current_player, second_throw_counts)

    if first_score <= 0 or second_score <= 0:
        break

    player_move.append(current_player)

if first_score <= 0:
    print(f'{first_player} won the game with {first_throw_counts} throws!')
elif second_score <= 0:
    print(f'{second_player} won the game with {second_throw_counts} throws!')




