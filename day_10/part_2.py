import numpy as np

# F = './day_10/test.dat'
F = './day_10/puzzle.dat'


def draw_pixel(cycle, sig, screen):
    if (c:= cycle % 40) in range(sig - 1, sig + 2):
        screen[int(cycle / 40)][c] = '@'


def main():
    screen = np.full((6, 40), ' ')
    cycle = 0
    sig = 1
    for l in open(F):
        match l.strip().split():
            case 'addx', ins:
                draw_pixel(cycle, sig, screen)
                cycle += 1
                draw_pixel(cycle, sig, screen)
                sig += int(ins)
                cycle += 1

            case ['noop']:
                draw_pixel(cycle, sig, screen)
                cycle += 1

    [print(''.join(v)) for v in screen]
    return 0

if __name__ == '__main__':
    answer = main()
    print(answer)
    assert answer == 0

# 13820