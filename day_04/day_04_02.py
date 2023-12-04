import re

import numpy as np


def extract_numbers(input_string):
    pattern = re.compile(r'\b\d+\b')
    numbers = [int(match) for match in pattern.findall(input_string)]
    return numbers


def winning_and_have_pairs(data):
    if len(data) == 0:
        return

    _, numbers = data.split(":")
    winning_string, have_string = numbers.split("|")

    winning = extract_numbers(winning_string)
    have = extract_numbers(have_string)

    return set(winning), set(have)


def main():
    # Read input data from a file
    with open('data.txt', 'r') as file:
        input_data = file.readlines()

    res = np.ones((len(input_data)))
    for index, line in enumerate(input_data):
        winning, have = winning_and_have_pairs(line)

        intersection = winning & have
        curr_count = len(intersection)
        for i in range(curr_count):
            res[index+(i+1)] += res[index]

    total = np.array(res).sum()
    print(total)


if __name__ == "__main__":
    print("Hello")
    main()
    print("Done")
