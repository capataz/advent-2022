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

    if current_val < mp[x][y] - 1:
        # Too tall to move
        return

    visited[x][y] = count


def main():
    mp = np.array([[string.ascii_letters.index(c) for c in t]
        for t in [list(x) for x in [l.strip() for l in open(F)]]])
    x, y = [c[0] for c in np.where(mp == 44)]
    target_x, target_y = [c[0] for c in np.where(mp == 30)]
    max_x = len(mp)
    max_y = len(mp[0])

    mp[target_x][target_y] = string.ascii_letters.index('z') # override height
    mp[x][y] = 0

    visited = np.zeros_like(mp)
    visited[x][y] = 1

    step = 1
    while True:
        for i, row in enumerate(visited):
            for j, val in enumerate(row):
                if val == step:
                    if i == target_x and j == target_y:
                        return step - 1

                    mark(mp[i][j], i+1, j, step + 1, max_x, max_y, visited, mp)
                    mark(mp[i][j], i-1, j, step + 1, max_x, max_y, visited, mp)
                    mark(mp[i][j], i, j+1, step + 1, max_x, max_y, visited, mp)
                    mark(mp[i][j], i, j-1, step + 1, max_x, max_y, visited, mp)
        step += 1


if __name__ == '__main__':
    answer = main()
    print(answer)
    assert answer == 484

# 1702