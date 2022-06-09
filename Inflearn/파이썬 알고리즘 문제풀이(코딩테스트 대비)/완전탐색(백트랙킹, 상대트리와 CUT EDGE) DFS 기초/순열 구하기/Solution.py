import sys
input = sys.stdin.readline


def DFS(v):
    global cnt, res, ch
    if v == r:
        print(*res, sep=" ")
        cnt += 1
    else:
        for i in range(1, n + 1):
            if ch[i] == 0:
                ch[i] = 1
                res[v] = i
                DFS(v + 1)
                ch[i] = 0


if __name__ == '__main__':
    n, r = map(int, input().split())
    res = [0 for _ in range(r)]
    ch = [0 for _ in range(n + 1)]
    cnt = 0

    DFS(0)
    print(cnt)
