n, m = map(int, input().split())

arr = [0] * (n + m + 1)
max = 0
cnt = 0

for i in range(1, n + 1):
    for j in range(1, m + 1):
        arr[i + j] += 1

for idx, num in enumerate(arr):
    if max < num:
        max = num
        index = idx
        cnt = 0
    elif max == num:
        cnt += 1

for i in range(cnt + 1):
    print(index + i, end = ' ')
'''
for i in range(len(arr)):
    if arr[i] > max:
        max = arr[i]
for i in range(len(arr)):
    if max == arr[i]:
        print(i, end = " ")
'''