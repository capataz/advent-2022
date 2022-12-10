# F = './day_10/test.dat'
F = './day_10/puzzle.dat'

CHECK_POINTS = [20, 60, 100, 140, 180, 220]


def main():
    sig = cycle = 1
    strength = 0

    for l in open(F):
        match l.strip().split():
            case 'addx', ins:
                strength += sig * cycle * (cycle in CHECK_POINTS)
                cycle += 1
                strength += sig * cycle * (cycle in CHECK_POINTS)
                sig += int(ins)
                cycle += 1

            case ['noop']:
                strength += sig * cycle * (cycle in CHECK_POINTS)
                cycle += 1

    return strength


if __name__ == '__main__':
    answer = main()
    print(answer)
    assert answer == 13820

# 13820