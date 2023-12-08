import math
import re

import numpy as np


def get_sequence_and_map(input_data):
    sequence = list(input_data[0][:-1])

    world_map = {}
    starting_positions = []
    for line in input_data[2:]:
        pos, left, right = re.findall(r'[A-Za-z0-9]{3}', line)
        world_map[pos] = (left, right)
        if pos[-1] == "A":
            starting_positions.append(pos)

    return sequence, world_map, starting_positions


def main():
    # Read input data from a file
    with open('data.txt', 'r') as file:
        input_data = file.readlines()

    sequence, world_map, curr_positions = get_sequence_and_map(input_data)

    tmp = []
    for curr_pos in curr_positions:
        step_count = 0
        is_found = False
        while not is_found:
            for step in sequence:
                if curr_pos[-1] == "Z":
                    is_found = True
                    break

                step_count += 1
                direction = 0
                if step == "R":
                    direction = 1

                curr_pos = world_map[curr_pos][direction]

        tmp.append(step_count)
    res = math.lcm(*tmp)
    print(res)


if __name__ == "__main__":
    print("Hello")
    main()
    print("Done")
