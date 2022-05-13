n = 7
m = 3
arr = [list(map(int, input().split())) for _ in range(n)]
cnt = 0
ch = []

for i in range(n):
    for j in range(m):
        ch = arr[i][j:j + 5]
        if ch == ch[::-1]:
            cnt += 1

for i in range(n):
    for j in range(m):
        ch = []
        for k in range(5):
            ch.append(arr[k + j][i])
        if ch == ch[::-1]:
            cnt += 1

print(cnt)