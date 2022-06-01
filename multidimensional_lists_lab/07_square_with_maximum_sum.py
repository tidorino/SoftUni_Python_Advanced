"""
Write a program that reads a matrix from the console and finds the 2x2 top-left submatrix
with biggest sum of its values.
You should print the found submatrix and the sum of its elements, as shown in the examples.
Input	              Output
3, 6                     9 8
7, 1, 3, 3, 2, 1         7 9
1, 3, 9, 8, 5, 6         33
4, 6, 7, 9, 1, 0

"""
import sys

rows, columns = [int(x) for x in input().split(', ')]

matrix = [[int(x) for x in input().split(', ')]for _ in range(rows)]

max_sum = - sys.maxsize
position = None

for row in range(rows - 1, 0, -1):
    for column in range(columns - 1, 0, - 1):

        current_sum = matrix[row][column] + matrix[row][column - 1]\
                      + matrix[row - 1][column] + matrix[row - 1][column - 1]
        if current_sum >= max_sum:
            max_sum = current_sum
            position = (row, column)

row, column = position
print(matrix[row - 1][column - 1], matrix[row - 1][column])
print(matrix[row][column - 1], matrix[row][column])
print(max_sum)


