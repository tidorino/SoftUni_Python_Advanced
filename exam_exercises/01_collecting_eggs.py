from collections import deque

eggs = deque(int(x) for x in input().split(', '))
papers = [int(x) for x in input().split(', ')]

box_size = 50
box_counter = 0

while eggs and papers:
    egg = eggs.popleft()
    paper = papers.pop()
    sum_of_egg_and_paper = egg + paper

    if egg <= 0:
        papers.append(paper)
    elif egg == 13:
        papers.append(paper)
        papers[0], papers[-1] = papers[-1], papers[0]
    elif sum_of_egg_and_paper <= box_size:
        box_counter += 1

if box_counter:
    print(f'Great! You filled {box_counter} boxes.')
else:
    print(f"Sorry! You couldn't fill any boxes!")

if eggs:
    print(f"Eggs left: {', '.join(str(e) for e in eggs)}")

if papers:
    print(f"Pieces of paper left: {', '.join(str(p) for p in papers)}")

