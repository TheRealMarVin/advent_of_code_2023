def prepare_data(use_dev_data=False):
    # Read input data from a file
    if use_dev_data:
        with open('data_dev.txt', 'r') as file:
            input_data = file.readlines()
    else:
        with open('data_challenge.txt', 'r') as file:
            input_data = file.readlines()

    prepared_data = []
    for string in input_data:
        prepared_data.extend(string.split(','))

    return prepared_data


if __name__ == "__main__":
    print("Hello")
    prepare_data(True)
    print("Done")
