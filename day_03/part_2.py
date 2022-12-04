F = './day_03/puzzle.dat'

from string import ascii_letters

def main():
    total = 0
    group = []
    for i, rk in enumerate([l.strip() for l in open(F)]):
        group.append(set(rk))

        if i % 3 == 2: # Compute and reset every thrid item
            total += ascii_letters.index((group[0] & group[1] & group[2]).pop()) + 1
            group = []

    return total



if __name__ == '__main__':
    answer = main()
    print(answer)
    assert answer == 2585

# 2585