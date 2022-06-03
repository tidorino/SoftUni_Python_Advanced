rows, columns = [int(x) for x in input().split()]

for row in range(rows):
    for column in range(columns):
        print(f'{chr(97 + row)}{chr(97 + row + column)}{chr(97 + row)}', end=" ")
    print()
