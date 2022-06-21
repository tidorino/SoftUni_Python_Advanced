from collections import deque

working_bees = deque(int(x) for x in input().split(' '))
nectars = [int(x) for x in input().split(' ')]
symbols = deque(input().split(' '))

operations = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a / b,
}
result = 0
while working_bees and nectars:
    bee = working_bees.popleft()
    nectar = nectars.pop()
    if nectar >= bee:
        symbol = symbols.popleft()
        result += abs(operations[symbol](bee, nectar))
    else:
        working_bees.appendleft(bee)

"""
*********** other solution ********
while working_bees and nectars:
    bee = working_bees.popleft()
    nectar = nectars.pop()
    if nectar < bee:
        working_bees.appendleft(bee)
        continue

    if nectar == 0:
        continue

    symbol = symbols.popleft()
    result += abs(operations[symbol](bee, nectar))
    
    Input:
20 62 99 35 0 150
120 60 10 1 70 10
+ - + + / * - - /

"""

print(f'Total honey made: {result}')

if working_bees:
    print(f"Bees left: {', '.join(str(x) for x in working_bees)}")
elif nectars:
    print(f"Nectar left: {', '.join(str(x) for x in nectars)}")

