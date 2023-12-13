def extract_numbers(input_string):
    numbers = [int(number) for number in input_string.split(',')]
    return numbers


def prepare_data(use_dev_data=False):
    # Read input data from a file
    if use_dev_data:
        with open('data_dev.txt', 'r') as file:
            input_data = file.readlines()
    else:
        with open('data_challenge.txt', 'r') as file:
            input_data = file.readlines()

    input_data = [string.rstrip('\n') for string in input_data]

    prepared_data = []
    for row in input_data:
        symbols, numbers_string = row.split()
        numbers = extract_numbers(numbers_string)
        prepared_data.append((symbols, numbers))

    return prepared_data


if __name__ == "__main__":
    print("Hello")
    prepare_data(True)
    print("Done")

