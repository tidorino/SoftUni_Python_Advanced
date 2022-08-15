from collections import deque

orders_of_pizza = deque([int(p) for p in input().split(', ')])
employees_capacity = [int(e) for e in input().split(', ')]
count_pizzas = 0

while orders_of_pizza and employees_capacity:
    pizza_order = orders_of_pizza.popleft()
    employee_capacity = employees_capacity.pop()
    if pizza_order > 10:
        employees_capacity.append(employee_capacity)

    elif pizza_order <= 0:
        employees_capacity.append(employee_capacity)

    elif pizza_order > employee_capacity:
        left_pizzas = pizza_order - employee_capacity
        orders_of_pizza.appendleft(left_pizzas)
        count_pizzas += employee_capacity
    else:
        count_pizzas += pizza_order

if not orders_of_pizza:
    print(f"All orders are successfully completed!\n"
          f"Total pizzas made: {count_pizzas}\n"
          f"Employees: {', '.join([str(e) for e in employees_capacity])}")
if not employees_capacity:
    print(f"Not all orders are completed.\nOrders left: {', '.join([str(p) for p in orders_of_pizza])}")
