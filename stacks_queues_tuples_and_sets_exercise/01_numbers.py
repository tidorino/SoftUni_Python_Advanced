first_sequence = set([int(x) for x in input().split()])
second_sequence = set([int(x) for x in input().split()])

number = int(input())
for _ in range(number):
    command_parts = input().split()
    command = command_parts[0]
    target_sequence = command_parts[1]

    if command == 'Add':
        if target_sequence == 'First':
            first_sequence = first_sequence.union([int(x) for x in command_parts[2:]])
        else:
            second_sequence = second_sequence.union([int(x) for x in command_parts[2:]])
    elif command == 'Remove':
        if target_sequence == 'First':
            first_sequence = first_sequence.difference([int(x) for x in command_parts[2:]])
        else:
            second_sequence = second_sequence.difference([int(x) for x in command_parts[2:]])
    else:
        print(first_sequence.issubset(second_sequence) or second_sequence.issubset(first_sequence))

print(', '.join([str(x) for x in first_sequence]))
print(', '.join([str(x) for x in second_sequence]))

