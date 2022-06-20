from collections import deque

bullet_price = int(input())
size_gun_barrel = int(input())
bullets = [int(x) for x in input().split(' ')]    # stack
numb_locks = deque(int(x) for x in input().split(' '))
intelligence_value = int(input())

size = size_gun_barrel
bullet_count = 0

while numb_locks and bullets:

    bullet = bullets.pop()   # last el of stack
    lock = numb_locks[0]     # 1-st el of queue
    bullet_count += 1

    if bullet <= lock:
        print('Bang!')
        numb_locks.popleft()
        size -= 1

    else:
        print('Ping!')
        size -= 1
    if not bullets:
        break
    if size == 0:
        print('Reloading!')
        size = size_gun_barrel


money = intelligence_value - (bullet_price * bullet_count)
if not numb_locks:
    print(f'{len(bullets)} bullets left. Earned ${money}')

else:
    print(f"Couldn't get through. Locks left: {len(numb_locks)}")

