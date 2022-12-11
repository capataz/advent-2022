import operator
from collections import deque
import numpy as np

# F = './day_11/test.dat'
F = './day_11/puzzle.dat'

monkeys = {}

operator_map = {
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul,
    '/' : operator.truediv
}


def generate_op(op, val):
    if val.isdigit():
        def func(v):
            return operator_map[op](int(val), v)
    else:
        def func(v):
            return operator_map[op](v, v)
    return func


def main():
    current_monkey = 0
    lcm = 1
    for l in open(F):
        match l.strip().split():
            case 'Monkey', id:
                monkeys[(current_monkey := int(id[:-1]))] = {}
            case 'Starting', 'items:', *rest:
                monkeys[current_monkey]['items'] = deque([int(r.replace(',', '')) for r in rest])
            case 'Operation:', 'new', '=', 'old', op, val:
                monkeys[current_monkey]['op'] = generate_op(op, val)
            case 'Test:', 'divisible', 'by', val:
                monkeys[current_monkey]['div'] = int(val)
                lcm *= int(val)
            case 'If', 'true:', 'throw', 'to', 'monkey', target:
                monkeys[current_monkey]['true_target'] = int(target)
            case 'If', 'false:', 'throw', 'to', 'monkey', target:
                monkeys[current_monkey]['false_target'] = int(target)
            case _:
                pass

    inspection_counts = np.zeros(len(monkeys.keys()))

    for _ in range(10000):
        for i, mon in monkeys.items():
            while len(mon['items']) > 0:
                inspection_counts[i] += 1  # Count a monkey inspections

                item = int(mon['op'](int(mon['items'].popleft())))
                item = item % lcm    # Well, I had to look this trick up. I had congruence and modulo aritmatic, just failed the lcm

                target = mon['false_target'] if item % mon['div'] else mon['true_target']
                monkeys[target]['items'].append(item)

    return int(np.prod(sorted(inspection_counts)[-2:]))

if __name__ == '__main__':
    answer = main()
    print(answer)
    assert answer == 23641658401

# 23641658401