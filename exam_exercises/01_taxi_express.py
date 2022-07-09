from collections import deque

customers = deque(int(x) for x in input().split(','))
taxis = [int(x) for x in input().split(',')]
total_time = 0
current_time = 0
while customers and taxis:
    customer = customers.popleft()
    taxi = taxis.pop()

    if customer <= taxi:
        total_time += customer
    else:
        customers.appendleft(customer)

if not customers:
    print(f'All customers were driven to their destinations\nTotal time: {total_time} minutes')
if customers and not taxis:
    print(f'Not all customers were driven to their destinations\nCustomers left:'
          f' {", ".join([str(x) for x in customers])}')


