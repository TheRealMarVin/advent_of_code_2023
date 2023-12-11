from collections import deque

import numpy as np
from tqdm import tqdm

from day_11.prepare_data import prepare_data


def manhattan_distance(start, end):
    return abs(start[0] - end[0]) + abs(start[1] - end[1])


def main():
    # Read input data from a file
    input_data = prepare_data(use_dev_data=False)

    indices = np.where(input_data == '#')
    positions = [p for p in zip(indices[0], indices[1])]

    position_pairs = []
    for index, p in tqdm(enumerate(positions[:-1])):
        for p2 in positions[index+1:]:
            position_pairs.append((p, p2))

    path_length = []
    for p1, p2 in tqdm(position_pairs):
        path = manhattan_distance(p1, p2)
        path_length.append(path)

    res = np.array(path_length).sum()
    print(res)
    a = 0


if __name__ == "__main__":
    print("Hello")
    main()
    print("Done")
