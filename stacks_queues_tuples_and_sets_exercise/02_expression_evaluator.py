"""
input:

6 3 - 2 1 * 5 /

"""
from collections import deque

numbers = input().split(' ')
numb_queue = deque()

operations = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a // b,
}

for n in numbers:
    if n in '*/+-':
        while len(numb_queue) > 1:
            num1 = numb_queue.popleft()
            num2 = numb_queue.popleft()
            result = operations[n](num1, num2)
            numb_queue.appendleft(result)

    else:
        numb_queue.append(int(n))

print(*numb_queue)
