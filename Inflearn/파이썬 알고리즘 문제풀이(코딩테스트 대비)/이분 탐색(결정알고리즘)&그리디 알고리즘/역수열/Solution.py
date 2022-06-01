import sys

n = int(sys.stdin.readline())
seq = list(map(int, sys.stdin.readline().split()))

ans = [n for _ in range(n)]

for i in range(1, n + 1):
    cnt = 0
    k = seq[i - 1]
    for j in range(n):
        if i < ans[j]:
            cnt += 1
        if cnt == k + 1:
            ans[j] = i
            break

print(*ans)
