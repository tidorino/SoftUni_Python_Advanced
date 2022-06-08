rows, columns = [int(x) for x in input().split()]

matrix = []

bunnies = set()
player_row = 0
player_col = 0
for row in range(rows):
    row_elements = list(input())
    for column in range(columns):

        if row_elements[column] == 'P':
            player_row = row
            player_col = column
        elif row_elements[column] == 'B':
            bunnies.add(f'{row},{column}')

    matrix.append(row_elements)

commands = input().split()

