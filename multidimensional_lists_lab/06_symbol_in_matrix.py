def symbol_in_matrix(info, char):
    for row_index in range(n):
        for column_index in range(n):
            if matrix[row_index][column_index] == symbol:
                return row_index, column_index

    return None


n = int(input())

matrix = [[x for x in input()]for _ in range(n)]
symbol = input()

result = symbol_in_matrix(matrix, symbol)

if result:
    row_ind, column_ind = result
    print(f'({row_ind}, {column_ind})')
else:
    print(f'{symbol} does not occur in the matrix')


