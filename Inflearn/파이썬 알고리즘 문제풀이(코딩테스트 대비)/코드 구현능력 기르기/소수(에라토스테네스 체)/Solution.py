n = int(input())
arr = [1, 1] + [0] * (n - 1)

for i in range(2, n + 1):
    if arr[i] == 0:
        for j in range(i * 2, n + 1, i):
            arr[j] = 1

print(arr.count(0))