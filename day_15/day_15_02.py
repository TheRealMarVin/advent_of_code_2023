import numpy as np

from day_15.prepare_data import prepare_data


def create_hash(string):
    total = 0
    for c in string:
        total += ord(c)
        total = (17 * total) % 256
    return total


def apply_minus(boxes, data):
    label = data[:-1]
    box_index = create_hash(label)
    boxes[box_index] = [b for b in boxes[box_index] if label != b[0]]
    return boxes


def apply_equal(boxes, data):
    label, val = data.split('=')
    box_index = create_hash(label)
    found = False
    for index, b in enumerate(boxes[box_index]):
        if label == b[0]:
            boxes[box_index][index][1] = val
            found = True

    if not found:
        boxes[box_index].append([label, val])
    return boxes


def main():
    # Read input data from a file
    input_data = prepare_data(use_dev_data=False)

    res = {k: [] for k in range(256)}
    for data in input_data:
        if '-' in data:
            res = apply_minus(res, data)
        elif '=' in data:
            res = apply_equal(res, data)

    # compute focus power
    total = []
    for k, values in res.items():

        if len(values) > 0:
            print(k, values)
        for i, v in enumerate(values):
            focal = (k+1) * (i+1) * int(v[1])
            total.append(focal)

    print(np.array(total).sum())


if __name__ == "__main__":
    print("Hello")
    main()
    print("Done")
