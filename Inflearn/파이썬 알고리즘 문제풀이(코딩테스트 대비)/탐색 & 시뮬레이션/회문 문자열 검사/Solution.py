n = int(input())
arr = []
for i in range(n):
    arr.append(str(input()))
    print(arr.reverse())
    if arr[i] == arr.reverse():
        print(f'#{i} YES')
    else:
        print(f'#{i} NO')