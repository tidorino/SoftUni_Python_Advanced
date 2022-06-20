numbers = [int(x) for x in input().split(' ')]
target_numb = int(input())
set_unique_pairs = set()
iterations = 0
while numbers:
    num1 = numbers[0]
    for n in range(1, len(numbers)):
        iterations += 1
        num2 = numbers[n]

        if num1 + num2 == target_numb:
            print(f'{num1} + {num2} = {target_numb}')
            set_unique_pairs.add((num1, num2))

    numbers.remove(num1)

print(f'Iterations done: {iterations}')
print(*set_unique_pairs, sep='\n')
