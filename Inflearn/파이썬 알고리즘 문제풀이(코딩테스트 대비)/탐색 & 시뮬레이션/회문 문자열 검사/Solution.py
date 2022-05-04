n = int(input())
arr = []

for i in range(n):
    string = input()
    string = string.lower()
    if string == string[::-1]:
        print(f'#{i + 1} YES')
    else:
        print(f'#{i + 1} NO')

'''
for i in range(n):
    string = input()
    string = string.lower()

    for j in range(len(string) // 2):
        if string[j] != string[-1-j]:
            print("%d NO" %(i + 1))
            break
    else:
        print("%d YES" %(i + 1))
'''