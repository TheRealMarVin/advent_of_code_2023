from collections import deque

import numpy as np

from day_20.prepare_data import prepare_data, Pulse


def main():
    # Read input data from a file
    modules_list, _ = prepare_data(use_dev_data=False)

    total_low_signal_count = 0
    total_high_signal_count = 0

    loop_count = 1000
    for i in range(loop_count):
        print("#######################################################")
        low_signal_count = 0
        high_signal_count = 0
        signal_queue = deque([('button', Pulse.LOW, None)])
        while signal_queue:
            module_name, signal, caller = signal_queue.popleft()
            if module_name is None:
                continue

            # print(caller, signal, module_name)

            if caller is not None:
                if signal == Pulse.LOW:
                    low_signal_count += 1
                elif signal == Pulse.HIGH:
                    high_signal_count += 1
            # print(low_signal_count, high_signal_count)

            if module_name not in modules_list:
                continue

            # if caller is not None:
                # if signal == Pulse.LOW:
                #     low_signal_count += 1
                # elif signal == Pulse.HIGH:
                #     high_signal_count += 1

            out = modules_list[module_name](caller, signal)
            signal_queue.extend(out)

        total_low_signal_count += low_signal_count
        total_high_signal_count += high_signal_count

    print('Low:',total_low_signal_count, '\tHigh:', total_high_signal_count)
    print(total_low_signal_count * total_high_signal_count)
    a = 0


if __name__ == "__main__":
    print("Hello")
    main()
    print("Done")
