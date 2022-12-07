# F = './day_07/test.dat'
F = './day_07/puzzle.dat'

ROOT = '/'

def main():
    tree = {
        ROOT: 0
    }
    path = ROOT

    for l in [l.strip() for l in open(F)]:
        match l.split():
            case '$', 'cd', '/'  : path = ROOT
            case '$', 'cd', '..' : path = '-'.join(path.split('-')[0:-1]) if path != ROOT else ROOT
            case '$', 'cd', chdir: path = path + f'-{chdir}' if chdir != ROOT else ROOT
            case '$', 'ls'       : pass
            case 'dir', new_dir  : tree.setdefault(path + f'-{new_dir}', 0)
            case size, _:
                tree[path] += int(size)
                for i in range(path.count('-')):
                    tree['-'.join(path.split('-')[0:i+1])] += int(size)

    return sum(i for i in tree.values() if i <= 100000)


if __name__ == '__main__':
    answer = main()
    print(answer)
    assert answer == 1077191

# 1077191