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


def check_if_valid(game_counts, max_counts):
    for game in game_counts:
        for k,v in game.items():
            if max_counts[k] < v:
                return False
    return True


def main():
    # Read input data from a file
    with open('data.txt', 'r') as file:
        input_data = file.readlines()

    max_counts = {"red": 12, "green": 13, "blue": 14}

    res = 0
    for curr_line in input_data:
        game_id, game_counts = extract_game_information(curr_line)
        #print(game_id, game_counts)

        is_valid = check_if_valid(game_counts, max_counts)
        if is_valid:
            res += game_id

    print(res)



if __name__ == "__main__":
    print("Hello")
    main()
    print("Done")
