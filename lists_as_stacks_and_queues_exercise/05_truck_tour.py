"""
There is a circle road with N petrol pumps.
You will receive two pieces of information (separated by a single space):
-	The amount of petrol the petrol pump will give you
-	The distance from that petrol pump to the next petrol pump (kilometers)
The truck consumes 1 liter of petrol per 1 kilometer, and its tank has infinite petrol capacity.
In the beginning, the tank is empty.
Your task is to calculate the first petrol pump from where the truck will be able to complete the circle.
You never miss filling its tank at a petrol pump.

"""


from collections import deque

petrol_pumps = int(input())

pumps = deque()


for _ in range (petrol_pumps):
    pumps.append([int(x) for x in input().split()])

for attempt in range(petrol_pumps):
    failed = False
    tank = 0
    for petrol, distance in pumps:
        tank = tank + petrol - distance
        if tank < 0:
            failed = True
            break

    if failed:
        pumps.append(pumps.popleft())

    else:
        print(attempt)
        break
