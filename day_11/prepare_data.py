import numpy as np
from tqdm import tqdm


def find_rows_columns_with_same_value(data, value):
    rows_with_value = np.all(data == value, axis=1)
    columns_with_value = np.all(data == value, axis=0)

    return np.where(rows_with_value)[0], np.where(columns_with_value)[0]


def prepare_data(use_dev_data=False, multiplier=1):
    # Read input data from a file
    if use_dev_data:
        with open('data_dev.txt', 'r') as file:
            input_data = file.readlines()
    else:
        with open('data_challenge.txt', 'r') as file:
            input_data = file.readlines()

    input_data = np.array([np.array(list(string.rstrip('\n'))) for string in input_data])
    empty_rows, empty_cols = find_rows_columns_with_same_value(input_data, '.')

    for index_to_insert in tqdm(reversed(empty_rows)):
        new_row = np.full((multiplier, input_data.shape[1]), '.')
        input_data = np.insert(input_data, index_to_insert, new_row, axis=0)

    for index_to_insert in tqdm(reversed(empty_cols)):
        # Add a column filled with the specified value at the specified index
        new_column = np.full((input_data.shape[0]), '.')
        input_data = np.insert(input_data, index_to_insert, new_column, axis=1)

    return input_data


if __name__ == "__main__":
    print("Hello")
    prepare_data(True)
    print("Done")
