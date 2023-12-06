import copy
import re

import numpy as np


def extract_numbers(input_string):
    pattern = re.compile(r'\b\d+\b')
    numbers = [int(match) for match in pattern.findall(input_string)]
    return numbers


def find_common_range(tuple1, tuple2):
    start1, length1 = tuple1
    end1 = start1 + length1

    start2, length2 = tuple2
    end2 = start2 + length2

    # Calculate the intersection
    common_start = max(start1, start2)
    common_end = min(end1, end2)

    non_matching_ranges = []
    matching_range = None
    if end1 <= start2 or end2 <= start1:
        return non_matching_ranges, matching_range

    if common_start > start1:
        non_matching_ranges.append((start1, common_start-start1))
    if common_start < common_end:
        common_length = common_end - common_start
        matching_range = (common_start, common_length)
    if common_end < end1 and end1 > common_end:
        non_matching_ranges.append((common_end, end1 - common_end))

    return non_matching_ranges, matching_range


def get_values_in_map(value, maps):
    result = []

    values = [value]
    for dest, start, length in maps:
        has_matched = False
        for v in values:
            non_matching, matching_range = find_common_range(v, (start, length))
            if matching_range is not None:
                has_matched = True
                values = values[:-1]
                values.extend(non_matching)
                temp_res = (dest + (matching_range[0] - start), matching_range[1])
                print("matching:", matching_range, " to:", temp_res)
                result.append(temp_res)

        if not has_matched:
            result.extend(non_matching)
    if len(value) > 0:
        result.extend(values)

    if len(result) == 0:
        result.append(value)

    return result

def loop_data(input_data, data, key):
    res = []
    for curr in input_data:
        res.extend(get_values_in_map(value=curr, maps=data[key]))
    return res


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
    data["seeds"] = np.array(data["seeds"]).reshape((-1, 2))

    print("seed-to-soil")
    soil = loop_data(data["seeds"], data, "seed-to-soil")
    print("soil-to-fertilizer")
    fertilizer = loop_data(soil, data, "soil-to-fertilizer")
    print("fertilizer-to-water")
    water = loop_data(fertilizer, data, "fertilizer-to-water")
    print("water-to-light")
    light = loop_data(water, data, "water-to-light")
    print("light-to-temperature")
    temperature = loop_data(light, data, "light-to-temperature")
    print("temperature-to-humidity")
    humidity = loop_data(temperature, data, "temperature-to-humidity")
    print("humidity-to-location")
    location = loop_data(humidity, data, "humidity-to-location")
    locations = [loc for loc, _ in location]

    min_location = np.array(locations).min()
    print(min_location)


if __name__ == "__main__":
    print("Hello")
    main()
    print("Done")
