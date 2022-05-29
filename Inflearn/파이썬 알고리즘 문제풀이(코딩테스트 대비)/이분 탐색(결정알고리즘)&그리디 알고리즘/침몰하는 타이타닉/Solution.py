import sys

n, k = map(int, sys.stdin.readline().split())
weight = list(map(int, sys.stdin.readline().split()))

weight.sort()
cnt = i = 0

while(len(weight) > 1):
    if i == len(weight) - 1:
        break
    if weight[0] + weight[-1 - i] <= k:
        cnt += 1
        weight.pop(0)
        weight.pop(-1-i)
        i = 0
    else:
        i += 1

print(cnt + len(weight))
