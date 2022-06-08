"""
Your job is to determine the direction in which the bunny should
go to collect the maximum number of eggs. The directions that should be considered
as possible are up, down, left, and right. If you reach a trap while checking some of the directions,
you should not consider the fields after the trap in this direction.

•	One bunny - randomly placed in it and marked with the symbol "B"
•	Number of eggs placed at different positions of the field and traps marked with "X"

*********
5
1 3 7 9 11
X 5 4 X 63
7 3 21 95 1
B 1 73 4 9
9 2 33 2 0

"""
import sys

n = int(input())

field = [[x for x in input().split(' ')] for _ in range(n)]
bunny_row = 0
bunny_col = 0

for row in range(n):
    for column in range(n):
        if field[row][column] == 'B':
            bunny_row = row
            bunny_col = column
            # count = collect_eggs(field, row, column)

directions = {
    'right': lambda r, c: (r, c + 1),
    'left': lambda r, c: (r, c - 1),
    'up': lambda r, c: (r - 1, c),
    'down': lambda r, c: (r + 1, c)
}
best_sum = -sys.maxsize
best_direction = ''
best_path = []

for direction in directions:
    row, col = directions[direction](bunny_row, bunny_col)
    current_sum = 0
    current_path = []

    while 0 <= row < n and 0 <= col < n and field[row][col] != 'X':
        current_sum += int(field[row][col])
        current_path.append([row, col])
        row, col = directions[direction](row, col)

    if current_sum > best_sum and current_path:
        best_sum = current_sum
        best_direction = direction
        best_path = current_path

print(best_direction)
print(*best_path, sep='\n')
print(best_sum)



