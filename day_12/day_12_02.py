from functools import cache

import numpy as np

from day_12.prepare_data import prepare_data

@cache
def count_permutations(data, groups):
    if len(data) == 0:
        return 1 if len(groups) == 0 else 0
    if len(groups) == 0:
        return 1 if '#' not in data else 0
    count = 0

    if data[0] in ".?":
        count += count_permutations(data[1:], groups)

    first_group_size = groups[0]
    if first_group_size <= len(data) and data[0] in "#?":
        group_sequence = data[:first_group_size]

        if "." not in group_sequence and (first_group_size == len(data) or data[first_group_size] != "#"):
            count += count_permutations(data[first_group_size+1:], groups[1:])

    return count


def unfold(data, counts):
    new_data = ((data + '?') * 5)[:-1]
    new_counts = []
    for i in range(5):
        new_counts.extend(counts)
    return new_data, new_counts


def main():
    # Read input data from a file
    input_data = prepare_data(use_dev_data=False)

    res_counts = []
    for data, counts in input_data:
        new_data, new_counts = unfold(data, counts)
        curr_count = count_permutations(data=new_data, groups=tuple(new_counts))
        print(data, counts, curr_count)
        res_counts.append(curr_count)

    res = np.array(res_counts).sum()
    print(res)


if __name__ == "__main__":
    print("Hello")
    main()
    print("Done")
