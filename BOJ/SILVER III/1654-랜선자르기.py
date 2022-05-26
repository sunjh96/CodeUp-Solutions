def check_ans(mid):
    cnt = 0
    for x in arr:
        cnt += x // mid

    return cnt


n, m = map(int, input().split())
arr = []

for i in range(n):
    arr.append(int(input()))

first = 1
last = max(arr)
ans = 0

while(True):
    mid = (first + last) // 2
    cnt = check_ans(mid)

    if last < first:
        break
    if cnt >= m:
        ans = mid
        first = mid + 1
    elif cnt < m:
        last = mid - 1
    else:
        first = mid + 1

print(ans)
