rows = int(input())
matrix = [[int(x) for x in input().split(' ')] for _ in range(rows)]

while True:
    command = input()
    if command == 'END':
        for row in matrix:
            print(*row, sep=' ')
        break

    new_command = command.split(' ')
    row, col, value = [int(x) for x in new_command[1:]]

    if row < 0 or col < 0 or row >= rows or col >= rows:
        print(f'Invalid coordinates')
        continue

    if new_command[0] == 'Add':
        matrix[row][col] += value

    else:
        matrix[row][col] -= value


