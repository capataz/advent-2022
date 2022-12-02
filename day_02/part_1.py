
SELECT = {
    'X': 1,
    'Y': 2,
    'Z': 3
}

WIN = {
    ('A','X'): 3, #R, R draw
    ('A','Y'): 6, #R, P win
    ('A','Z'): 0, #R, S loss

    ('B','X'): 0, #P, R loss
    ('B','Y'): 3, #P, P draw
    ('B','Z'): 6, #P, S win
    
    ('C','X'): 6, #S, R win
    ('C','Y'): 0, #S, P loss
    ('C','Z'): 3, #S, S draw
}


def calculate_points(them, me):
    return SELECT[me] + WIN[(them, me)]


def main():
    return sum([calculate_points(*i.strip().split(' '))
        for i in open('./day_02/puzzle.dat')])


if __name__ == '__main__':
    print(main())