n = int(input())
matrix = [[int(x) for x in input().split(', ')] for _ in range(n)]
# for _ in range(n):
#     row = [int(x) for x in input().split(', ')]
#     for m in row:
#         matrix.append(m)
flattened_matrix = [m for row in matrix for m in row]
print(flattened_matrix)

