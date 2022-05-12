n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
m = int(input())
dir = [list(map(int, input().split())) for _ in range(m)]

ans = s = 0
e = n -1

for i in range(m):
    if dir[i][1] == 0:
        arr[dir[i][0] - 1] = arr[dir[i][0] - 1][dir[i][2]:] + arr[dir[i][0] - 1][:dir[i][2]]
    else:
        arr[dir[i][0] - 1] = arr[dir[i][0] - 1][- dir[i][2]:] + arr[dir[i][0] - 1][:- dir[i][2]]

for i in range(n):
    for j in range(s, e + 1):
        ans += arr[i][j]
    if i < n // 2:
        s += 1
        e -= 1
    else:
        s -= 1
        e += 1

print(ans)