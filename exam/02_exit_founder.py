"""
*******Input*****
Jerry, Tom
. . . W . .
. . T T . .
. . . . . .
. T . W . .
W . . . E .
. . . W . .
(0, 3)
(3, 3)
(1, 3)
(2, 2)
(3, 5)
(4, 0)
(5, 3)
(3, 1)
(4, 4)
(4, 4)

"""

from collections import deque

first_player, second_player = input().split(', ')

n = 6
matrix= [[x for x in input().split(' ')] for _ in range(n)]

player_move = deque([first_player, second_player])
player_rest = []

while True:
    position = input().strip('()').split(', ')
    next_row, next_col = int(position[0]), int(position[1])

    current_player = player_move.popleft()
    if current_player in player_rest:
        player_rest.remove(current_player)
        player_move.append(current_player)
        continue

    if matrix[next_row][next_col] == 'E':
        print(f'{current_player} found the Exit and wins the game!')
        break
    if matrix[next_row][next_col] == 'T':
        print(f'{current_player} is out of the game! The winner is {"".join(player_move)}.')
        break
    if matrix[next_row][next_col] == 'W':
        print(f'{current_player} hits a wall and needs to rest.')
        player_rest.append(current_player)

    player_move.append(current_player)
