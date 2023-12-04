import re

import numpy as np


def process_line(line, line_index, special_characters):
    offsets = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

    parts = []

    numbers = extract_integer_numbers(line)
    for number, position in numbers:
        found = False
        for i in range(len(str(number))):
            for x, y in offsets:
                if (line_index + x) in special_characters and position+i+y in special_characters[line_index + x]:
                    found = True
                    break
            if found:
                break
        if found:
            parts.append(number)

    return parts



def extract_integer_numbers(line):
    pattern = re.compile(r'\b(\d+)\b')
    matches = pattern.finditer(line)

    result = [(int(match.group()), match.start()) for match in matches]

    return result


def extract_special_characters(line):
    pattern = re.compile(r'(\W)')
    matches = pattern.finditer(line)

    result_dict = {match.start(): match.group() for match in matches if match.group() != "."}
    return result_dict


def main():
    # Read input data from a file
    with open('data.txt', 'r') as file:
        input_data = file.readlines()

    special_characters = {}
    for index, curr_data in enumerate(input_data):
        special_characters[index] = extract_special_characters(curr_data[:-1])

    # data_as_grid = [list(list_item) for list_item in input_data]

    parts = []
    for line_index, curr_line in enumerate(input_data):
        result = process_line(curr_line, line_index, special_characters)
        parts.extend(result)

    count = np.array(parts).sum()
    print(count)


if __name__ == "__main__":
    print("Hello")
    main()
    print("Done")
