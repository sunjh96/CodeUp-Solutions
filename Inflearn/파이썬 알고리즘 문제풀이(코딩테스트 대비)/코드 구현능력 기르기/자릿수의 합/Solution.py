def digit_sum(x):
    b = []
    for i in range (1, len(str(x)) + 1):
        a = x % pow(10, i)
        b.append(a//pow(10, i-1))
    return sum(b)

n = int(input())
num = list(map(int, input().split()))
max = 0

for i in range(n):
    if max < digit_sum(num[i]):
        max = digit_sum(num[i])
        ans = num[i]

print(ans)

'''
def digit_sum(x):
    sum = 0
    while x>0:
        sum += x % 10
        x = x // 10
    return sum
'''