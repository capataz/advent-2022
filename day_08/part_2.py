import numpy as np

# F = './day_08/test.dat'
F = './day_08/puzzle.dat'

def main():
    rows = [[int(i) for i in l.strip()] for l in open(F)]
    t_rows = list(map(list, zip(*rows)))

    view_range = np.ones_like(rows, int)
    
    for i, row in enumerate(t_rows):
        for j, tree in enumerate(row):
            c_down = j + 1
            c_up = j - 1
            down = up = 1

            while c_down < len(row) - 1 and row[c_down] < tree:
                down += 1
                c_down += 1

            while c_up > 0 and row[c_up] < tree:
                up += 1
                c_up -= 1

            view_range[j][i] *= down * up

            if i == 0 or j == 0 or i == len(row) - 1 or j == len(t_rows) - 1:
                view_range[j][i] *= 0


    for i, row in enumerate(rows):
        for j, tree in enumerate(row):
            c_right = j + 1
            c_left = j - 1
            right = left = 1

            while c_right < len(row) - 1 and row[c_right] < tree:
                right += 1
                c_right += 1

            while c_left > 0 and row[c_left] < tree:
                left += 1
                c_left -= 1

            view_range[i][j] *= right * left

    return max([max(x) for x in view_range])


if __name__ == '__main__':
    answer = main()
    print(answer)
    assert answer == 480000

# 8