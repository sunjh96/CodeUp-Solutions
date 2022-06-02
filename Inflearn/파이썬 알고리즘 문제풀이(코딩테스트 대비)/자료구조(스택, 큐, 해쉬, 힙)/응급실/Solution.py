import sys
from collections import deque

queue = deque()

n, k = map(int, sys.stdin.readline().split())
priority = list(map(int, sys.stdin.readline().split()))
cnt = 0
front = 0
rear = k

for i in range(n):
    queue.append(priority[i])

while(True):
    if rear < 0:
        rear = len(queue) - 1
    if queue[0] == max(queue):
        if front == rear:
            break
        else:
            queue.popleft()
            cnt += 1
            rear -= 1
    else:
        queue.rotate(-1)
        rear -= 1

print(cnt + 1)
