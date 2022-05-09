n = int(input())
arr = [list(map(int, input().split()))  for _ in range (n)]

max = dig1 = dig2 = 0

for i in range(n):
    sum_col = 0
    if max < sum(arr[i]):
        max = sum(arr[i])
    for j in range(n):
        sum_col += arr[j][i]
    if max < sum_col:
        max = sum_col
    dig1 += arr[i][i]
    dig2 += arr[n - i - 1][i]

if max < dig1:
    max = dig1

if max < dig2:
    max = dig2

print(max)