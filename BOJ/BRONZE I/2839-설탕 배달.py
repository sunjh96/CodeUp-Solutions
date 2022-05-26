import sys

n = int(sys.stdin.readline())
cnt = 0

while(n >= 0):
    if n % 5 == 0:
        cnt += n // 5
        break
    else:
        n = n - 3
        cnt += 1
else:
    cnt = -1

print(cnt)
