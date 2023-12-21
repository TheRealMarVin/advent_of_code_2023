import math
from collections import deque

import numpy as np

from day_20.prepare_data import prepare_data, Pulse


def main():
    # Read input data from a file
    modules_list, callers = prepare_data(use_dev_data=False)

    child_nodes = [callers[x] for x in callers['rx']][0]
    # here will not be a generic solution, but only one node send to rx
    # and this node is a conjunction. My plan is to find the loop for each child,
    # so they output a low pulse. Then will use lcm. If Ju had it first time
    # it must be the right path, but this solution is shit. I know!

    cycle_count = {}
    should_continue = True
    count = 0
    while should_continue:
        count += 1
        signal_queue = deque([('button', Pulse.LOW, None)])
        while signal_queue:
            module_name, signal, caller = signal_queue.popleft()

            if module_name is None:
                continue

            all_found = True
            for x in child_nodes:
                if x == caller and signal == Pulse.HIGH and x not in cycle_count:
                    cycle_count[x] = count
                all_found = all_found and (x in cycle_count)

            if all_found:
                should_continue = False
                break

            if module_name not in modules_list:
                continue

            out = modules_list[module_name](caller, signal)
            signal_queue.extend(out)

    res = math.lcm(*list(cycle_count.values()))
    print(res)


if __name__ == "__main__":
    print("Hello")
    main()
    print("Done")
