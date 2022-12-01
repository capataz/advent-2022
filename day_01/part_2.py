from types import SimpleNamespace

def process_line(input, v):
    if len(input):
        v.total_cal += int(input)
    else:
        v.cals.append(v.total_cal)
        v.total_cal = 0

def main():
    v = SimpleNamespace(**{
        'cals': [],
        'total_cal': 0
    })

    with open('./day_01/puzzle.dat') as f:
        [process_line(ln.strip(), v) for ln in f]

    v.cals.sort()

    return sum(v.cals[-3:])


if __name__ == '__main__':
    print(main())
