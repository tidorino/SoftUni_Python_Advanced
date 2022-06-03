n = int(input())

matrix = [[int(x) for x in input().split(' ')] for _ in range(n)]
primary_diagonal = []
secondary_diagonal = []

for index in range(n):
    primary_diagonal.append(matrix[index][index])
    secondary_diagonal.append(matrix[index][n - 1 - index])

absolute_sum = abs(sum(primary_diagonal) - sum(secondary_diagonal))
print(absolute_sum)
