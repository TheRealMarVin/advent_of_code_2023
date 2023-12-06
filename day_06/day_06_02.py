import re

import numpy as np


def extract_numbers(input_string):
    pattern = re.compile(r'\b\d+\b')
    number = ""
    for match in pattern.findall(input_string):
        number += match

    return [int(number)]


def main():
    # Read input data from a file
    with open('data.txt', 'r') as file:
        input_data = file.readlines()

    times = extract_numbers(input_data[0])
    distances = extract_numbers(input_data[1])

    initial_speed = 0
    hold_acceleration = 1

    res = []
    for distance, time in zip(distances, times):
        count = 0
        for t in range(time):
            d = (initial_speed * t) + (t * hold_acceleration * (time - t))
            if d > distance:
                count += 1
        res.append(count)

    res = np.array(res).prod()
    print(res)


if __name__ == "__main__":
    print("Hello")
    main()
    print("Done")
