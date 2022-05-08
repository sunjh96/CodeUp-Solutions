n, m = map(int, input().split())
arr = list(map(int, input().split()))

sum = 0
cnt = 0

for i in range(len(arr)):
    sum = arr[i]
    if sum == m:
        cnt += 1
        continue
    for j in range(i + 1, len(arr)):
        sum += arr[j]
        if sum > m:
            break
        elif sum == m:
            cnt += 1
            break
    else:
        break

print(cnt)