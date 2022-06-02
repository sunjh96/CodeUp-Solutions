import sys
from collections import defaultdict

counter = defaultdict(int)
n = int(sys.stdin.readline())
words = [sys.stdin.readline().strip() for _ in range((2 * n) - 1)]

for word in words:
    counter[word] += 1

for x, y in counter.items():
    if y == 1:
        print(x)
