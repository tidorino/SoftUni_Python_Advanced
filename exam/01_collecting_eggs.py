"""
Input:
20, 13, -7, 7
10, 5, 20, 15, 7, 9

"""

from collections import deque

eggs = deque(int(x) for x in input().split(', '))
papers = deque(int(x) for x in input().split(', '))

box_counter = 0

while eggs and papers:
    egg = eggs.popleft()
    paper = papers.pop()
    if egg == 13:
        first_paper = papers.popleft()
        papers.append(first_paper)
        papers.appendleft(paper)
        continue
    if egg <= 0:
        papers.append(paper)
        continue
    if (egg + paper) <= 50:
        box_counter += 1

if box_counter:
    print(f'Great! You filled {box_counter} boxes.')
else:
    print(f"Sorry! You couldn't fill any boxes!")

if eggs:
    print(f"Eggs left: {', '.join(str(x) for x in eggs)}")
if papers:
    print(f"Pieces of paper left: {', '.join(str(x) for x in papers)}")


