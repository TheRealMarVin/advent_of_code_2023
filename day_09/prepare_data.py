import re


def extract_numbers(input_string):
    numbers = [int(number) for number in input_string.split()]
    return numbers


def prepare_data(use_dev_data=False):
    # Read input data from a file
    if use_dev_data:
        with open('data_dev.txt', 'r') as file:
            input_data = file.readlines()
    else:
        with open('data_challenge.txt', 'r') as file:
            input_data = file.readlines()

    input_data = [extract_numbers(string) for string in input_data]

    return input_data
