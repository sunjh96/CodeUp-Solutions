n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

med = n // 2
res = 0

for i in range(n):
    if i <= med:
        res += sum(arr[i][med - i:med + i + 1])
    else:
        res += sum(arr[i][i - med:n - i + med])
print(res)

# import sys
# sys.stdin = open("input.txt", 'r')
# n=int(input())
# a=[list(map(int, input().split())) for _ in range(n)]
# res=0
# s=e=n//2
# for i in range(n):
#     for j in range(s, e+1):
#         res+=a[i][j]
#     if i<n//2:
#         s-=1
#         e+=1
#     else:
#         s+=1
#         e-=1
# print(res)
