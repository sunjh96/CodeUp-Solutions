import sys
from itertools import product
input = sys.stdin.readline


def sol_product():
    cnt = 0
    nums = [i for i in range(1, n + 1)]

    for num in product(nums, repeat=m):
        print(*num)
        cnt += 1
    print(cnt)


def DFS(v):
    global cnt

    if v == m:
        print(*ch, sep=" ")
        cnt += 1
    else:
        for i in range(1, n + 1):
            ch[v] = i
            DFS(v + 1)


if __name__ == '__main__':
    n, m = map(int, input().split())
    ch = [0 for _ in range(m)]
    cnt = 0

    DFS(0)
    print(cnt)
