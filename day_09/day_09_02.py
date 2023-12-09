import numpy as np

from day_09.prepare_data import prepare_data


def reduce(numbers):
    if len(numbers) <= 2:
        raise Exception("oups")

    res = []
    line = numbers
    while line.count(0) != len(line):
        line = [line[i+1] - line[i] for i in range(len(line) - 1)]
        if len(line) == 0:
            line = [0]
        res.append(line)

    return res


def predict_next(reductions, numbers):
    previous_diff = 0
    for index in range(len(reductions) - 1, -1, -1):
        next_val = reductions[index][0] - previous_diff
        reductions[index].insert(0, next_val)
        previous_diff = next_val

    res = numbers[0] - previous_diff
    return res


def main():
    # Read input data from a file
    input_data = prepare_data(use_dev_data=False)

    res = []
    for line in input_data:
        diff_list = reduce(line)
        next_value = predict_next(diff_list, line)
        res.append(next_value)

    print(np.array(res).sum())


if __name__ == "__main__":
    print("Hello")
    main()
    print("Done")
