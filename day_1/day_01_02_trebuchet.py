def extract_calibration_values(lines):
    values = []

    # Replace spelled-out digits with numerical representation
    for line in lines:
        current_number = ""
        index = 0

        while index < len(line):
            if line[index].isdigit():
                current_number += line[index]
                index += 1
            else:
                for spelled_out, numerical in spelled_out_digits.items():
                    if line.startswith(spelled_out, index):
                        current_number += numerical
                        index += 1
                        break
                else:

                    index += 1

        digits = ''.join(char for char in current_number if char.isdigit())

        # Check if we have at least two digits
        if len(digits) >= 1:
            # Combine the first and last digits
            value = int(digits[0] + digits[-1])
            values.append(value)

    return values


# Read calibration input from a file
with open('data.txt', 'r') as file:
    calibration_input = file.readlines()


# Define spelled-out digits
spelled_out_digits = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

calibration_values = extract_calibration_values(calibration_input)
sum_calibration = sum(calibration_values)

print(calibration_values)
print(sum_calibration)

with open('data.txt', 'r') as file:
    calibration_input2 = file.readlines()

for i, x in enumerate(zip(calibration_values, calibration_input2)):
    print(i, x)
