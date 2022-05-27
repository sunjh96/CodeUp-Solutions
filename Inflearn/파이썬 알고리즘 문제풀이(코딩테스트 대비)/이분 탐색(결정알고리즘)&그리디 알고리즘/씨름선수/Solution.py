import sys

n = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

cnt = 0
largest = 0
arr.sort(key=lambda x: (x[0], x[1]), reverse=True)

for x, y in arr:
    if largest < y:
        largest = y
        cnt += 1

print(cnt)
