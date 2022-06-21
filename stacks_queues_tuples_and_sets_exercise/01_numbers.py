first_sequence = set([int(x) for x in input().split()])
second_sequence = set([int(x) for x in input().split()])

number = int(input())
for _ in range(number):
    command_parts = input().split()
    command = command_parts[0]
    target_sequence = command_parts[1]

    if command == 'Add':
        numbs = [int(x) for x in command_parts[2:]]
        if target_sequence == 'First':
            first_sequence = first_sequence.union(numbs)
        else:
            second_sequence = second_sequence.union(numbs)
    elif command == 'Remove':
        numbs = [int(x) for x in command_parts[2:]]
        if target_sequence == 'First':
            first_sequence = first_sequence.difference(numbs)
        else:
            second_sequence = second_sequence.difference(numbs)
    else:
        print(first_sequence.issubset(second_sequence) or second_sequence.issubset(first_sequence))

# print(', '.join([str(x) for x in first_sequence]))
# print(', '.join([str(x) for x in second_sequence]))
print(*first_sequence, sep=', ')
print(*second_sequence, sep=', ')
