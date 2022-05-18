n , m = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()
start = 0
end = n - 1

while(True):
    mid = (start + end) // 2
    if arr[mid] == m:
        ans = mid
        break
    elif arr[mid] < m:
        start = mid + 1
    else:
        end = mid - 1

print(ans + 1)