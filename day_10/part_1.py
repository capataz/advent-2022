# F = './day_10/test.dat'
F = './day_10/puzzle.dat'

str_check = [20, 60, 100, 140, 180, 220]

def add_signal_strengh(cycle, sig):
    if cycle in str_check:
        return sig * cycle
    return 0


def main():
    sig = cycle = 1
    strength = 0

    for l in open(F):
        match l.strip().split():
            case 'addx', ins:
                strength += add_signal_strengh(cycle, sig)
                cycle += 1
                strength += add_signal_strengh(cycle, sig)
                sig += int(ins)
                cycle += 1

            case ['noop']:
                strength += add_signal_strengh(cycle, sig)
                cycle += 1

    return strength


if __name__ == '__main__':
    answer = main()
    print(answer)
    assert answer == 13820

# 13820