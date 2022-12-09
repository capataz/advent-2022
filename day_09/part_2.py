import numpy as np

# F = './day_09/test2.dat'
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


def move_snake(snake, hx, hy):
    snake[0][0], snake[0][1] = move_tail(hx, hy, snake[0][0], snake[0][1])
    for i, s in enumerate(snake[1:]):
        s[0], s[1] = move_tail(snake[i][0], snake[i][1], s[0], s[1])


def main():
    hx = hy = 200
    grid = np.zeros((500, 500))
    snake = np.full((9, 2), hx)

    for dir, moves in [l.split() for l in [l.strip() for l in open(F)]]:
        for _ in range(int(moves)):
            match dir:
                case 'R': hy += 1
                case 'U': hx += 1
                case 'L': hy -= 1
                case 'D': hx -= 1
            move_snake(snake, hx, hy)
            grid[int(snake[-1][0])][int(snake[-1][1])] = 1

    return np.sum(grid)


if __name__ == '__main__':
    answer = main()
    print(answer)
    assert answer == 2516

# 2516
