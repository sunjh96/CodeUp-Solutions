n = 9
arr = [list(map(int, input().split())) for _ in range(n)]

ans = True
check = [1, 2, 3, 4, 5, 6, 7, 8, 9]
temp = []
s = e = 0

for i in range(n):
    temp = sorted(arr[i])
    if temp != check:
        ans = False
        break

if ans:
    for i in range(n):
        temp = []
        for j in range(n):
            if arr[j][i] in temp:
                ans = False
                break
            else:
                temp.append(arr[j][i])

if ans:
    for i in range(n):
        temp = []
        for j in range(3):
            for k in range(3):
                if arr[s][e] in temp:
                    ans = False
                    break
                else:
                    temp.append(arr[s][e])
                    e += 1
            e -= 3
            s += 1
        s -= 3
        e += 3
        if e == 9:
            s += 3
            e = 0

if ans:
    print('YES')
else:
    print('NO')