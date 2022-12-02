
SELECT = {
    'X': 1,
    'Y': 2,
    'Z': 3
}

WIN = {
    ('A','X'): 3, #R, R draw  0 - 0 + 4 = 4 % 3 = 1 * 3 = 3
    ('A','Y'): 6, #R, P win   1 - 0 + 4 = 5 % 3 = 2 * 3 = 6
    ('A','Z'): 0, #R, S loss  2 - 0 + 4 = 6 % 3 = 0 * 3 = 0

    ('B','X'): 0, #P, R loss  0 - 1 + 4 = 3 % 3 = 0 * 3 = 0
    ('B','Y'): 3, #P, P draw  1 - 1 + 4 = 4 % 3 = 1 * 3 = 3
    ('B','Z'): 6, #P, S win   2 - 1 + 4 = 5 % 3 = 2 * 3 = 6

    ('C','X'): 6, #S, R win   0 - 2 + 4 = 2 % 3 = 2 * 3 = 6
    ('C','Y'): 0, #S, P loss  1 - 2 + 4 = 3 % 3 = 0 * 3 = 0
    ('C','Z'): 3, #S, S draw  2 - 2 + 4 = 4 % 3 = 1 * 3 = 3
}


def calculate_points(them, me):
    return SELECT[me] + WIN[(them, me)]


def main():
    # Rock = 0
    # Paper = 1
    # Scissors = 2
    ips = [(ord(i[0]) - ord('A'), ord(i[2]) - ord('X'))  for i in open('./day_02/puzzle.dat')]

    return sum([(((i[1] - i[0] + 4) % 3) * 3) + (i[1] + 1) for i in ips])


    #return sum([calculate_points(*i.strip().split(' '))
    #    for i in open('./day_02/puzzle.dat')])


if __name__ == '__main__':
    answer = main()
    print(answer)
    assert answer == 13809