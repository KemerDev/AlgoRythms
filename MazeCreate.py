import random


def create_maze():
    start = 'S'
    goal = 'G'
    wall = '#'
    road = ' '
    temp = []
    maze = []

    mazerow = 10
    mazecol = 10

    for i in range(mazerow):
        for j in range(mazecol):
            rand_col = random.randint(1, mazecol - 2)
            if j == rand_col:
                temp.append(wall)
            elif i == 0 or i == (mazerow - 1):
                temp.append(wall)
            elif j == 0 or j == (mazecol - 1):
                temp.append(wall)
            else:
                temp.append(road)
        maze.append(temp)
        temp = []

    row = random.randint(0, mazerow - 1)
    col = random.randint(0, mazecol - 1)

    for i, c in enumerate(maze):
        for j, h in enumerate(c):
            if i == row and j == col:
                maze[i][j] = start
                break

    row = random.randint(0, mazerow - 1)
    col = random.randint(0, mazecol - 1)

    for i, c in enumerate(maze):
        for j, h in enumerate(c):
            if (i == row and j == col) and h != start:
                maze[i][j] = goal
                break

    return maze