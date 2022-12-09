import numpy as np

# F = './day_08/test.dat'
F = './day_08/puzzle.dat'

def main():
    rows = [[int(i) for i in l.strip()] for l in open(F)]
    t_rows = list(map(list, zip(*rows)))

    visible = np.zeros_like(rows, int)

    for i, row in enumerate(t_rows):
        for j, tree in enumerate(row):
            if j == len(row) - 1 or tree > max(row[j+1:]) or \
                j == 0 or tree > max(row[0:j]):
                visible[j][i] = 1

    for i, row in enumerate(rows):
        for j, tree in enumerate(row):
            if j == len(row) - 1 or tree > max(row[j+1:]) or \
                j == 0 or tree > max(row[0:j]):
                visible[i][j] = 1

    return sum([sum(x) for x in visible])

if __name__ == '__main__':
    answer = main()
    print(answer)
    assert answer == 1807

# 1807