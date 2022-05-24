def check_ans(arr, num):

    cnt = 0

    temp = arr[0]
    for i in range(1, len(arr)):
        if num <= arr[i] - temp:
            temp = arr[i]
            cnt += 1

    return cnt + 1

n, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]

arr.sort()

start = 1
finish = arr[-1]
ans = 0

while(start <= finish):
    mid = (start + finish) // 2
    res = check_ans(arr, mid)

    if res < k:
        finish = mid - 1
    else:
        ans = mid
        start = mid + 1

print(ans)