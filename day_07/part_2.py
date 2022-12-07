# F = './day_07/test.dat'
F = './day_07/puzzle.dat'

def main():
    tree = {
        '/': 0
    }
    path = '/'

    for l in [l.strip() for l in open(F)]:
        if l[0:4] == '$ cd':
            chdir = l.split(' ')[-1]
            if chdir == '..':
                path = '-'.join(path.split('-')[0:-1]) if len(path) > 1 else '/' # Move up one level unless already at the top of the path
            else: # move one down
                path = path + f'-{chdir}' if chdir != '/' else '/'

        elif l[0:3] == 'dir':
            tree.setdefault(path + f'-{l.split(" ")[-1]}', 0)

        elif l[0:4] == '$ ls':
            continue

        else:  # Anythin else is a file
            tree[path] += (size := int(l.split(' ')[0]))
            for i in range(path.count('-')):
                tree['-'.join(path.split('-')[0:i+1])] += size

    needed = 30000000 - (70000000 - tree['/'])
    smallest_gap = smallest_size = 70000000

    for i in tree.values():
        if i < needed: continue
        if (i - needed) < smallest_gap:
            smallest_gap = i - needed
            smallest_size = i

    return smallest_size


if __name__ == '__main__':
    answer = main()
    print(answer)
    assert answer == 5649896

# 1077191