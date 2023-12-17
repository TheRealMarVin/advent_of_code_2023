import numpy as np


def prepare_data(use_dev_data=False):
    # Read input data from a file
    if use_dev_data:
        with open('data_dev.txt', 'r') as file:
            input_data = file.readlines()
    else:
        with open('data_challenge.txt', 'r') as file:
            input_data = file.readlines()

    input_data = np.array([string.rstrip('\n') for string in input_data])
    grid = {j + i * 1j: int(input_data[i][j]) for i in range(len(input_data)) for j in range(len(input_data[0]))}

    return input_data, grid


if __name__ == "__main__":
    print("Hello")
    prepare_data(True)
    print("Done")
