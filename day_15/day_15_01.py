import numpy as np

from day_15.prepare_data import prepare_data


def create_hash(string):
    total = 0
    for c in string:
        total += ord(c)
        total = (17 * total) % 256
    return total


def main():
    # Read input data from a file
    input_data = prepare_data(use_dev_data=False)

    res = []
    for data in input_data:
        val = create_hash(data)
        res.append(val)

    total = np.array(res).sum()
    print(total)


if __name__ == "__main__":
    print("Hello")
    main()
    print("Done")
