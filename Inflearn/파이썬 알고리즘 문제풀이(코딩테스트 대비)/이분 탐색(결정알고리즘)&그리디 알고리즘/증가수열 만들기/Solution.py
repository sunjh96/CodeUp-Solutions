import sys
from collections import deque

n = int(sys.stdin.readline())
arr = deque(map(int, sys.stdin.readline().split()))

seq = []
dir = []

if arr[0] < arr[-1]:
    seq.append(arr.popleft())
    dir.append('L')
else:
    seq.append(arr.pop())
    dir.append('R')

while(True):
    if arr[0] < seq[-1] and arr[-1] < seq[-1]:
        break
    elif seq[-1] < arr[0] and seq[-1] < arr[-1]:
        if arr[0] < arr[-1]:
            seq.append(arr.popleft())
            dir.append('L')
        elif arr[-1] < arr[0]:
            seq.append(arr.pop())
            dir.append('R')
    elif seq[-1] < arr[0]:
        seq.append(arr.popleft())
        dir.append('L')
    else:
        seq.append(arr.pop())
        dir.append('R')

print(len(seq))
for y in dir:
    print(y, end='')
