from collections import deque

'''
Every n-th toss, the child holding the 
potato leaves the game. When a kid leaves the game, it passes
the potato to the next kid. It continues until there is only one kid left.
"George Peter Michael William Thomas"
"10"
'''

kids_string = input().split(" ")
kids = deque(kids_string)
toss_count = int(input())
counter = 0

while len(kids) > 1:
    kid = kids.popleft()
    counter += 1
    if counter < toss_count:
        kids.append(kid)

    else:
        counter = 0
        print(f"Removed {kid}")

print(f"Last is {kids.popleft()}")
