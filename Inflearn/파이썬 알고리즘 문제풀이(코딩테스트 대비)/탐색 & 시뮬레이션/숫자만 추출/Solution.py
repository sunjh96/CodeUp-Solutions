string = input()
arr = []
ans = 0
cnt = 0

for i in string:
    if i.isdecimal():
        ans = 10 * ans + int(i)

for i in range(1, ans // 2 + 1):
    if ans % i == 0:
        cnt += 1

print(ans, cnt + 1)
# isalpha, isdecimal, isupper, islower
'''
for i in string:
    if i.isalpha() == False:
        arr.append(i)

ans = "".join(arr)
ans = int(ans)

for i in range(1, ans // 2 + 1):
    if ans % i == 0:
        cnt += 1

print(ans, cnt + 1)
'''
