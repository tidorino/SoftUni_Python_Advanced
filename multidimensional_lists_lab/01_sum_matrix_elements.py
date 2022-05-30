n, m = [int(x) for x in input().split(', ')]
matrix = []
total_sum = 0
for _ in range(n):
    row = [int(x) for x in input().split(', ')]
    total_sum += sum(row)
    matrix.append(row)

print(total_sum)
print(matrix)
