import numpy as np
import string
from collections import deque

# F = './day_12/test.dat'
F = './day_12/puzzle.dat'

def process(value, x, y, max_x, max_y, visited, mp):
    if x >= max_x or y >= max_y or x < 0 or y < 0 or \
        value < mp[x][y] - 1 or \
        (x, y) in visited:

        return False

    return True


def main():
    mp = np.array([[string.ascii_letters.index(c) for c in t]
        for t in [list(x) for x in [l.strip() for l in open(F)]]])

    x, y = [c[0] for c in np.where(mp == 44)]
    target_x, target_y = [c[0] for c in np.where(mp == 30)]
    mp[target_x][target_y] = string.ascii_letters.index('z') # override height
    mp[x][y] = string.ascii_letters.index('a') # override height

    q = deque([[x, y, 1]])
    visited = set((x, y))
    while True:
        x, y, count = q.popleft()

        if x == target_x and y == target_y:
            return count - 1

        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_x = x + dx
            new_y = y + dy
            if process(mp[x][y], new_x, new_y, len(mp), len(mp[0]), visited, mp):
                q.append([new_x, new_y, count + 1])
                visited.add((new_x, new_y))


if __name__ == '__main__':
    answer = main()
    print(answer)
    assert answer == 484

# 484