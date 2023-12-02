import numpy as np


def extract_calibration_values(lines):
    values = []

    for line in lines:
        # Filter out non-numeric characters
        digits = ''.join(char for char in line if char.isdigit())

        # Check if we have at least two digits
        if len(digits) >= 1:
            # Combine the first and last digits
            value = int(digits[0] + digits[-1])
            values.append(value)

    return values


# Read calibration input from a file
with open('data.txt', 'r') as file:
    calibration_input = file.readlines()


calibration_values = extract_calibration_values(calibration_input)
print(calibration_values)
print(np.array(calibration_values).sum())
