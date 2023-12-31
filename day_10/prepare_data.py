def prepare_data(use_dev_data=False):
    # Read input data from a file
    if use_dev_data:
        with open('data_dev.txt', 'r') as file:
            input_data = file.readlines()
    else:
        with open('data_challenge.txt', 'r') as file:
            input_data = file.readlines()

    input_data = [string.rstrip('\n') for string in input_data]
    start_pos = None
    for i, line in enumerate(input_data):
        for j, elem in enumerate(line):
            if elem == "S":
                start_pos = (i, j)
                break

    return input_data, start_pos


if __name__ == "__main__":
    print("Hello")
    prepare_data(True)
    print("Done")
