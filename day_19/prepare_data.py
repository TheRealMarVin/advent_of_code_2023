import re


def prepare_data(use_dev_data=False):
    # Read input data from a file
    if use_dev_data:
        with open('data_dev.txt', 'r') as file:
            input_data = file.readlines()
    else:
        with open('data_challenge.txt', 'r') as file:
            input_data = file.readlines()

    input_data = [string.rstrip('\n') for string in input_data]

    blank_index = input_data.index("")
    workflows = prepare_workflow(input_data[:blank_index])
    parts = prepare_parts(input_data[blank_index + 1:])

    return workflows, parts


def prepare_parts(data):
    parts = []
    for string in data:
        raw_parts = string[1:-1].split(',')
        curr_part = {}
        for part in raw_parts:
            part_rating,value = part.split("=")
            curr_part[part_rating] = int(value)

        parts.append(curr_part)
    return parts


def prepare_workflow(data):
    pattern = re.compile(r'(\w+)\{(.*.*)\}')
    operators = ['<', '>', '=']

    workflows = {}
    for string in data:
        match = pattern.search(string)
        if match:
            identifier = match.group(1)
            conditions = match.group(2).split(",")

            for index, condition in enumerate(conditions):
                for op in operators:
                    if op in condition:
                        part_rating, rest = condition.split(op)
                        value, next_condition = rest.split(':')
                        conditions[index] = (part_rating, op, int(value), next_condition)

            workflows[identifier] = conditions

    return workflows


if __name__ == "__main__":
    print("Hello")
    prepare_data(True)
    print("Done")
