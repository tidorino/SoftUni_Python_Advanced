"""
The current project is assembly-line robots.
Each robot has a processing time – it is the time in seconds the robot needs to process a product.
When a robot is free, it should take a product for processing and log its name, product, and processing start time.
Each robot processes a product coming from the assembly line. A product is coming from the line each second
(so the first product should appear at [start time + 1 second]).
If a product passes the line and there is not a free robot to take it, it should be queued at the end of the line again.
The robots are standing in the line in the order of their appearance.

Input:
ROB-15;SS2-10;NX8000-3
8:00:00
detail
glass
wood
apple
End

"""

from collections import deque


def robotic_info():
    info = input().split(";")
    robot_dic = {}
    for rob in info:
        name, process_time = rob.split("-")
        robot_dic[name] = int(process_time)
    return robot_dic


def time_in_seconds():
    hour, minute, sec = input().split(":")
    total_seconds = int(hour) * 60 * 60 + int(minute) * 60 + int(sec)
    return total_seconds


def product_queue():
    items = deque()
    while True:
        item_on_line = input()
        if item_on_line == 'End':
            break
        items.append(item_on_line)
    return items


def convert(seconds):
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60

    return f'{hour:02d}:{minutes:02d}:{seconds:02d}'


robotics = robotic_info()
starting_time = time_in_seconds()
products = product_queue()

available_robots = [k for k in robotics.keys()]
processing_robots = {}

while products:

    starting_time = starting_time + 1
    time = convert(starting_time)

    for robot_name in [k for k in processing_robots.keys()]:
        processing_robots[robot_name] -= 1
        if processing_robots[robot_name] <= 0:
            processing_robots.pop(robot_name)
    current_item = products.popleft()

    for robot_name in available_robots:
        if robot_name not in processing_robots:
            print(f"{robot_name} - {current_item} [{time}]")
            processing_robots[robot_name] = robotics[robot_name]
            break

    else:
        products.append(current_item)



