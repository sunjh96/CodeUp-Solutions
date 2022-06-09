import sys
input = sys.stdin.readline


def DFS(v, sum_coin):
    global res
    if sum_coin > change or res < v:
        return
    if sum_coin == change:
        if v < res:
            res = v
        return
    else:
        for i in range(n):
            DFS(v + 1, sum_coin + coins[i])


if __name__ == '__main__':
    n = int(input())
    coins = list(map(int, input().split()))
    change = int(input())

    coins.sort(reverse=True)
    res = 21470000

    DFS(0, 0)
    print(res)
