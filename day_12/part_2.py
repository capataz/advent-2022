import numpy as np
import string

# F = './day_12/test.dat'
F = './day_12/puzzle.dat'


def mark(current_val, x, y, count, max_x, max_y, visited, mp):
    if x >= max_x or y >= max_y or x < 0 or y < 0:
        # Out of grid bounds
        return

    if visited[x][y] and visited[x][y] < count:
        # Already visited on a shorter path
        return

    if current_val - 1 > mp[x][y]:
        # Too tall to move up (in reverse)
        return

    visited[x][y] = count


def main():
    mp = np.array([[string.ascii_letters.index(c) for c in t]
        for t in [list(x) for x in [l.strip() for l in open(F)]]])
    x, y = [c[0] for c in np.where(mp == 30)]
    max_x = len(mp)
    max_y = len(mp[0])

    mp[x][y] = string.ascii_letters.index('z') # override height

    visited = np.zeros_like(mp)
    visited[x][y] = 1

    step = 1
    while True:
        for row_count, row in enumerate(visited):
            for col_count, val in enumerate(row):
                if val == step:
                    if mp[row_count][col_count] == 0:
                        return step - 1

                    mark(mp[row_count][col_count], row_count+1, col_count, step + 1, max_x, max_y, visited, mp)
                    mark(mp[row_count][col_count], row_count-1, col_count, step + 1, max_x, max_y, visited, mp)
                    mark(mp[row_count][col_count], row_count, col_count+1, step + 1, max_x, max_y, visited, mp)
                    mark(mp[row_count][col_count], row_count, col_count-1, step + 1, max_x, max_y, visited, mp)


        step += 1


if __name__ == '__main__':
    answer = main()
    print(answer)
    assert answer == 478

# 478