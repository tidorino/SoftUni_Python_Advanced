from collections import deque

str_numbers = input()
numbers = deque(str_numbers.split())

target_numb = int(input())

for i in numbers:
    
    numbers.popleft(i)

