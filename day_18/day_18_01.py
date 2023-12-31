from collections import deque

import numpy as np

from day_18.prepare_data import prepare_data


def find_start_position(grid):
    rows, cols = grid.shape

    for row in range(rows-1):
        border_counts = 0
        for col in range(cols-1):
            if grid[row][col] == 1:
                border_counts += 1
            if grid[row][col] == 0 and border_counts == 1:
                return row, col

    # Return None if no suitable position is found
    return None


def fill_inside(grid, row, col):
    rows, cols = grid.shape
    queue = deque([(row, col)])

    while queue:
        row, col = queue.popleft()

        if 0 <= row < rows and 0 <= col < cols and grid[row][col] == 0:
            grid[row][col] = 1  # Change zero to one

            # Add neighbors to the queue
            queue.append((row - 1, col))
            queue.append((row + 1, col))
            queue.append((row, col - 1))
            queue.append((row, col + 1))


def main():
    # Read input data from a file
    input_data = prepare_data(use_dev_data=True)

    direction_map = {"U": np.array([-1, 0]), "D": np.array([1, 0]), "L": np.array([0, -1]), "R": np.array([0, 1])}
    points = [np.array([0, 0])]
    for d, m, _ in input_data:
        points.append((direction_map[d] * m) + points[-1])

    min_extend = np.min(points, axis=0)
    max_extend = np.max(points, axis=0)
    bounds = (max_extend - min_extend)+1

    grid = np.zeros(bounds)
    pos = -min_extend
    grid[pos[0]][pos[1]] = 1
    for d, m, _ in input_data:
        for i in range(m):
            pos = pos + direction_map[d]
            grid[pos[0]][pos[1]] = 1
    print(grid)

    start = find_start_position(grid)
    while start is not None:
        fill_inside(grid, *start)
        start = find_start_position(grid)

    print(grid)
    print(grid.sum())


if __name__ == "__main__":
    print("Hello")
    main()
    print("Done")
