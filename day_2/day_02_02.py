import numpy as np

import re


def extract_game_information(input_string):
    # Split content
    game_info, sequences_string = input_string.split(":")

    # get game number
    game_index = int(game_info[5:])

    sequences = sequences_string.split(";")

    sequences_res = []
    for sequence in sequences:
        seq_dict = {}

        pairs = sequence.split(",")
        for pair in pairs:
            sequence = pair.strip()
            count, color = sequence.split(" ")
            if color not in seq_dict:
                seq_dict[color] = int(count)
            else:
                seq_dict[color] += int(count)

        sequences_res.append(seq_dict)

    return game_index, sequences_res


def get_minimum_set(game_counts):
    minimum_set = {}
    for game in game_counts:
        for k, v in game.items():
            if k not in minimum_set:
                minimum_set[k] = v
            else:
                minimum_set[k] = max(minimum_set[k], v)

    return minimum_set


def get_power_set(counts):
    power = 1
    for _, v in counts.items():
        power *= v

    return power


def main():
    # Read input data from a file
    with open('data.txt', 'r') as file:
        input_data = file.readlines()

    max_counts = {"red": 12, "green": 13, "blue": 14}

    res = 0
    for curr_line in input_data:
        game_id, game_counts = extract_game_information(curr_line)
        #print(game_id, game_counts)

        minimum_set = get_minimum_set(game_counts)
        power = get_power_set(minimum_set)
        res += power
        print(minimum_set, power, res)


    print(res)


if __name__ == "__main__":
    print("Hello")
    main()
    print("Done")
