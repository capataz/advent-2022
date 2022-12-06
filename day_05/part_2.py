# F = './day_05/test.dat'
F = './day_05/puzzle.dat'

def parse_input():
    in_stack = True
    raw_stacks = []
    instructions = []
    for l in [l.rstrip() for l in open(F) if len(l) > 2]:
        if l[1] == '1':
            in_stack = False
            stack_count = int(max(l.strip().split(' ')))
        elif in_stack:
            raw_stacks.insert(0, l)
        else:
            i = l.split(' ')
            instructions.append([int(i[1]), int(i[3]) - 1, int(i[5]) - 1])

    str_len = stack_count * 4 - 1
    idx = list(range(1, str_len))[0::4]

    stacks = []
    for i in range(stack_count):
        stacks.append([])

    for s in raw_stacks:
        target = 0
        for x in idx:
            if x < len(s):
                if s[x] != ' ':
                    stacks[target].append(s[x])
                target += 1

    return [stacks, instructions]

def main():
    stacks, instructions = parse_input()

    for qty, src, dst in instructions:
        stacks[dst].extend(stacks[src][-1 * qty:])
        stacks[src] = stacks[src][: -1 * qty ]

    return ''.join([x[-1] for x in stacks])


if __name__ == '__main__':
    answer = main()
    print(answer)
    assert answer == 'MGDMPSZTM'

# MGDMPSZTM