"""
Input:
11, 6, 8, 1
3, 1, 9, 10, 5, 9, 1

"""

from collections import deque

pizza_orders = deque(int(x) for x in input().split(', '))
employee_capacity = [int(x) for x in input().split(', ')]
total_pizzas = 0

while pizza_orders and employee_capacity:
    pizza = pizza_orders.popleft()
    employee = employee_capacity.pop()

    if pizza <= 0 or pizza > 10:
        employee_capacity.append(employee)
        continue

    if pizza > employee:
        pizza_left = pizza - employee
        pizza_orders.appendleft(pizza_left)
        total_pizzas += employee
    if pizza < employee:
        total_pizzas += pizza

if not pizza_orders:
    print("All orders are successfully completed!")
    print(f'Total pizzas made: {total_pizzas}')
    print(f'Employees: {", ".join([str(x) for x in employee_capacity])}')
if not employee_capacity:
    print('Not all orders are completed.')
    print(f'Orders left: {", ".join([str(x) for x in pizza_orders])}')
