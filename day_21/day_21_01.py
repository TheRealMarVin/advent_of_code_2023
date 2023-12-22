import numpy as np

from day_21.prepare_data import prepare_data


def main():
    # Read input data from a file
    input_data, start_pos = prepare_data(use_dev_data=False)
    grid_shape = (len(input_data), len(input_data[0]))

    step_count = 64
    positions = set([start_pos])
    directions = [np.array([-1,0]), np.array([1,0]), np.array([0,-1]), np.array([0,1])]
    for i in range(step_count):
        new_positions = set()
        for p in positions:
            p = np.array(p)
            for d in directions:
                new_pos = p + d
                if 0 <= new_pos[0] < grid_shape[0] and 0 <= new_pos[1] < grid_shape[1]:
                    if input_data[new_pos[0]][new_pos[1]] in '.S':
                        new_positions.add((new_pos[0], new_pos[1]))
        positions = new_positions

    # for r, c in positions:
    #     input_data[r][c] = 'O'
    # print(np.array(input_data))
    print('result: ', len(positions))


if __name__ == "__main__":
    print("Hello")
    main()
    print("Done")
