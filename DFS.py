import collections
import time
import sys
from MazeCreate import create_maze as m


def DFS_algo():
    maze = m()
    maze_cords = []
    notvisited = []
    start = []
    finish = []
    stack = []
    step = []

    for i, c in enumerate(maze):
        for j, h in enumerate(c):
            if h == 'S':
                start.append([i, j])

    for i, c in enumerate(maze):
        for j, h in enumerate(c):
            if h == 'G':
                finish.append([i, j])

    for i, c in enumerate(maze):
        for j, h in enumerate(c):
            maze_cords.append([[i, j]])

    for i, c in enumerate(maze):
        for j, h in enumerate(c):
            if h == ' ' or h == 'G' or h == 'S':
                notvisited.append([i, j])

    stack.append(start)

    for i, c in enumerate(notvisited):
        if stack in c:
            notvisited.pop(i)

    while stack:
        step = stack.pop()
        num = []

        if step[0] == finish[0]:
            for i in maze:
                print(i)
            break

        for j, h in enumerate(notvisited):
            if h == step:
                notvisited.pop(j)
                break
            for k in j:
                for i in maze_cords[k]:
                    if i in notvisited:
                        stack.append([i])
                        if maze[i[0]][i[1]] != 'S' and maze[i[0]][i[1]] != 'S' and maze[i[0]][i[1]] != 'G':
                            maze[i[0]][i[1]] = 'W'

            time.sleep(1)
            for i in maze:
                print(i, end='\n', flush=True)

DFS_algo()
