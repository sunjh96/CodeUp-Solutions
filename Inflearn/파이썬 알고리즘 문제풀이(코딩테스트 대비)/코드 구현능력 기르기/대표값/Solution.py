n = int(input())
arr = list(map(int, input().split()))
score_min = float('inf')
avg = 0
indxx = 0

for i in range(n):
    avg += arr[i]

avg = round(avg / n)

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