"""
You will be given an integer n for the size of the Wonderland territory with a square shape.
On the following n lines, you will receive the rows of the territory:
•	Alice will be placed in a random position, marked with the letter "A".
•	On the territory, there will be bags of tea, represented as numbers.
If Alice steps on a number position, she collects the tea bags and increases the quantity with the corresponding number.
•	There will always be one rabbit hole on the territory marked with the letter "R".
•	All of the empty positions will be marked with ".".
After the field state, you will be given commands for Alice's movements.
Move commands can be: "up", "down", "left" or "right".
When Alice collects at least 10 bags of tea, she is ready to go to the tea party,
and she does not need to continue collecting. Otherwise, if she steps on the rabbit hole
or goes out of the territory, she can't return, and the program ends.
In the end, the path she walked had to be marked with '*'.

*********
5
. A . . 1
R . 2 . .
4 7 . 1 .
. . . 2 .
. 3 . . .
down
right
left
down
up
left

"""
def get_next_position(row, col, position):
    if position == 'up':
        return row - 1, col
    if position == 'down':
        return row + 1, col
    if position == 'right':
        return row, col + 1
    if position == 'left':
        return row, col - 1


n = int(input())

territory_matrix = [[x for x in input().split(' ')] for _ in range(n)]
alice_row = 0
alice_col = 0

for row in range(n):
    for column in range(n):
        if territory_matrix[row][column] == 'A':
            alice_row = row
            alice_col = column

tea_bag_counter = 0

while tea_bag_counter < 10:
    territory_matrix[alice_row][alice_col] = '*'

    command = input()
    next_row, next_col = get_next_position(alice_row, alice_col, command)

    if next_row < 0 or next_col < 0 or next_row >= n or next_col >= n:
        break

    alice_row, alice_col = next_row, next_col

    if territory_matrix[alice_row][alice_col] == '.' or territory_matrix[alice_row][alice_col] == '*':
        continue

    if territory_matrix[alice_row][alice_col] == 'R':
        break

    tea_bag_counter += int(territory_matrix[alice_row][alice_col])

territory_matrix[alice_row][alice_col] = '*'

if tea_bag_counter >= 10:
    print(f"She did it! She went to the party.")
else:
    print(f"Alice didn't make it to the tea party.")

for i in territory_matrix:
    print(*i, sep=' ')
