rows, columns = [int(x) for x in input().split()]

matrix = [[x for x in input().split()] for _ in range(rows)]
squares = 0

for row in range(rows - 1):
    for column in range(columns - 1):
        if matrix[row][column] == matrix[row][column + 1] == matrix[row + 1][column] == matrix[row + 1][column + 1]:
            squares += 1

print(squares)

