#!/usr/bin/python3
""" island perimeter module """


def island_perimeter(grid):
    """ returns the periemter of an island """
    rows = len(grid)
    cols = len(grid[0])
    p = 0
    connections = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                p += 4

                # Check top
                if i != 0 and grid[i - 1][j] == 1:
                    connections += 1

                # Check left
                if j != 0 and grid[i][j - 1] == 1:
                    connections += 1

    return p - connections * 2
