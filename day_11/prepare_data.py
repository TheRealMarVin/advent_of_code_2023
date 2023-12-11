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

    indices = np.where(input_data == '#')
    positions = [p for p in zip(indices[0], indices[1])]

    shifted_positions = []
    for row_pos, col_pos in positions:
        row_offset = 0
        col_offset = 0
        for row in empty_rows:
            if row_pos > row:
                row_offset += (multiplier - 1)
        for col in empty_cols:
            if col_pos > col:
                col_offset += (multiplier - 1)
        new_pos = (row_pos + row_offset, col_pos + col_offset)
        shifted_positions.append(new_pos)

    position_pairs = []
    for index, p in tqdm(enumerate(positions[:-1])):
        for p2 in positions[index + 1:]:
            position_pairs.append((p, p2))

    updated_pairs = []
    for index, p in tqdm(enumerate(shifted_positions[:-1])):
        for p2 in shifted_positions[index + 1:]:
            updated_pairs.append((p, p2))

    # for index_to_insert in tqdm(reversed(empty_rows)):
    #     new_row = np.full((multiplier, input_data.shape[1]), '.')
    #     input_data = np.insert(input_data, index_to_insert, new_row, axis=0)
    #
    # for index_to_insert in tqdm(reversed(empty_cols)):
    #     # Add a column filled with the specified value at the specified index
    #     new_column = np.full((input_data.shape[0]), '.')
    #     input_data = np.insert(input_data, index_to_insert, new_column, axis=1)

    return updated_pairs


if __name__ == "__main__":
    print("Hello")
    prepare_data(True)
    print("Done")
