import numpy as np
from tqdm import tqdm

from day_11.prepare_data import prepare_data


def manhattan_distance(start, end):
    return abs(start[0] - end[0]) + abs(start[1] - end[1])


def main():
    # Read input data from a file
    position_pairs = prepare_data(use_dev_data=False, multiplier=1000000)

    path_length = []
    for p1, p2 in tqdm(position_pairs, desc='compute dist', total=len(position_pairs)):
        path = manhattan_distance(p1, p2)
        path_length.append(path)

    res = np.array(path_length).sum()
    print(res)
    # 857986849428


if __name__ == "__main__":
    print("Hello")
    main()
    print("Done")
