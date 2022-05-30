n = int(input())
matrix = []
for _ in range(n):
    column = [int(x) for x in input().split(', ')]
    matrix.append(list(m for m in column if m % 2 == 0))

print(matrix)
