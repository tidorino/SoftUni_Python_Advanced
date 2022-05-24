"""
You will be given the quantity of the food you have for the day (an integer number).
You will be given a sequence of integers (separated by a single space), each representing the quantity of food in each order.
Keep the orders in a queue.
Find the biggest order and print it.
Next, you will begin servicing your clients from the first one that came. Before each order, check if you have
enough food left to complete it:
•	If you have, remove the order from the queue and reduce the quantity of food in the restaurant.
•	Otherwise, stop serving
"""

from collections import deque

quantity_of_food = int(input())
each_order = [int(x) for x in input().split()]
order_queue = deque()
for order in each_order:
    order_queue.append(order)

biggest_order = max(order_queue)
print(biggest_order)

orders_complete = True
order_left = []
while order_queue:
    current_order = order_queue.popleft()
    if current_order <= quantity_of_food:
        quantity_of_food -= current_order
        orders_complete = True

    else:
        order_left += [str(current_order)]
        orders_complete = False
        break

if orders_complete:
    print(f"Orders complete")
else:

    for i in order_queue:
        order_left.append(str(i))
    orders_left = " ".join(order_left)
    print(f"Orders left: {orders_left}")
