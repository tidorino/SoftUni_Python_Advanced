from collections import deque


def flights(*args):
    destination = {}
    args_queue = deque(args)

    while args_queue[0] != 'Finish':
        city = args_queue.popleft()
        passengers = args_queue.popleft()
        if city not in destination:
            destination[city] = passengers
        else:
            destination[city] += passengers

    return destination

print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))

print(flights('London', 0, 'New York', 9, 'Aberdeen', 215, 'Sydney', 2, 'New York', 300, 'Nice', 0, 'Finish'))
print(flights('Finish', 'New York', 90, 'Aberdeen', 300, 'Sydney', 0))