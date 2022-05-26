import sys

n = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

arr.sort(key=lambda x: (x[0], x[1]), reverse=True)

print(arr)
