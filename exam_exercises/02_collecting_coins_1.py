def is_not_inside(row, col, size):
    return row < 0 or col < 0 or row >= size or col >= size


def get_next_position(row, col, position, size):
    if position == 'up':
        row -= 1
        if is_not_inside(row, col, size):
            return n - 1, col
        else:
            return row, col
    if position == 'down':
        row += 1
        if is_not_inside(row, col, size):
            return 0, col
        else:
            return row, col
    if position == 'right':
        col += 1
        if is_not_inside(row, col, size):
            return row, 0
        else:
            return row, col
    if position == 'left':
        col -= 1
        if is_not_inside(row, col, size):
            return row, n - 1
        else:
            return row, col


n = int(input())
matrix = [[x for x in input().split(' ')] for _ in range(n)]
player_row = 0
player_col = 0
coins = 0
player_path = []

for row in range(n):
    for col in range(n):
        if matrix[row][col] == 'P':
            player_row = row
            player_col = col
player_path.append([player_row,player_col])

while True:
    command = input()

    next_row, next_col = get_next_position(player_row, player_col, command, n)
    player_path.append([next_row, next_col])
    if matrix[next_row][next_col] == 'X':
        coins = coins // 2
        print(f"Game over! You've collected {round(coins)} coins.")
        break

    if matrix[next_row][next_col].isdigit():
        number = matrix[next_row][next_col]
        coins += int(number)
        matrix[next_row][next_col] = '.'

    player_row, player_col = next_row, next_col
    if coins >= 100:
        break

if coins >= 100:
    print(f"You won! You've collected {round(coins)} coins.")

result = f'Your path:\n'
for row, col in player_path:
    result += f'[{row}, {col}]\n'
print(result)

# print('Your path:')
# for item in player_path:
#     print(item)
