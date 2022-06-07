import sys
input = sys.stdin.readline


def DFS(arr, weight_sum):
    if weight_sum >= limit:
        print(arr)
    else:
        arr.append(weights.pop(0))
        DFS(arr, weight_sum + arr[-1])
        DFS(arr, weight_sum)


if __name__ == '__main__':
    limit, n = map(int, input().split())
    weights = [int(input()) for _ in range(n)]
    print(DFS([], 0))
