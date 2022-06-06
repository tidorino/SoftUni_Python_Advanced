"""
Your program should receive commands in the format: "swap {row1} {col1} {row2} {col2}"
where ("row1", "col1") and ("row2", "col2") are the coordinates of two points in the matrix.
A valid command starts with the "swap" keyword along with four valid coordinates (no more, no less),
separated by a single space.
•	If the command is valid, you should swap the values at the given indexes and print the matrix
at each step (thus, you will be able to check if the operation was performed correctly).
•	If the command is not valid (does not contain the keyword "swap", has fewer or more coordinates entered,
or the given coordinates are not valid), print "Invalid input!" and move on to the following command.
A negative value makes the coordinates not valid.
Your program should finish when the command "END" is entered.

2 3
1 2 3
4 5 6
swap 0 0 1 1
swap 10 9 8 7
swap 0 1 1 0
END

"""

rows, columns = [int(x) for x in input().split()]

matrix = [[x for x in input().split()] for _ in range(rows)]

while True:
    command = input()

    if command == 'END':
        break

    new_command = command.split()

    if len(new_command) != 5 or new_command[0] != 'swap':
        print("Invalid input!")
        continue

    row1, column1, row2, column2 = [int(x) for x in new_command[1:]]

    if row1 > rows or row2 > rows or column1 > columns or column2 > columns:
        print("Invalid input!")

    elif new_command[0] == 'swap' and len(new_command) == 5:
        matrix[row1][column1], matrix[row2][column2] = matrix[row2][column2], matrix[row1][column1]

        for row in matrix:
            print(*row, sep=" ")

