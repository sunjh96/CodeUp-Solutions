import sys

n = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

arr.sort(key=lambda x: (x[1], x[0]))

cnt = 1
end_time = arr[0][1]

for i in range(1, n):
    if end_time <= arr[i][0]:
        end_time = arr[i][1]
        cnt += 1

print(cnt)
