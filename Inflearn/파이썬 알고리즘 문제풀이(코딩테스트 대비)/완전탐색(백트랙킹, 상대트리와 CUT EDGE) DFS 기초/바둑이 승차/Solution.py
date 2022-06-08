import sys
input = sys.stdin.readline


def DFS(v, weight_sum, tsum):
    global ans
    if (total - tsum) + weight_sum < ans:
        return
    if weight_sum > limit:
        return
    if v == n:
        if weight_sum > ans:
            ans = weight_sum
    else:
        DFS(v + 1, weight_sum + weights[v], tsum + weights[v])
        DFS(v + 1, weight_sum, tsum + weights[v])


if __name__ == '__main__':
    limit, n = map(int, input().split())
    weights = [int(input()) for _ in range(n)]
    ans = -21470000
    total = sum(weights)

    DFS(0, 0, 0)

    print(ans)
