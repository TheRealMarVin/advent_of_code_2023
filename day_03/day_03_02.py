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

    pairs = {(int(match.group()), match.start()) for match in matches}
    result = {}
    for val, pos in pairs:
        for i in range(len(str(val))):
            result[pos+i] = val

    return result


def extract_special_characters(line):
    pattern = re.compile(r'(\*)')
    matches = pattern.finditer(line)

    result_dict = {match.start(): match.group() for match in matches if match.group() != "."}
    return result_dict


def main():
    # Read input data from a file
    with open('data.txt', 'r') as file:
        input_data = file.readlines()

    special_characters = {}
    numbers_map = {}
    for index, curr_data in enumerate(input_data):
        specials = extract_special_characters(curr_data[:-1])
        if len(specials) > 0:
            special_characters[index] = specials

        numbers = extract_integer_numbers(curr_data)
        if len(numbers) > 0:
            numbers_map[index] = numbers

    gears = []
    offsets = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

    for line, sv1 in special_characters.items():
        for col in sv1.keys():
            touch = []

            for x, y in offsets:
                if line + x in numbers_map and col+y in numbers_map[line+x]:
                    touch.append(numbers_map[line+x][col+y])

            touch = list(set(touch))
            if len(touch) == 2:
                gears.append(np.array(touch).prod())

    count = np.array(gears).sum()
    print(count)


if __name__ == "__main__":
    print("Hello")
    main()
    print("Done")
