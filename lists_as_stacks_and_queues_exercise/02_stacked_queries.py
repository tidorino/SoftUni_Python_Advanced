"""
You have an empty stack. You will receive an integer – N.
On the next N lines, you will receive queries.

9
1 97
2
1 20
2
1 26
1 20
3
1 91
4

"""

queries_count = int(input())

stack = []

for _ in range(queries_count):
    query_parts = input().split()
    # !!! query_parts = [int(x) for x in input().split()]

    command = int(query_parts[0])
    # ! command = query_parts[0]

    if command == 1:
        number = query_parts[1]
        stack.append(number)
    elif command == 2 and stack:
        stack.pop()
    elif command == 3 and stack:
        print(max(stack))
    elif command == 4 and stack:
        print(min(stack))

reversed_stack = []
while stack:

    reversed_stack.append(str(stack.pop()))

print(", ".join(reversed_stack))



