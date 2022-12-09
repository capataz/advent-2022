import numpy as np

# F = './day_09/test.dat'
F = './day_09/puzzle.dat'


def move_tail(hx, hy, tx, ty):
    x_diff = abs(hx - tx)
    y_diff = abs(hy - ty)
    x_sign = int((hx - tx) / x_diff) if x_diff else 0
    y_sign = int((hy - ty) / y_diff) if y_diff else 0

    if x_diff > 1 or y_diff > 1:
        return [tx + x_sign, ty + y_sign]
    else:
        return [tx, ty]


def main():
    grid = np.zeros((300, 300))
    hx = hy = tx = ty = 0

    for dir, moves in [l.split() for l in [l.strip() for l in open(F)]]:
        for _ in range(int(moves)):
            match dir:
                case 'R': hy += 1
                case 'U': hx += 1
                case 'L': hy -= 1
                case 'D': hx -= 1
            tx, ty = move_tail(hx, hy, tx, ty)
            grid[tx][ty] = 1

    return np.sum(grid)


if __name__ == '__main__':
    answer = main()
    print(answer)
    assert answer == 6188

# 6188
