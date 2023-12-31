def prepare_data(use_dev_data=False):
    # Read input data from a file
    if use_dev_data:
        with open('data_dev.txt', 'r') as file:
            input_data = file.readlines()
    else:
        with open('data_challenge.txt', 'r') as file:
            input_data = file.readlines()

    prepared_data = []
    for line in input_data:
        d, m, c = line.rstrip('\n').split()
        new_m = int(c[2:-2], 16)
        new_d = "U"
        if c[-2] == "0":
            new_d = "R"
        if c[-2] == "1":
            new_d = "D"
        if c[-2] == "2":
            new_d = "L"

        prepared_data.append((d, int(m), (new_d, new_m)))

    return prepared_data


if __name__ == "__main__":
    print("Hello")
    prepare_data(True)
    print("Done")
