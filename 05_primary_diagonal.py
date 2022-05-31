def get_primary_diagonal_sum(matrix):
    n = len(matrix)
    return sum(matrix[i][i] for i in range(n))


n_square_matrix = int(input())
square_matrix = [[int(x) for x in input().split()]for _ in range(n_square_matrix)]

print(get_primary_diagonal_sum(square_matrix))

# *********** OTHER SOLUTION - a bit longer ***************

# n_square_matrix = int(input())
# square_matrix = [[int(x) for x in input().split()]for _ in range(n_square_matrix)]
# sum_primary_diagonal = 0
# for n in range(n_square_matrix):
#     for m in range(n_square_matrix):
#         if n == m:
#             sum_primary_diagonal += square_matrix[n][m]
# print(sum_primary_diagonal)
