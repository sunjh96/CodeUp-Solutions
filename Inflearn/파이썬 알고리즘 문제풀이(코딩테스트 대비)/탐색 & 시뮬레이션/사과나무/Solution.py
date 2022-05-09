n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

med = n // 2
res = 0

for i in range(n):
    if i <= med:
        res += sum(arr[i][med - i:med + i + 1])
    else:
        res += sum(arr[i][i - med:n - i + med])
print(res)