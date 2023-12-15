import numpy as np


def prepare_data(use_dev_data=False):
    # Read input data from a file
    if use_dev_data:
        with open('data_dev.txt', 'r') as file:
            input_data = file.readlines()
    else:
        with open('data_challenge.txt', 'r') as file:
            input_data = file.readlines()

    input_data = [string.rstrip('\n') for string in input_data]

    grids = []
    curr_grid = []
    for line in input_data:
        if len(line) == 0:
            grids.append(np.array(curr_grid))
            curr_grid = []
        else:
            curr_grid.append(np.array(list(line)))

    if len(curr_grid) > 0:
        grids.append(np.array(curr_grid))

    return grids


if __name__ == "__main__":
    print("Hello")
    prepare_data(True)
    print("Done")
