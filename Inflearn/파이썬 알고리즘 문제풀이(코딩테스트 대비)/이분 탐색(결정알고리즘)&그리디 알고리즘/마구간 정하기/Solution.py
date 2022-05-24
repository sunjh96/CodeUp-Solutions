n, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]

arr.sort()

start = arr[0]
finish = arr[n - 1]