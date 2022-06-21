from collections import deque


def cup_chocolate_func(cups, chocolate, milkshake):
    cup = cups[0]
    choco = chocolate[-1]
    if cup <= 0:
        cups.popleft()
    elif choco <= 0:
        chocolate.pop()
    elif cup == choco:
        cups.popleft()
        chocolate.pop()
        milkshake += 1
    elif 0 < cup or choco < 0:
        if cup != choco:
            cups.popleft()
            cups.append(cup)
            chocolate[-1] -= 5

    return cups, chocolate, milkshake


chocolate = [int(x) for x in input().split(', ')]
cups = deque(int(x) for x in input().split(', '))
milkshake = 0

while cups and chocolate:
    cups, chocolate, milkshake = cup_chocolate_func(cups, chocolate,milkshake)

    if milkshake == 5:
        break

if milkshake == 5:
    print(f'Great! You made all the chocolate milkshakes needed!')
else:
    print(f'Not enough milkshakes.')
if chocolate:
    print(f"Chocolate: {', '.join(str(x) for x in chocolate)}")
else:
    print(f'Chocolate: empty')

if cups:
    print(f"Milk: {', '.join(str(x) for x in cups)}")
else:
    print(f'Milk: empty')
