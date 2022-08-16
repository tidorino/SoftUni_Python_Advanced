def check_if_hit(row, col, bucket_list):
    if [row, col] in bucket_list:
        return True
    else:
        return False


def is_not_inside(row, col, size):
    return row < 0 or col < 0 or row >= size or col >= size


def get_points(row, col, board, n):
    positions = {
        'up': (-1, 0),
        'down': (1, 0)
    }
    points = 0
    for position in positions:
        next_row = row + positions[position][0]
        next_col = col + positions[position][1]
        while not is_not_inside(next_row, next_col, n):
            points += int(board[next_row][next_col])

            next_row += positions[position][0]
            next_col += positions[position][1]

    return points


n = 6
board = [[x for x in input().split(' ')] for _ in range(n)]

bucket_list = []
total_points = 0

for _ in range(3):
    throw_command = [int(n) for n in input().strip("()").split(", ")]
    row, col = throw_command[0], throw_command[1]
    if is_not_inside(row, col, n):
        continue
    if board[row][col] == 'B':
        hit_bucket = check_if_hit(row, col, bucket_list)
        if hit_bucket:
            continue
        points = get_points(row, col, board, n)
        total_points += points
        bucket_list.append([row, col])

if 100 <= total_points <= 199:
    print(f"Good job! You scored {total_points} points, and you've won Football.")
elif 200 <= total_points <= 299:
    print(f"Good job! You scored {total_points} points, and you've won Teddy Bear.")
elif total_points >= 300:
    print(f"Good job! You scored {total_points} points, and you've won Lego Construction Set.")
else:
    needed_points = 100 - total_points
    print(f"Sorry! You need {needed_points} points more to win a prize.")
