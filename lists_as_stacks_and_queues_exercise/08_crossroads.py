"""
Sam is on a single lane of cars that queue until the light goes green.
When it does, they start passing one by one on a flashing green light and during the free window
before the intersecting road's light goes green. For each second, only one part of a car
(a single character) passes the crossroad. If a car is still in the middle of the crossroads
when the free window ends, it will get hit at the first character that is still in the crossroads.
A green light cycle goes as follows:
•	During the green light, cars will enter and exit the crossroads one by one
•	During the free window, cars will only exit the crossroads

10
5
Mercedes
green
Mercedes
BMW
Skoda
green
END

"""

from collections import deque

green_line_duration = int(input())
free_window_duration = int(input())

cars_commands = deque()
total_cars_passed = 0
crashed = False

while not crashed:
    command = input()
    if command == 'END':
        break

    if command == 'green':
        green_duration = green_line_duration

        while cars_commands and green_duration > 0:
            car = cars_commands.popleft()
            seconds_to_pass = green_duration + free_window_duration

            if seconds_to_pass >= len(car):
                green_duration -= len(car)
                total_cars_passed += 1
                crashed = False
            else:
                print('A crash happened!')
                print(f"{car} was hit at {car[seconds_to_pass]}.")
                crashed = True
                break

    else:
        cars_commands.append(command)

if not crashed:
    print(f'Everyone is safe.')
    print(f"{total_cars_passed} total cars passed the crossroads.")

