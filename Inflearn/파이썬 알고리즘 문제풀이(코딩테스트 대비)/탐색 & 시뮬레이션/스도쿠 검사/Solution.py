n = 9
arr = [list(map(int, input().split())) for _ in range(n)]

ans = True
check = [1, 2, 3, 4, 5, 6, 7, 8, 9]
temp = []
for i in range(n):
    temp = sorted(arr[i])
    if temp != check:
        ans = False

print(ans)