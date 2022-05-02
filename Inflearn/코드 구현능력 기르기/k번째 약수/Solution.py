def div(x):
    a = []

    for i in range(1, x+1):
        if (x % i) == 0:
            a.append(i)
    a.sort()
    return a

num = []
n = list(map(int, input().split()))
num = div(n[0])

if n[1] > len(num):
    print(-1)
else:
    print(num[n[1] - 1])