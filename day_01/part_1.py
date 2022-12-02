F = './day_01/puzzle.dat'

def main():
    res = [0]

    for l in [int(l.strip()) if len(l.strip()) else 0 for l in open(F)]:
        if l == 0:
            res.append(0)
        res[-1] += l

    return max(res)


if __name__ == '__main__':
    answer = main()
    assert answer == 66487
    print(answer)

# 66487