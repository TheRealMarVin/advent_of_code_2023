from functools import cache

import numpy as np

from day_14.prepare_data import prepare_data


@cache
def tilt_grid(hashable_tuple):
    grid = np.array(hashable_tuple)

    for row_index in range(grid.shape[0]):
        row = grid[row_index]
        for col_index, item in enumerate(row):
            if item == "O":
                curr = row_index
                north = curr - 1
                while north >= 0 and grid[north][col_index] == ".":
                    grid[north][col_index] = "O"
                    grid[curr][col_index] = "."
                    curr = north
                    north -= 1

    out_grid = to_hashable(grid)
    return out_grid


def count_weights(grid):
    counts = {k: 0 for k in range(grid.shape[0])}
    for row_index in range(grid.shape[0]):
        row = grid[row_index]
        for col_index, item in enumerate(row):
            if item == "O":
                counts[row_index] += 1

    count = 0
    for k, v in counts.items():
        count += v * (grid.shape[0] - k)

    return count


def to_hashable(grid):
    res = []
    for row in grid:
        as_tuple = tuple(list(row))
        res.append(as_tuple)
    return tuple(res)


def cycle(grid):
    flattened_tuple = to_hashable(grid)
    new_grid = tilt_grid(flattened_tuple)
    grid = np.array(new_grid)

    grid = np.rot90(grid, k=-1)
    flattened_tuple = to_hashable(grid)
    new_grid = tilt_grid(flattened_tuple)
    grid = np.array(new_grid)

    grid = np.rot90(grid, k=-1)
    flattened_tuple = to_hashable(grid)
    new_grid = tilt_grid(flattened_tuple)
    grid = np.array(new_grid)

    grid = np.rot90(grid, k=-1)
    flattened_tuple = to_hashable(grid)
    new_grid = tilt_grid(flattened_tuple)
    grid = np.array(new_grid)

    grid = np.rot90(grid, k=-1)
    flattened_tuple = to_hashable(grid)

    return flattened_tuple


def main():
    # Read input data from a file
    input_data = prepare_data(use_dev_data=False)

    res = []
    for grid in input_data:
        cycle_count = 0

        flattened_tuple = to_hashable(grid)
        seen = {flattened_tuple}
        cached_output = []
        while True:
            cycle_count += 1
            flattened_tuple = cycle(flattened_tuple)
            if flattened_tuple in seen:
                break
            else:
                seen.add(flattened_tuple)
                cached_output.append(flattened_tuple)

        curr_index = cached_output.index(flattened_tuple) + 1
        cached_index = (1000000000 - curr_index) % (cycle_count - curr_index) + curr_index

        grid = np.array(cached_output[cached_index-1])
        res.append(count_weights(grid))

    total = np.array(res).sum()
    print(total)


if __name__ == "__main__":
    print("Hello")
    main()
    print("Done")
