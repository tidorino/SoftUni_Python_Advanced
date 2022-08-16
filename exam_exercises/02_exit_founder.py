players = input().split(', ')
player1 = players[0]
player2 = players[1]

n = 6
maze = [[x for x in input().split(' ')] for _ in range(n)]
resting_list = []

while True:
    players[0] = player1
    players[1] = player2
    coordinates = input().strip('()').split(', ')
    row = int(coordinates[0])
    col = int(coordinates[1])
    player1 = players[0]
    player2 = players[1]

    if player1 in resting_list:
        resting_list.remove(player1)
        player1, player2 = player2, player1
        continue

    elif maze[row][col] == 'E':
        print(f"{player1} found the Exit and wins the game!")
        break
    elif maze[row][col] == 'T':
        print(f"{player1} is out of the game! The winner is {player2}.")
        break
    elif maze[row][col] == 'W':
        if player1 in resting_list:
            resting_list.remove(player1)
        resting_list.append(player1)
        print(f"{player1} hits a wall and needs to rest.")

    player1, player2 = player2, player1



