n = int(input())
arr = list(map(int, input().split()))
m = int(input())
arr1 = list(map(int, input().split()))

ans = []

while True:
    if len(arr) == 0 or len(arr1) == 0:
        ans = ans + arr + arr1
        break
    elif arr[0] <= arr1[0]:
        ans.append(arr.pop(0))
    else:
        ans.append(arr1.pop(0))

print(*ans, end = " ")

''' #이미 sort가 되어있기에 O(nlogn) -- 비효율적
arr = arr + arr1
arr.sort()

print(*arr, end = " ")
'''