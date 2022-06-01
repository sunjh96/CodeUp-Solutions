import sys

n, k = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

cnt = 0
temp = 0
stack = []

for i in range(k):
    max_cnt = 0
    if stack.count(arr[i]) != 0:
        continue
    if len(stack) < n:
        stack.append(arr[i])
    else:
        for x in stack:
            try:
                if arr[i:].index(x) > max_cnt:
                    max_cnt = arr[i:].index(x)
                    temp = x
            except ValueError:
                temp = x
                break
        stack.remove(temp)
        cnt += 1
        stack.append(arr[i])
print(cnt)
