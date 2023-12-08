import re

import numpy as np


def main():
    # Read input data from a file
    with open('data.txt', 'r') as file:
        input_data = file.readlines()

    sequence = list(input_data[0][:-1])

    world_map = {}
    for line in input_data[2:]:
        pos, left, right = re.findall(r'[A-Za-z]{3}', line)
        world_map[pos] = (left, right)

    curr_pos = "AAA"
    step_count = 0
    is_found = False
    while not is_found:
        for step in sequence:
            if curr_pos == "ZZZ":
                is_found = True
                break

            step_count += 1
            direction = 0
            if step == "R":
                direction = 1

            curr_pos = world_map[curr_pos][direction]

    print(step_count)


if __name__ == "__main__":
    print("Hello")
    main()
    print("Done")

