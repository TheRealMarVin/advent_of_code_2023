import numpy as np

from day_19.prepare_data import prepare_data


def main():
    # Read input data from a file
    workflows, parts = prepare_data(use_dev_data=False)

    accepted_score = []
    for curr_parts in parts:
        conditions = workflows['in']
        continue_searching = True
        while continue_searching:
            for cond in conditions:
                if cond == 'A':
                    accepted_score.append(np.array(list(curr_parts.values())).sum())
                    continue_searching = False
                    break
                elif cond == 'R':
                    continue_searching = False
                    break
                elif cond in workflows:
                    conditions = workflows[cond]
                    break
                else:
                    rating, op, value, next_workflow = cond
                    if op == '>' and value < curr_parts[rating] or op == '<' and value > curr_parts[rating]:
                        if next_workflow == 'A':
                            accepted_score.append(np.array(list(curr_parts.values())).sum())
                            continue_searching = False
                        elif next_workflow == 'R':
                            continue_searching = False
                        else:
                            conditions = workflows[next_workflow]
                        break

    print(np.array(accepted_score).sum())


if __name__ == "__main__":
    print("Hello")
    main()
    print("Done")
