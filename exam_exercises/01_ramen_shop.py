"""
You will be given two sequences of integers representing bowls of ramen and customers.
Your task is to find out if you can serve all the customers.
Start by taking the last bowl of ramen and the first customer. Try to serve every customer with ramen
until we have no more ramen or customers left:
•	Each time the value of the ramen is equal to the value of the customer, remove them both and continue with
the next bowl of ramen and the next customer.
•	Each time the value of the ramen is bigger than the value of the customer, decrease the value of that
ramen with the value of that customer and remove the customer. Then try to match the same bowl of ramen (which has been decreased) with the next customer.
•	Each time the customer's value is bigger than the value of the ramen bowl, decrease the value of the customer
with the value of the ramen bowl and remove the bowl. Then try to match the same customer
(which has been decreased) with the next bowl of ramen.

Input:
14, 25, 37, 43, 19
58, 23, 37

"""

from collections import deque

bowls = deque(int(x) for x in input().split(', '))
customers = deque(int(x) for x in input().split(', '))

while bowls and customers:
    bowl = bowls.pop()
    customer = customers.popleft()
    if bowl == customer:
        continue

    elif bowl > customer:
        bowl -= customer
        bowls.append(bowl)
    elif bowl < customer:
        customer -= bowl
        customers.appendleft(customer)

if bowls:
    print('Great job! You served all the customers.')
    print(f"Bowls of ramen left: {', '.join(str(x) for x in bowls)}")
elif customers:
    print("Out of ramen! You didn't manage to serve all customers.")
    print(f"Customers left: {', '.join(str(x) for x in customers)}")
else:
    print('Great job! You served all the customers.')

