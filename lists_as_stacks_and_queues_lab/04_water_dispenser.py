from collections import deque

quantity_water = int(input())

queue = deque()

while True:
    command = input()
    if command == 'Start':
        break

    queue.append(command)

while True:
    command = input()
    if command == 'End':
        print(f"{quantity_water} liters left")
        break

    elif 'refill' in command:         # if command.startwith('refill'):
        new_command = command.split(" ")
        water_refill = int(new_command[1])
        quantity_water += water_refill

    else:
        water_wanted = int(command)
        person = queue.popleft()

        if water_wanted <= quantity_water:
            print(f"{person} got water")
            quantity_water -= water_wanted
        else:
            print(f"{person} must wait")










