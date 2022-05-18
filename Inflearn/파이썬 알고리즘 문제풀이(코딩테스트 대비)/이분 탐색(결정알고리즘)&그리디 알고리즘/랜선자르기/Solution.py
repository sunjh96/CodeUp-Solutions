def check_ans(ans):
    cnt = 0
    for x in arr:
        cnt += x // ans
    if cnt == m:
        res.append(ans)
        check_ans(ans + 1)
    return cnt, res

n, m = map(int, input().split())
arr = []

for i in range(n):
    arr.append(int(input()))

lt = 0
rt = max(arr)
res = []

while(True):
    mid = (lt + rt) // 2
    cnt, res = check_ans(mid)

    if cnt == m:
        break
    elif cnt < m:
        rt = mid - 1
    elif cnt > m:
        lt = mid + 1

print(max(res))