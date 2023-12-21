from enum import Enum


class Pulse(Enum):
    HIGH = 1,
    LOW = 2

class Button:
    def __init__(self, modules_to_call):
        self.modules_to_call = modules_to_call

    def __call__(self, caller, signal):
        return [(self.modules_to_call, Pulse.LOW, "button")]


class Broadcaster:
    def __init__(self, modules_to_call, module_name):
        self.modules_to_call = modules_to_call
        self.module_name = module_name

    def __call__(self, caller, signal):
        res = [(x, signal, self.module_name) for x in self.modules_to_call]
        return res


class FlipFlop:
    def __init__(self, modules_to_call, module_name):
        self.modules_to_call = modules_to_call
        self.state = 0
        self.module_name = module_name

    def __call__(self, caller, signal):
        if signal == Pulse.HIGH:
            return [(None, signal, self.module_name)]

        if self.state == 0:
            res = [(x, Pulse.HIGH, self.module_name) for x in self.modules_to_call]
        else:
            res = [(x, Pulse.LOW, self.module_name) for x in self.modules_to_call]

        self.state = 0 if self.state == 1 else 1

        return res


class Conjunction:
    def __init__(self, modules_to_call, module_name):
        self.modules_to_call = modules_to_call
        self.state = {}
        self.module_name = module_name

    def __call__(self, caller, signal):
        self.state[caller] = signal
        if list(self.state.values()).count(Pulse.HIGH) == len(self.state):
            res = [(x, Pulse.LOW, self.module_name) for x in self.modules_to_call]
        else:
            res = [(x, Pulse.HIGH, self.module_name) for x in self.modules_to_call]

        return res


def prepare_data(use_dev_data=False):
    # Read input data from a file
    if use_dev_data:
        with open('data_dev.txt', 'r') as file:
            input_data = file.readlines()
    else:
        with open('data_challenge.txt', 'r') as file:
            input_data = file.readlines()

    input_data = [string.rstrip('\n') for string in input_data]

    callers = {}
    modules_list = {'button': Button('broadcaster')}
    for line in input_data:
        name, values = line.split("->")
        values = [a.strip() for a in values.split(',')]
        if name.startswith('broadcaster'):
            name = 'broadcaster'
            modules_list[name] = Broadcaster(values, name)
        elif name.startswith('%'):
            name = name[1:].strip()
            modules_list[name] = FlipFlop(values, name)
        elif name.startswith('&'):
            name = name[1:].strip()
            modules_list[name] = Conjunction(values, name)

        for v in values:
            if v not in callers:
                callers[v] = []
            callers[v].append(name)

    for k, module in modules_list.items():
        if isinstance(module, Conjunction):
            module.state = {x: Pulse.LOW for x in callers[module.module_name]}

    return modules_list, callers


if __name__ == "__main__":
    print("Hello")
    prepare_data(True)
    print("Done")
