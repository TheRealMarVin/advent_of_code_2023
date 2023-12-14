import numpy as np

from day_13.prepare_data import prepare_data


def find_equal_columns(grid):
    for row in range(len(grid)):
        rows_above = grid[row - 1::-1]
        rows_below = grid[row:]

        column_pairs = zip(rows_above, rows_below)
        unequal_pairs_count = sum(c != d for pair in column_pairs for c, d in zip(*pair))
        if unequal_pairs_count == 0:
            return row
    else:
        return 0


def main():
    # Read input data from a file
    input_data = prepare_data(use_dev_data=False)

    res = 0
    for index, grid in enumerate(input_data):

        rows = find_equal_columns(grid)
        columns = find_equal_columns(grid.T)

        # print(columns_pairs, roes)
        if (columns) > (rows):
            res += (columns)
        else:
            res += (rows) * 100

        print(index+1, '-', (rows), (columns), res)

    print(res)


if __name__ == "__main__":
    print("Hello")
    main()
    print("Done")
