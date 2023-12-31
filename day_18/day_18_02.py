import numpy as np

from day_18.prepare_data import prepare_data


def shoelace_formula(vertices):
    vertices = np.array(vertices)
    vertices_count = len(vertices)
    area = np.int64(0)

    for i in range(vertices_count):
        area -= np.int64(vertices[i][0]) * np.int64(vertices[(i + 1) % vertices_count][1])
        area += np.int64(vertices[i][1]) * np.int64(vertices[(i + 1) % vertices_count][0])
    area //= 2

    return area


def main():
    # Read input data from a file
    input_data = prepare_data(use_dev_data=False)

    direction_map = {"U": np.array([-1, 0]), "D": np.array([1, 0]), "L": np.array([0, -1]), "R": np.array([0, 1])}

    # Here I assume the shape is clockwise and solution will not generalize.
    # I also assume even lines are left or right and odd are vertical
    points = [np.array([0, 0])]

    border_area = 0
    for _, _, c in input_data:
        d, m = c
        border_area += m
        new_pos = (direction_map[d] * m) + points[-1]

        # if not np.array_equal(new_pos, points[-1]):
        points.append(new_pos)

    if np.array_equal(points[0], points[-1]):
        points = points[1:]

    total = shoelace_formula(points) + (border_area//2) + 1
    print(total)


if __name__ == "__main__":
    print("Hello")
    main()
    print("Done")
