def prize(x):
    cnt = 0

    for idx, num in enumerate(x):
        if cnt == 2:
            break
        for j in range(idx + 1, len(x)):
            if num == x[j]:
                cnt += 1
                res = num

    if cnt == 1:
        ans = 1000 + res * 100
    elif cnt == 2:
        ans = 10000 + res * 1000
    else:
        ans = max(x) * 100

    return(ans)

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
max_num = 0

for i in range(n):
    if max_num < prize(arr[i]):
        max_num = prize(arr[i])

print(max_num)

'''
max=0
res=0
n=int(input())
for i in range(n):
    tmp=input().split()
    tmp.sort()
    a, b, c=map(int, tmp)
    if a==b and b==c:
        money=10000+(a*1000);
    elif a==b or a==c:
        money=1000+(a*100)
    elif b==c:
        money=1000+(b*100)
    else:
        money=c*100
    if money > res:
        res=money

print(res)
'''