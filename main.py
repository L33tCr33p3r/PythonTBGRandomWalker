# This is a sample Python script.
import random


def generate_map(size, steps):
    grid = []
    for i in range(size):
        grid.append([])
        for j in range(size):
            grid[i].append(0)
    middle = size // 2
    grid[middle][middle] = 1

    walker_x = middle
    walker_y = middle
    for k in range(steps):
        direction = random.randrange(4)
        if direction == 0:
            walker_y -= 1
        elif direction == 1:
            walker_x += 1
        elif direction == 2:
            walker_y += 1
        elif direction == 3:
            walker_x -= 1
        if walker_x < 0:
            walker_x = 0
        if walker_y < 0:
            walker_y = 0
        if walker_x >= size:
            walker_x = size - 1
        if walker_y >= size:
            walker_y = size - 1
        if grid[walker_x][walker_y] == 0:
            grid[walker_x][walker_y] = random.randrange(2, 10)
    return grid


def prettyprint(gird):
    for i in range(len(gird)):
        print(gird[i])


if __name__ == '__main__':
    game_map = generate_map(11, 1000)
    prettyprint(game_map)
