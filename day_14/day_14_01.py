import numpy as np

from day_14.prepare_data import prepare_data


def main():
    # Read input data from a file
    input_data = prepare_data(use_dev_data=False)


    res = []
    for grid in input_data:
        counts = {k: 0 for k in range(grid.shape[0])}
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
                    counts[curr] += 1

        count = 0
        for k, v in counts.items():
            count += v * (grid.shape[0] - k)
        res.append(count)
    total = np.array(res).sum()
    print(total)






if __name__ == "__main__":
    print("Hello")
    main()
    print("Done")
