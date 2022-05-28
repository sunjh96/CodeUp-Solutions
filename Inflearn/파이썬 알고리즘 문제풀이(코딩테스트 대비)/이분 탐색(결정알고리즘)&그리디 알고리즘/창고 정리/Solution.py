import sys

k = int(sys.stdin.readline())
box = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())

box.sort(reverse=True)
for _ in range(m):
    box[0] -= 1
    box[k - 1] += 1
    box.sort(reverse=True)

print(box[0] - box[k - 1])
