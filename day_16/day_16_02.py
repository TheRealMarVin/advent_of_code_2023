import numpy as np

from day_16.prepare_data import prepare_data


def find_energy(input_data, starting_move):
    moves = [starting_move]
    seen = set()
    energized = set()
    while len(moves) > 0:
        curr_move = moves.pop()

        if curr_move in seen:
            continue

        pos, direction = curr_move
        if 0 > pos[0] or pos[0] >= input_data.shape[0] or 0 > pos[1] or pos[1] >= input_data.shape[1]:
            continue

        seen.add(curr_move)
        energized.add(pos)

        tile = input_data[pos[0]][pos[1]]
        if tile == '.':
            next_move = ((pos[0] + direction[0], pos[1] + direction[1]), direction)
            moves.append(next_move)

        elif tile == '|':
            if direction[1] != 0:
                next_move_up = ((pos[0] - 1, pos[1]), (-1, 0))
                next_move_down = ((pos[0] + 1, pos[1]), (1, 0))
                moves.append(next_move_up)
                moves.append(next_move_down)
            else:
                next_move = ((pos[0] + direction[0], pos[1] + direction[1]), direction)
                moves.append(next_move)
        elif tile == '-':
            if direction[0] != 0:
                next_move_left = ((pos[0], pos[1] - 1), (0, -1))
                next_move_right = ((pos[0], pos[1] + 1), (0, 1))
                moves.append(next_move_left)
                moves.append(next_move_right)
            else:
                next_move = ((pos[0] + direction[0], pos[1] + direction[1]), direction)
                moves.append(next_move)
            pass
        elif tile == '/':
            if direction[1] > 0:
                next_move = ((pos[0] - 1, pos[1]), (-1, 0))
            elif direction[1] < 0:
                next_move = ((pos[0] + 1, pos[1]), (1, 0))
            elif direction[0] > 0:
                next_move = ((pos[0], pos[1] - 1), (0, -1))
            elif direction[0] < 0:
                next_move = ((pos[0], pos[1] + 1), (0, 1))
            moves.append(next_move)
        elif tile == '\\':
            if direction[1] > 0:
                next_move = ((pos[0] + 1, pos[1]), (1, 0))
            elif direction[1] < 0:
                next_move = ((pos[0] - 1, pos[1]), (-1, 0))
            elif direction[0] > 0:
                next_move = ((pos[0], pos[1] + 1), (0, 1))
            elif direction[0] < 0:
                next_move = ((pos[0], pos[1] - 1), (0, -1))
            moves.append(next_move)

    return len(energized)


def main():
    # Read input data from a file
    input_data = prepare_data(use_dev_data=False)

    starting_moves = [((i, 0), (0, 1)) for i in range(input_data.shape[0])]
    starting_moves.extend([((i, input_data.shape[0] - 1), (0, -1)) for i in range(input_data.shape[0])])
    starting_moves.extend([((0, i), (1, 0)) for i in range(input_data.shape[1])])
    starting_moves.extend([((0, input_data.shape[1] - 1), (-1, 0)) for i in range(input_data.shape[1])])

    res = []
    for starting_move in starting_moves:
        e = find_energy(input_data, starting_move)
        res.append(e)

    total = np.array(res).max()
    print(total)


if __name__ == "__main__":
    print("Hello")
    main()
    print("Done")
