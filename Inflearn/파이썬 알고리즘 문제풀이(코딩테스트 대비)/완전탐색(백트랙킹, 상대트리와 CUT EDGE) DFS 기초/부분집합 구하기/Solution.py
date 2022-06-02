import sys
input = sys.stdin.readline


def DFS(v):
    if v == num + 1:
        for i in range(1, num + 1):
            if ch[i] == 1:
                print(i, end=' ')
        print()
    else:
        ch[v] = 1
        DFS(v + 1)
        ch[v] = 0
        DFS(v + 1)


if __name__ == '__main__':
    num = int(input())
    ch = [0] * (num + 1)
    DFS(1)
