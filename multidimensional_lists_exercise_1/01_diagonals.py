n = int(input())

matrix = [[int(x) for x in input().split(', ')] for _ in range(n)]
primary_diagonal = []
secondary_diagonal = []

for row in range(n):
    for column in range(n):
        if column == row:
            primary_diagonal.append(matrix[row][column])

        if row == n - column - 1:
            secondary_diagonal.append(matrix[row][column])

print(f'Primary diagonal: {", ".join(str(x) for x in primary_diagonal)}. Sum: {sum(primary_diagonal)}')
print(f'Secondary diagonal: {", ".join(str(x) for x in secondary_diagonal)}. Sum: {sum(secondary_diagonal)}')
