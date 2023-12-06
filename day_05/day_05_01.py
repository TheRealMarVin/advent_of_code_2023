import re

import numpy as np


def extract_numbers(input_string):
    pattern = re.compile(r'\b\d+\b')
    numbers = [int(match) for match in pattern.findall(input_string)]
    return numbers


def get_in_value_in_map(value, maps):
    result = None
    for dest, start, length in maps:
        if value >= start and value < start + length:
            result = dest + (value - start)
            break

    if result is None:
        result = value

    return result


def main():
    # Read input data from a file
    with open('data.txt', 'r') as file:
        input_data = file.readlines()

    pattern = re.compile(r'^([a-zA-Z-]+).*$', re.MULTILINE)
    data = {}

    curr_keys = None
    for index, line in enumerate(input_data):
        if line == "":
            curr_keys = None
            continue

        matches = pattern.findall(line)
        if len(matches) > 0:
            curr_keys = matches[0]

        numbers = extract_numbers(line)
        if curr_keys not in data:
            data[curr_keys] = numbers
        elif len(numbers) > 0:
            data[curr_keys].append(numbers)
    a = 0

    locations = []
    for seed in data["seeds"]:
        soil = get_in_value_in_map(value=seed, maps=data["seed-to-soil"])
        fertilizer = get_in_value_in_map(value=soil, maps=data["soil-to-fertilizer"])
        water = get_in_value_in_map(value=fertilizer, maps=data["fertilizer-to-water"])
        light = get_in_value_in_map(value=water, maps=data["water-to-light"])
        temperature = get_in_value_in_map(value=light, maps=data["light-to-temperature"])
        humidity = get_in_value_in_map(value=temperature, maps=data["temperature-to-humidity"])
        location = get_in_value_in_map(value=humidity, maps=data["humidity-to-location"])
        locations.append(location)

    min_location = np.array(locations).min()
    print(min_location)


if __name__ == "__main__":
    print("Hello")
    main()
    print("Done")
