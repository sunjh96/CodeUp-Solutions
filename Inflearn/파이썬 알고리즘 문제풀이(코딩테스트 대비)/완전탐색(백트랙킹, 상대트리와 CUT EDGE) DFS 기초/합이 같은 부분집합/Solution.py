import sys
input = sys.stdin.readline


def DFS(idx, num_sum):
    if num_sum > total // 2:
        return
    if idx == n:
        if num_sum * 2 == total:
            print('YES')
            sys.exit(0)
    else:
        DFS(idx + 1, num_sum + arr[idx])
        DFS(idx + 1, num_sum)


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    total = sum(arr)

    DFS(0, 0)
    print('NO')
