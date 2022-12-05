# F = './day_04/test.dat'
F = './day_04/puzzle.dat'

def main():
    overlap = 0
    for a, b in [l.strip().split(',') for l in open(F)]:

        a_min, a_max = [int(i) for i in a.split('-')]
        b_min, b_max = [int(i) for i in b.split('-')]
        overlap += \
            a_max == b_min or \
            b_max == a_min or \
            a_max == b_max or \
            a_min == b_min or \
            (a_max > b_min and a_min < b_min) or \
            (b_max > a_min and b_min < a_min)

    return overlap


if __name__ == '__main__':
    answer = main()
    print(answer)
    assert answer == 924

# 562