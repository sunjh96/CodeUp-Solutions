def check_ans(mid):
    sum = 0
    cnt = 0

    for x in arr:
        if sum + x > mid:
            sum = x
            cnt += 1
        else:
            sum += x
    return cnt + 1

k, m = map(int, input().split())
arr = list(map(int, input().split()))

first = 1
last = sum(arr)
res = 0
maxx = max(arr)

while first <= last:
    mid = (first + last) // 2
    cnt = check_ans(mid)

    if mid >= maxx and cnt <= m:
        last = mid - 1
        res = mid
    else:
        first = mid + 1

print(res)