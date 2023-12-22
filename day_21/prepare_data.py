import numpy as np


def prepare_data(use_dev_data=False):
    # Read input data from a file
    if use_dev_data:
        with open('data_dev.txt', 'r') as file:
            input_data = file.readlines()
    else:
        with open('data_challenge.txt', 'r') as file:
            input_data = file.readlines()

    input_data = [list(string.rstrip('\n')) for string in input_data]

    start_pos = get_start_position(input_data)
    return input_data, start_pos


def get_start_position(input_data):
    start_pos = None

    for line_index, line in enumerate(input_data):
        for col_index, v in enumerate(line):
            if v == 'S':
                return (line_index, col_index)

    return start_pos


if __name__ == "__main__":
    print("Hello")
    prepare_data(True)
    print("Done")
