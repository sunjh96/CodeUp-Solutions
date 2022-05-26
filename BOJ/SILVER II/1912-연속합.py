from re import X
import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

num_sum = arr[0]
dp = num_sum

for x in arr[1:]:
    if num_sum > 0 and num_sum + x > 0:
        num_sum += x
    else:
        num_sum = x
    if dp < num_sum:
        dp = num_sum

print(dp)
