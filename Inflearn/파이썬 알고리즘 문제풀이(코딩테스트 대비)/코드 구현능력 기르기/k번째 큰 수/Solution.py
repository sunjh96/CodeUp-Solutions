from itertools import combinations

n, k = map(int, input().split())
num = list(map(int, input().split()))
sum = 0
sum_list = []

for i in list(combinations(num, 3)):
    for x in i:
        sum += x
    sum_list.append(sum)
    sum = 0

sum_list = list(set(sum_list))
sum_list.sort(reverse=True)
print(sum_list[k - 1])

'''  ## Combination을 사용하지 않았을경우 ##
n, k = map(int, input().split())
num = list(map(int, input().split()))
res = set()

for i in range(n):
    for j in range(i + 1, n):
        for m in range(j + 1, n):
            res.add(num[i] + num[j] + num[m])

res = list(res)
res.sort(reverse = True)
print(res[k-1])
'''