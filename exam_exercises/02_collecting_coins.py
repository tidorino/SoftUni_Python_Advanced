def get_next_position(row, col, position):
    if position == 'up':
        return row - 1, col
    if position == 'down':
        return row + 1, col
    if position == 'right':
        return row, col + 1
    if position == 'left':
        return row, col - 1


def get_new_position(row, col, position):
    if position == 'up':
        return n - 1, col
    if position == 'down':
        return 0, col
    if position == 'right':
        return row, 0
    if position == 'left':
        return row, n - 1


n = int(input())

field = [[x for x in input().split(" ")] for _ in range(n)]
player_row = 0
player_col = 0
coins = 0

player_path = []

for row in range(n):
    for column in range(n):
        if field[row][column] == 'P':
            player_row = row
            player_col = column
player_path.append([player_row, player_col])

while True:
    command = input()

    next_row, next_col = get_next_position(player_row, player_col, command)

    if 0 > next_row or 0 > next_col or next_row >= n or next_col >= n:
        next_row, next_col = get_new_position(next_row, next_col, command)

    player_path.append([next_row, next_col])
    if field[next_row][next_col] == 'X':
        coins = coins // 2
        print(f"Game over! You've collected {round(coins)} coins.")
        break

    value = field[next_row][next_col]
    if value.isdigit():
        coins += int(value)
        field[next_row][next_col] = '*'

    player_row, player_col = next_row, next_col


    if coins >= 100:
        break


if coins >= 100:
    print(f"You won! You've collected {round(coins)} coins.")

print(f'Your path: ')
for item in player_path:
    print(item)

