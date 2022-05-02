def k_num(s, e, k, num):
    num1 = sorted(num[s-1:e])
    return num1[k - 1]

t = int(input())

for i in range(1, t + 1):
    n, s, e, k = map(int, input().split())
    num = list(map(int, input().split()))
    print(f'#{i} {k_num(s, e, k, num)}')