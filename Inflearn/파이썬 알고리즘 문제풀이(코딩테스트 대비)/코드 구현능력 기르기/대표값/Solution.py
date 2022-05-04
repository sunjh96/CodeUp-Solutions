n = int(input())
arr = list(map(int, input().split()))

avg = sum(arr) / n
avg = avg + 0.5
avg = int(avg)
min = float('inf')

for idx, score in enumerate(arr):
    tmp = abs(avg - score)
    if tmp < min:
        min = tmp
        index = idx
    elif tmp == min:
        if score > arr[index]:
            min = tmp
            index = idx

print(f'{avg} {index + 1}')

'''
n = int(input())    내가 푼 코드(비효율적) 파이썬 round 는 round-half-even방식
arr = list(map(int, input().split()))
score_min = float('inf')
avg = 0
indxx = 0

avg = round(sum(arr) / n)

for idx, num in enumerate(arr):
    if abs(avg - num) < score_min:
        score_min = abs(avg - num)
        index = idx
    elif abs(avg - num) == score_min:
        if num > arr[index]:
            score_min = abs(avg - num)
            index = idx
        elif num == arr[index]:
            if idx < index:
                score_min = abs(avg - num)
                index = idx

print(f'{avg} {index + 1}')
'''