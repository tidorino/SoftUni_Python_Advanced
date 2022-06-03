import sys

"""
Write a program that reads a rectangular matrix's dimensions and finds
the 3x3 square with a maximum sum of its elements.
There will be no case with two or more 3x3 squares with equal maximal sum.

"""

rows, columns = [int(x) for x in input().split()]

matrix = [[int(x) for x in input().split()] for _ in range(rows)]

total_sum_of_elements = - sys.maxsize
index_row = 0  # start_element_index_best_sum_3x3_matrix
index_column = 0  # start_element_index_best_sum_3x3_matrix

for row in range(rows - 2):
    for column in range(columns - 2):
        sum_of_elements = matrix[row][column] + matrix[row][column + 1] + matrix[row][column + 2]\
                          + matrix[row + 1][column] + matrix[row + 1][column + 1] + matrix[row + 1][column + 2]\
                          + matrix[row + 2][column] + matrix[row + 2][column + 1] + matrix[row + 2][column + 2]
        if total_sum_of_elements < sum_of_elements:
            total_sum_of_elements = sum_of_elements
            index_row = row
            index_column = column

print(f'Sum = {total_sum_of_elements}')
print(f'{matrix[index_row][index_column]} {matrix[index_row][index_column + 1]} {matrix[index_row][index_column + 2]}')
print(f'{matrix[index_row + 1][index_column]} {matrix[index_row + 1][index_column + 1]}'
      f' {matrix[index_row + 1][index_column + 2]}')
print(f'{matrix[index_row + 2][index_column]} {matrix[index_row + 2][index_column + 1]}'
      f' {matrix[index_row + 2][index_column + 2]}')



