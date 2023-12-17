import numpy as np
from heapq import heappop, heappush
from day_17.prepare_data import prepare_data


def main():
    # Read input data from a file
    input_data, grid = prepare_data(use_dev_data=False)

    target_position = (len(input_data[0]) - 1) + (len(input_data) - 1) * 1j

    # State: (heat, unique_id, current_position, direction_moved, blocks_moved)
    initial_positions = [1, 1j]
    initial_states = [(grid[position], id(position), position, position, 1) for position in initial_positions]

    priority_queue = initial_states
    visited_states = set()

    while priority_queue:
        current_heat, _, current_position, current_direction, blocks_moved = heappop(priority_queue)

        if (current_position, current_direction, blocks_moved) in visited_states:
            continue

        visited_states.add((current_position, current_direction, blocks_moved))

        if current_position == target_position:
            print("result:", current_heat)
            break

        possible_directions = [current_direction * 1j, -current_direction * 1j]

        # Turn
        for new_direction in possible_directions:
            new_position = current_position + new_direction
            if new_position in grid:
                heappush(priority_queue,
                         (current_heat + grid[new_position], id(new_position), new_position, new_direction, 1))

        # If moved less than 3 blocks, continue in the same direction
        if blocks_moved < 3:
            new_position = current_position + current_direction
            if new_position in grid:
                heappush(priority_queue, (
                current_heat + grid[new_position], id(new_position), new_position, current_direction, blocks_moved + 1))

import numpy as np
from heapq import heappop, heappush
from day_17.prepare_data import prepare_data

def main():
    # Read input data from a file
    input_data, grid = prepare_data(use_dev_data=False)

    target_position = (len(input_data[0]) - 1) + (len(input_data) - 1) * 1j

    # State: (heat, unique_id, current_position, direction_moved, blocks_moved)
    initial_positions = [1, 1j]
    initial_states = [(grid[position], id(position), position, position, 1) for position in initial_positions]

    priority_queue = initial_states
    visited_states = set()

    while priority_queue:
        current_heat, _, current_position, current_direction, blocks_moved = heappop(priority_queue)

        if (current_position, current_direction, blocks_moved) in visited_states:
            continue

        visited_states.add((current_position, current_direction, blocks_moved))

        if current_position == target_position and blocks_moved >= 4:
            print("result:", current_heat)
            break

        # If moved less than 10 blocks, continue in the same direction
        if blocks_moved < 10:
            new_position = current_position + current_direction
            if new_position in grid:
                heappush(priority_queue, (
                    current_heat + grid[new_position], id(new_position), new_position, current_direction,
                    blocks_moved + 1))

        # If moved at least 4 blocks, we can turn.
        if blocks_moved >= 4:
            possible_directions = [current_direction * 1j, -current_direction * 1j]
            for new_direction in possible_directions:
                new_position = current_position + new_direction
                if new_position in grid:
                    heappush(priority_queue,
                             (current_heat + grid[new_position], id(new_position), new_position, new_direction, 1))


if __name__ == "__main__":
    print("Hello")
    main()
    print("Done")
