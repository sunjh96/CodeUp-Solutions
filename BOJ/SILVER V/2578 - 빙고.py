import sys
input = sys.stdin.readline


def sol():
    for x in arr:
        for idx, val in enumerate(bingo):
            if x in val:
                val[val.index(x)] = 0
                if check():
                    return arr.index(x) + 1
                break


def check():
    cnt = 0

    for x in bingo:
        if sum(x) == 0:
            cnt += 1

    for i in range(5):
        sum_col = 0
        for j in range(5):
            sum_col += bingo[j][i]
        if sum_col == 0:
            cnt += 1

    sum_diag = 0
    for i in range(5):
        sum_diag += bingo[i][i]

    if sum_diag == 0:
        cnt += 1
    sum_diag = 0
    for j in range(5):
        sum_diag += bingo[4 - j][j]
    if sum_diag == 0:
        cnt += 1

    if cnt >= 3:
        return True
    else:
        return False


if __name__ == '__main__':
    arr = []
    bingo = [list(map(int, input().split())) for _ in range(5)]

    for i in range(5):
        arr = arr + list(map(int, input().split()))

    print(sol())
