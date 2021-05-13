import collections
import time
import sys
from MazeCreate import create_maze as m


def DFS_algo():
    maze = m()
    maze_cords = []
    maze_walls = []
    num_wall = []
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
            else:
                maze_walls.append([i, j])

    for i, c in enumerate(maze_walls):
        num_wall.append(i)

    stack.append(start)

    for i, c in enumerate(notvisited):
        if stack in c:
            notvisited.pop(i)

DFS_algo()
