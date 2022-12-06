# F = './day_06/test.dat'
F = './day_06/puzzle.dat'

def main():
    for l in [l.strip() for l in open(F)]:
        for i in range(len(l[13:])):
            if len(set(l[i:i+14])) == 14:
                return i + 14


if __name__ == '__main__':
    answer = main()
    print(answer)
    assert answer == 3559

# 3559