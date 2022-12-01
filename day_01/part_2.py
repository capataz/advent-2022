
def main():
    cals = []
    total_cal = 0

    with open('./day_01/puzzle.dat') as f:
        for ln in f:
            ln = ln.strip()
            if len(ln):
                total_cal += int(ln)
            else:
                cals.append(total_cal)
                total_cal = 0

    cals.sort()

    return sum(cals[-3:])


if __name__ == '__main__':
    print(main())
