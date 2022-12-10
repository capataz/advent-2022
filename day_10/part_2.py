import numpy as np

F = './day_10/test.dat'
# F = './day_10/puzzle.dat'


def draw_pixel(cycle, sig, screen):
    row = int((cycle - 1) / 40)
    rel_cycle = (cycle - 1) % 40

    if rel_cycle in range(sig - 1, sig + 2):
        screen[row][rel_cycle] = '@'


def main():
    screen = np.full((6, 40), ' ')
    sig = cycle = 1
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