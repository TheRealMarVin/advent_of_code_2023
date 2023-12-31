import math
import sys

import numpy as np

from day_10.prepare_data import prepare_data


def main():
    # Read input data from a file
    input_data, start_pos = prepare_data(use_dev_data=False)

    symbol_direction_mapping = {
        "|": [(0, 1), (0, -1)],
        "-": [(1, 0), (-1, 0)],
        "L": [(0, -1), (1, 0)],
        "J": [(0, -1), (-1, 0)],
        "7": [(-1, 0), (0, 1)],
        "F": [(1, 0), (0, 1)],
        "S": [(0, 1), (0, -1), (1, 0), (-1, 0)]
    }

    connecting_symbols = {
        "|": ["L", "J", "7", "F", "|"],
        "-": ["L", "J", "7", "F", "-"],
        "L": ["|", "-", "7", "F", "J"],
        "J": ["|", "-", "7", "F", "L"],
        "7": ["|", "-", "L", "J", "F"],
        "F": ["|", "-", "L", "J", "7"],
        "S": ["|", "-", "L", "J", "7", "F"]
    }

    positions_to_explore = [(start_pos, 0, None)]
    distance_map = np.full((len(input_data), len(input_data[0])), sys.maxsize)

    while len(positions_to_explore) > 0:
        curr_pos, dist, last_direction = positions_to_explore[-1]
        line, col = curr_pos
        positions_to_explore = positions_to_explore[:-1]

        if dist >= distance_map[line][col]:
            continue

        distance_map[line][col] = dist
        curr_symbol = input_data[line][col]
        if curr_symbol == ".":
            continue

        directions = symbol_direction_mapping[curr_symbol]
        for d in directions:
            new_pos = (line + d[1], col + d[0]) # here I messed the description column and line, but laziness win!
            if new_pos[0] < 0 or new_pos[1] < 0:
                continue
            if new_pos[0] >= len(input_data) or new_pos[1] >= len(input_data[0]):
                continue
            next_symbol = input_data[new_pos[0]][new_pos[1]]
            if next_symbol in connecting_symbols[curr_symbol]:
                positions_to_explore.append((new_pos, dist+1, d))
                if dist == 0:
                    break  # This is a hack to get the solution faster

    distance_map[distance_map == sys.maxsize] = -1

    res = distance_map.max()

    print("res", math.ceil(res/2))


if __name__ == "__main__":
    print("Hello")
    main()
    print("Done")
