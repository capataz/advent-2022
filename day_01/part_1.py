from types import SimpleNamespace

def process_line(input, v):

    if len(input):
        v.current_cal += int(input)
    else:
        # Indicates an empty line, reset counters
        if v.current_cal > v.max_cal:
            v.max_cal = v.current_cal
            v.max_id = v.current_id
        v.current_cal = 0
        v.current_id += 1


def main():
    v = SimpleNamespace(**{
        'current_cal': 0,
        'current_id': 0,
        'max_cal': -1,
        'max_id': -1
        })


    with open('./day_01/puzzle.dat') as f:
        [process_line(ln.strip(), v) for ln in f]

    return f'{v.max_id} - {v.max_cal}'


if __name__ == '__main__':
    print(main())
