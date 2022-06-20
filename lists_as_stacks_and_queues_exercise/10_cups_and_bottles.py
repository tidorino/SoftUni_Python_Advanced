from collections import deque

cups = deque(int(x) for x in input().split(' '))
bottles = [int(x) for x in input().split(' ')]

wasted_water = 0

while bottles and cups:
    bottle = bottles.pop()
    cup = cups[0]

    if bottle >= cup:
        wasted_water += bottle - cup
        cups.popleft()
    else:
        cup -= bottle
        cups.popleft()
        cups.appendleft(cup)

if not cups:
    print(f"Bottles: {' '.join(str(x) for x in bottles)}")
elif not bottles:
    print(f"Cups: {' '.join(str(x) for x in cups)}")

print(f'Wasted litters of water: {wasted_water}')

