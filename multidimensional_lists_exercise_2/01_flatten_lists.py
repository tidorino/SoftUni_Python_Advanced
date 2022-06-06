string = input().split("|")
matrix = []

for element in string:
    number = list(map(int, element.split()))
    matrix.append(number)

for el in reversed(matrix):
    for i in el:
        print(i, end=' ')
