import sys

from collections import deque

queue = deque()

n, k = map(int, sys.stdin.readline().split())

for i in range(1, n + 1):
    queue.append(i)

while(len(queue) != 1):
    queue.rotate(-(k - 1))
    queue.popleft()

print(*queue)
