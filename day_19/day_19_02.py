import copy
from collections import deque

import numpy as np

from day_19.prepare_data import prepare_data


def update_range(part, condition):
    res = copy.deepcopy(part)
    rating, op, value, next_workflow = condition

    low, high = part[rating]
    if op == '<':
        res[rating] = (low, min(high, value-1))
        part[rating] = (max(low, value), high)
    elif op == '>':
        res[rating] = (max(low, value+1), high)
        part[rating] = (low, min(high, value))

    return part, res


def main():
    # Read input data from a file
    workflows, _ = prepare_data(use_dev_data=False)

    accepted_score = []
    parts = deque([('in', {'x': (1, 4000), 'm': (1, 4000), 'a': (1, 4000), 's': (1, 4000)})])
    while parts:
        workflow, part = parts.pop()
        if workflow == 'A':
            curr_total = 1
            for low, high in part.values():
                curr_total *= (high - low) + 1
            accepted_score.append(curr_total)
            continue

        conditions = workflows[workflow]
        for cond in conditions:
            if cond == 'A':
                parts.append((cond, part))
                break
            elif cond == 'R':
                break
            elif cond in workflows:
                parts.append((cond, part))
                break
            else:
                _, _, _, next_workflow = cond
                part, new_part = update_range(part, cond)

                if next_workflow != 'R':
                    parts.append((next_workflow, new_part))

    print(accepted_score)
    print(np.array(accepted_score).sum())


if __name__ == "__main__":
    print("Hello")
    main()
    print("Done")
