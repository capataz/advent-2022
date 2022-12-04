F = './day_03/puzzle.dat'

priority = '0abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

def main():
    total = 0
    for rk in [l.strip() for l in open(F)]:
        unique = (set(rk[:int(len(rk) / 2)]) & set(rk[int(len(rk) / 2):])).pop()
        total += priority.find(unique)

    return total



if __name__ == '__main__':
    answer = main()
    print(answer)
    assert answer == 7917

# 7917