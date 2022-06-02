import sys
from collections import defaultdict

word1 = list(sys.stdin.readline().strip())
word2 = list(sys.stdin.readline().strip())
counter = defaultdict(int)


for word in word1:
    counter[word] += 1

for word in word2:
    counter[word] -= 1

if any(val != 0 for key, val in counter.items()):
    print('NO')
else:
    print('YES')
