n = int(input())
score = list(map(int, input().split()))

for idx, val in enumerate(score):
    if idx == n - 1:
        break
    elif val > 0 and score[idx + 1] == 1:
        score[idx + 1] = val + 1

print(sum(score))